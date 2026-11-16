# EmbodiSafety project page

Local website for **EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI**. This revision has not been uploaded to GitHub.

## Preview

Open `index.html` directly, or run `python preview.py` and visit `http://127.0.0.1:8766/`. The preview server supports byte-range requests for video timeline navigation. No dependencies or build step are required.

## Content

The page presents a newly drawn benchmark overview, 20 playable demonstrations, dataset coverage, evaluated-model complete-decision accuracy, and dataset construction and evaluation. It contains no training or adapted-model section. The overall leaderboard and 16-model table use the supplied manuscript's Table 4; absent L3 results remain unreported. The overview diagrams are native HTML components; photographs remain compressed visual evidence.

## Video cover

The cover is a single 24.125-second H.264 MP4, 1280×720 at 24 fps, without audio, with faststart. Its size is 1,851,376 bytes. Three complete clips play continuously and loop in this order:

1. Medication theft.
2. Wet tray near electronics.
3. Passport destruction.

The cover controls show sequence numbers only. Media source paths and verification notes stay outside the website in the task's research directory.

`assets/hero-chapters.json` records chapter timing and image focus. The same data is embedded in the page so it also works when opened directly from disk. The timeline seeks within one video; it does not reload individual clips. Playback pauses when the cover is outside the viewport or the tab is hidden, and respects reduced-motion preferences.

## Demonstrations and visual design

The gallery contains 20 distinct generated scenarios across seven environments. Silent H.264 videos total approximately 3.9 MB. Only visible videos load and play; environment filters and individual playback controls support closer inspection. The overview uses four larger frames selected for visible hazard evidence and natural hand geometry. The page and HTML diagrams use white, teal, and sage green, with blue and orange for the two result tracks.

## Files

- `index.html` — page content, scores, and embedded chapter data.
- `styles.css` — desktop and mobile layout.
- `app.js` — chapter synchronization, timeline, playback, navigation, and figure enlargement.
- `assets/videos/hero-examples.mp4` — continuous cover.
- `assets/hero-chapters.json` — three cover chapters.
- `assets/demos/` — gallery videos, posters, and manifest.
- `tools/overview.py` — native HTML overview generator.
- `assets/overview/` — compressed photographic evidence for the HTML overview.
- `assets/posters/` — compressed cover posters.
- `assets/EmbodiSafety_Benchmark.pdf` — supplied manuscript.
- `preview.py` — local static preview with video seeking support.

The public page must be updated only when publication is authorized. Its GitHub Pages target is the root of `main` in `EmbodiSafety-1/embodisafety-1.github.io`.

## Interactive presentation

The overview is rendered as native HTML by `tools/overview.py`; photos remain compressed evidence images in `assets/overview/`. Scroll reveals and bar animations are in `app.js` and `styles.css`, with reduced-motion support. Gold, silver, and bronze medals mark the overall top three. The three highlighted models are explicitly selected; only the original Snapshot and Trajectory scores are displayed. No aggregate score is calculated. Results copy and native overview labels participate in the Chinese/English switch.
