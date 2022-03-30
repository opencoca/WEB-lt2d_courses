 /**
 * Implements functionality needed for the AI guide that loads Snap! projects into iframes
 * Authors: Ken Kahn
 * License: New BSD
 */

let world;
let ide_morph;
window.addEventListener('load', function () {
	var world_canvas = document.getElementById('world');
	ide_morph = new IDE_Morph();
	var loop = function loop() {
		requestAnimationFrame(loop);
		world.doOneCycle();
	};
	let full_screen = true;
	let edit_mode = window.location.href.indexOf('editMode') >= 0;
	let run_full_screen = window.location.href.indexOf('noRun') < 0;
	let project_path;
	let show_palette = true; // unless in an iframe where the default is to hide it for space reasons
	world = new WorldMorph(world_canvas);
//  world.worldCanvas.focus(); // not good for pages with iframes containing Snap! programs
	ide_morph.openIn(world);
	if (window !== window.parent) { // if running in an iframe setup snap for that
	    if (!window.frameElement) {
	    	if (window.location.protocol !== 'https:' && window.location.protocol !== 'http:') {
	    		alert("Cannot load project into Snap! since URL protocol is neither HTTPS nor HTTP.");
	    	} else {
				alert("Sorry something has gone wrong with loading projects into Snap! on this page.");
	    	}
	    	return;
	    }
		
		run_full_screen = run_full_screen || window.frameElement.getAttribute("run_full_screen");
		full_screen = run_full_screen || full_screen || window.frameElement.getAttribute("full_screen");
		edit_mode = edit_mode || window.frameElement.getAttribute("edit_mode");
		show_palette = window.frameElement.getAttribute("show_palette");
		let stage_scale = window.frameElement.getAttribute("stage_ratio");
		
		if (!full_screen && edit_mode) {
			ide_morph.controlBar.hide();    // no need for the control bar
			ide_morph.toggleAppMode(false); // launch in edit mode
		}
		if (stage_scale) {
			ide_morph.toggleStageSize(true, +stage_scale);
		}
		ide_morph.setBlocksScale(1); // the chapter projects were designed with default block size (though scaled via CSS)
		window.onbeforeunload = function () {}; // don't bother the user about reloading
		window.speechSynthesis.getVoices();     // no need to wait for them to load
	}
	loadAutosaveOrSample();
	loop();
// 	window.addEventListener('load', loop);
});

function load_project_path_if_exists() {
	const load_project_string =
		function (project_text) {
			// timeout wasn't needed before Snap 4.1
			// without it iframes show only Snap! background texture
			if (!project_text || project_text.indexOf('Status 404 – Not Found') >= 0) {
				ide_morph.showMessage("Error fetching " + project_path);
				return;
			}
			setTimeout(function () {
				const parameters = new URLSearchParams(window.parent.location.hash);
				if (parameters.get('locale')) {
					// Snap uses _ instead of - in two part language code names
					ide_morph.setLanguage(parameters.get('locale').replace('-', '_'));
				}
				ide_morph.rawOpenProjectString(project_text);
				if (window.location.href.indexOf('editMode') >= 0) {
					ide_morph.toggleAppMode(false);
				} else if (full_screen) {
					ide_morph.toggleAppMode(true);
					if (run_full_screen) {
						ide_morph.runScripts();
					}
				}
				ide_morph.showMessage(""); // remove message
// 				if (!show_palette && full_screen && edit_mode) {
//                 ide_morph.setPaletteWidth(0);
//              }
			},
				1000);
		};


	if (hasProjectPath()) {
		project_path = window.frameElement.getAttribute("project_path");
		// fetch and load
		ide_morph.showMessage("Loading...", 10);
		fetch(project_path).then(function (response) {
			ide_morph.showMessage("Opening project");
			response.text().then(load_project_string);
		}).catch(function (error) {
			ide_morph.showMessage("Error fetching " + project_path + ": " + error.message);
		});
	}
}


function loadAutosaveOrSample() {
	var ide = world.children[0];
	// Only load library from github if NOT hosted
	if (!hasProjectPath()) {
		// Load in library from github
		fetch("https://raw.githubusercontent.com/Robot-In-A-Can/eBrain-Snap/develop/RIAC%20Blocks.xml")
			.then(response => {
				if (!response.ok) {
					throw new Error('could not fetch RIAC blocks from github');
				}
				return response.text();
			}).then(RIAClibrary => {
				ide.droppedText(RIAClibrary, "RIAC");
				localStorage.setItem("RIAClibrary", RIAClibrary);
			}).catch(error => {
				console.log('cannot load library from internet. Attempting load from cache');
				if (localStorage.getItem("RIAClibrary") !== undefined) {
					ide.droppedText(localStorage.getItem("RIAClibrary"), "RIAC");
				} else {
					alert("Cannot load RIAC library");
				}
			}).then(loadAutosave);
	} else {
		loadAutosave();
	}
}

function loadAutosave() {
	var ide = world.children[0];
	var storedProject = localStorage.getItem("snapIDE" + autosavePath());
	if (storedProject) {
		askYesNo("Load project?", "Do you want to load the project you were working on?",
			function (button) {
				// Must delay autosave until after a selection is made, otherwise empty project will be auto saved.
				if (button) {
					ide.openProjectString(storedProject, startAutosave);
				} else {
					load_project_path_if_exists(); // Attempt to load project from the iframe parameter.
					startAutosave();
				}
			});
	} else {
		load_project_path_if_exists(); // Attempt to load project from the iframe parameter.
		startAutosave();
	}
}

/**
 * Start project autosave every 15 seconds.
 */
function startAutosave() {
	var saveInterval = setInterval(function () {
		var ide = world.children[0];
		var xml = ide.serializer.serialize(new Project(ide.scenes, ide.scene));
		localStorage.setItem("snapIDE" + autosavePath(), xml);
	}, 15000);
}

function autosavePath() {
	if (hasProjectPath()) {
		var projectPath = window.frameElement.getAttribute("project_path");
		return "snapIDE" + projectPath;
	} else {
		return "snapIDE" + window.location.href;
	}
}

function hasProjectPath() {
	try {
		return window.frameElement && window.frameElement.getAttribute("project_path");
	} catch (e) {
		return false;
	}
}