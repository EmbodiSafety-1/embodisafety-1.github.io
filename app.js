'use strict';
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const nav = document.querySelector('.topnav');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav-links a');
function closeNav() {
  nav.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  navToggle.setAttribute('aria-label', 'Open navigation');
}
navToggle.addEventListener('click', () => {
  const open = navToggle.getAttribute('aria-expanded') !== 'true';
  navToggle.setAttribute('aria-expanded', String(open));
  navToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  nav.classList.toggle('open', open);
});
navLinks.forEach(link => link.addEventListener('click', closeNav));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav.classList.contains('open')) { closeNav(); navToggle.focus(); }
});
const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) navLinks.forEach(link => {
      const active = link.hash === `#${entry.target.id}`;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  });
}, { rootMargin: '-15% 0px -65% 0px' });
document.querySelectorAll('main > section').forEach(section => sectionObserver.observe(section));

const heroVideos = [...document.querySelectorAll('.hero-tile video')];
const motionToggle = document.querySelector('#motionToggle');
let motionPaused = reducedMotion.matches;
let heroVisible = true;
function updateHeroPlayback() {
  heroVideos.forEach(video => {
    if (motionPaused || !heroVisible || document.hidden) video.pause();
    else video.play().catch(error => {
      if (error.name === 'AbortError') return;
      motionPaused = true;
      heroVideos.forEach(clip => clip.pause());
      motionToggle.textContent = '▷ Play videos';
      motionToggle.setAttribute('aria-pressed', 'true');
    });
  });
  motionToggle.textContent = motionPaused ? '▷ Play videos' : 'Ⅱ Pause videos';
  motionToggle.setAttribute('aria-pressed', String(motionPaused));
}
motionToggle.addEventListener('click', () => { motionPaused = !motionPaused; updateHeroPlayback(); });
reducedMotion.addEventListener('change', event => { motionPaused = event.matches; updateHeroPlayback(); });
new IntersectionObserver(entries => {
  heroVisible = entries[0].isIntersecting; updateHeroPlayback();
}, { threshold: 0.05 }).observe(document.querySelector('.hero-visual'));
document.addEventListener('visibilitychange', updateHeroPlayback);

const demoCards = [...document.querySelectorAll('.demo-card')];
const count = document.querySelector('#demoCount');
function setFilter(filter) {
  let visible = 0;
  demoCards.forEach(card => {
    const show = filter === 'all' || card.dataset.mode === filter;
    card.hidden = !show;
    if (show) visible++; else card.querySelector('video').pause();
  });
  count.textContent = `${visible} ${visible === 1 ? 'example' : 'examples'}`;
  document.querySelectorAll('.filter-button').forEach(button => {
    const selected = button.dataset.filter === filter;
    button.classList.toggle('active', selected);
    button.setAttribute('aria-pressed', String(selected));
  });
}
document.querySelectorAll('.filter-button').forEach(button => button.addEventListener('click', () => setFilter(button.dataset.filter)));
setFilter('all');
demoCards.forEach(card => {
  const video = card.querySelector('video');
  video.addEventListener('play', () => demoCards.forEach(other => { if (other !== card) other.querySelector('video').pause(); }));
});
const demoObserver = new IntersectionObserver(entries => entries.forEach(entry => {
  if (!entry.isIntersecting) entry.target.pause();
}), { threshold: 0.05 });
demoCards.forEach(card => demoObserver.observe(card.querySelector('video')));

const models = [
 ['Claude-Opus-5.5',56.1,61.5],['GPT-6-astra',55.8,57.2],['GPT-5.6-sol',50.3,57.4],['Gemini-3.8-Flash',51.5,52.8],['Qwen3.5-35B-A3B',24.1,26.9],['HomeGuard-8B',25.7,20.4],['Qwen3.5-4B',37.3,13.1],['Qwen3.5-2B',20.8,7.6],['EmbodiSafety-4B',52.2,27.4,true],['EmbodiSafety-2B',44.6,24.6,true]
];
function renderChart(track) {
  const index = track === 'snapshot' ? 1 : 2;
  const chart = document.querySelector('#resultsChart');
  chart.replaceChildren();
  const sorted = [...models].sort((a,b) => b[index]-a[index]);
  sorted.forEach(model => {
    const row = document.createElement('div'); row.className = `chart-row${model[3] ? ' adapted' : ''}`;
    const label = document.createElement('span'); label.className = 'chart-model'; label.textContent = model[0];
    const value = document.createElement('div'); value.className = 'chart-values';
    const line = document.createElement('div'); line.className = 'bar-line';
    const bar = document.createElement('span'); bar.className = 'bar'; bar.style.width = `${model[index]}%`;
    const number = document.createElement('span'); number.className = 'bar-number'; number.textContent = model[index].toFixed(1);
    line.append(bar,number); value.append(line); row.append(label,value); chart.append(row);
  });
  chart.setAttribute('aria-label', `${track === 'snapshot' ? 'Snapshot' : 'Trajectory'} complete-decision accuracy (%): ${sorted.map(m => `${m[0]} ${m[index]}`).join('; ')}`);
  document.querySelectorAll('.metric-button').forEach(button => {
    const active = button.dataset.track === track; button.classList.toggle('active',active); button.setAttribute('aria-pressed',String(active));
  });
}
document.querySelectorAll('.metric-button').forEach(button => button.addEventListener('click', () => renderChart(button.dataset.track)));
renderChart('snapshot');

const figureDialog = document.querySelector('#figureDialog');
let figureTrigger;
document.querySelectorAll('.figure-button').forEach(button => button.addEventListener('click', () => {
  figureTrigger = button;
  const source = button.querySelector('img'); const enlarged = figureDialog.querySelector('img'); enlarged.src = source.src; enlarged.alt = source.alt; figureDialog.showModal();
}));
document.querySelector('.dialog-close').addEventListener('click', () => figureDialog.close());
figureDialog.addEventListener('click', event => { if (event.target === figureDialog) figureDialog.close(); });
figureDialog.addEventListener('close', () => figureTrigger?.focus());
