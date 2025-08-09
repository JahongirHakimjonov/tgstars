const CACHE = 'tg-gallery-v1';
const ASSETS = [
    '/',
    '/index.html',
    'https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css',
    'https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js'
    // add other static assets or image prefixes you want cached
];

self.addEventListener('install', evt => {
    evt.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
    self.skipWaiting();
});

self.addEventListener('activate', evt => {
    evt.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', evt => {
    const req = evt.request;
    // network-first for html / api, cache-first for images & static
    if (req.destination === 'document' || req.url.endsWith('.html')) {
        evt.respondWith(fetch(req).catch(() => caches.match('/')));
        return;
    }

    if (req.destination === 'image' || req.url.includes('/picsum.photos/')) {
        evt.respondWith(caches.match(req).then(r => r || fetch(req).then(resp => {
            const copy = resp.clone();
            caches.open(CACHE).then(cache => cache.put(req, copy));
            return resp;
        })));
        return;
    }

    evt.respondWith(caches.match(req).then(r => r || fetch(req)));
});
