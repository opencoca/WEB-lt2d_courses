var cacheName = 'snap-pwa',
    filesToCache = [
        'Snap/snap.html',
        'asteroids.xml',
        'player.html',

        // program
        'Snap/src/morphic.js',
        'Snap/src/symbols.js',
        'Snap/src/widgets.js',
        'Snap/src/blocks.js',
        'Snap/src/threads.js',
        'Snap/src/objects.js',
        'Snap/src/scenes.js',
        'Snap/src/gui.js',
        'Snap/src/paint.js',
        'Snap/src/lists.js',
        'Snap/src/byob.js',
        'Snap/src/tables.js',
        'Snap/src/sketch.js',
        'Snap/src/video.js',
        'Snap/src/maps.js',
        'Snap/src/extensions.js',
        'Snap/src/xml.js',
        'Snap/src/store.js',
        'Snap/src/locale.js',
        'Snap/src/cloud.js',
        'Snap/src/api.js',
        'Snap/src/sha512.js',
        'Snap/src/FileSaver.min.js'
    ];

/* Start the service worker and cache all of the app's content */
self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('activate', (evt) => {
    evt.waitUntil(
        caches.keys().then((keyList) => {
            return Promise.all(keyList.map((key) => {
                if (key !== cacheName) {
                    return caches.delete(key);
                }
            }));
        })
    );
    self.clients.claim();
});

/* Serve cached content when offline */
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});
