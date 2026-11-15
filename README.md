# EmbodiSafety

Academic project page for **EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI**.

Website: https://embodisafety-1.github.io/

## Preview locally

Run `python -m http.server 8000` in this directory, then open `http://localhost:8000`. The site is also viewable by opening `index.html` directly. No build or package installation is needed.

## Files

- `index.html`: research content and accessible markup.
- `styles.css`: white academic design, responsive desktop and mobile layouts.
- `app.js`: navigation, video playback, example filtering, results chart, figure enlargement.
- `assets/video-manifest.json`: the source-matched Figure 1 examples and reference decisions.
- `assets/videos/` and `assets/posters/`: compressed video clips and WebP covers.
- `assets/figures/`: cropped paper figures.
- `assets/EmbodiSafety_Benchmark.pdf`: the supplied manuscript.

## Deploy

GitHub Pages serves this repository from the root of `main`. Commit these files to `main` to publish. `.nojekyll` keeps the page buildless.

## Media

Only two videos were verified to match Figure 1 exactly. The remaining examples were omitted. Both clips are complete eight-second excerpts: 720×406, H.264, CRF 29, 24 fps, no audio, with MP4 faststart. Their combined size is 365,588 bytes (about 0.35 MiB).

The opening videos respect reduced-motion preferences, can be paused together, and pause when outside the viewport or when the page is hidden. The examples section loads videos on demand and permits only one example to play at a time. It reuses the same media URLs as the hero.

## Research content

All reported tasks, model results, response modes, and reference decisions are taken from the user-supplied manuscript. No author affiliations, venue acceptance, dataset downloads, or benchmark-code availability are inferred.

Page design inspired by https://xsparkai.com/Spark-0/. Research content, figures, and examples belong to the EmbodiSafety project.
