var cacheName = '{{ snap.slug }}-pwa',
    filesToCache = [
        '/static/snap/Snap/snap-no-logging.html',
        '/media/{{ snap.file }}',
        '{% url "courses:snap_detail" snap.slug %}',

        // program
        '/static/snap/Snap/src/morphic.js',
        '/static/snap/Snap/src/symbols.js',
        '/static/snap/Snap/src/widgets.js',
        '/static/snap/Snap/src/blocks.js',
        '/static/snap/Snap/src/threads.js',
        '/static/snap/Snap/src/objects.js',
        '/static/snap/Snap/src/scenes.js',
        '/static/snap/Snap/src/gui.js',
        '/static/snap/Snap/src/paint.js',
        '/static/snap/Snap/src/lists.js',
        '/static/snap/Snap/src/byob.js',
        '/static/snap/Snap/src/tables.js',
        '/static/snap/Snap/src/sketch.js',
        '/static/snap/Snap/src/video.js',
        '/static/snap/Snap/src/maps.js',
        '/static/snap/Snap/src/extensions.js',
        '/static/snap/Snap/src/xml.js',
        '/static/snap/Snap/src/store.js',
        '/static/snap/Snap/src/locale.js',
        '/static/snap/Snap/src/cloud.js',
        '/static/snap/Snap/src/api.js',
        '/static/snap/Snap/src/sha512.js',
        '/static/snap/Snap/src/FileSaver.min.js'
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