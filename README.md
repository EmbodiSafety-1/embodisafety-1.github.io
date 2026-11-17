# EmbodiSafety project page

Local mirror of the project page for **EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI**. The published copy is served by GitHub Pages from the root of `main` in `EmbodiSafety-1/embodisafety-1.github.io` at <https://embodisafety-1.github.io/>; this directory is the working source for the next revision.

## Preview

Open `index.html` directly, or run `python preview.py` and visit `http://127.0.0.1:8766/`. The preview server supports byte-range requests for video timeline navigation. No dependencies or build step are required.

## Content

The page has three sections: Overview, Dataset video examples, and Results. It includes 32 playable demonstrations, dataset coverage, and complete-decision accuracy for the 15 models with reported L3 scores. The overall top three remain highlighted without calculating a combined score. The overview diagrams use native HTML; evidence photographs remain compressed images.

## Video cover

The cover is a single 24.125-second H.264 MP4, 1280×720 at 24 fps, without audio, with faststart. Its size is 1,851,376 bytes. Three complete clips play continuously and loop in this order:

1. Medication theft.
2. Wet tray near electronics.
3. Passport destruction.

The cover controls show sequence numbers only. Media source paths and verification notes stay outside the website in the task's research directory.

`assets/hero-chapters.json` records chapter timing and image focus. The same data is embedded in the page so it also works when opened directly from disk. The timeline seeks within one video; it does not reload individual clips. Playback pauses when the cover is outside the viewport or the tab is hidden, and respects reduced-motion preferences.

## Demonstrations and visual design

The gallery contains 32 distinct scenarios across seven environments, including the 12 newly selected samples. The merged dataset chapter pairs an introduction and four statistics on the left with an eight-column, 32-video mosaic on the right. Selecting a tile opens the full video and bilingual caption. Only visible videos load and play. Each video has a sequence number, title, instruction, and environment. English and Chinese captions are supported. The Dataset section uses text and environment distributions without the former robot illustrations. Results place the compact model table on the left and green paired bars on the right beneath the three highlighted models; phones stack these panels.

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

The overview is rendered as native HTML by `tools/overview.py`; photos remain compressed evidence images in `assets/overview/`. Scroll reveals and bar animations are in `app.js` and `styles.css`, with reduced-motion support. Gold, silver, and bronze medals mark the overall top three. The three highlighted models are explicitly selected; only the original Snapshot and Trajectory scores are displayed. No aggregate score is calculated. Page copy participates in the Chinese/English switch. Native overview figure labels remain English.
