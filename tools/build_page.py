from pathlib import Path
from html import escape
import json
from overview import render_overview
from leaderboard import render_leaderboard
from overview_text import PARAGRAPHS
from construction import render_construction

root=Path(__file__).resolve().parents[1]
chapters=json.loads((root/'assets/hero-chapters.json').read_text(encoding='utf-8'))
demos=json.loads((root/'assets/demos/manifest.json').read_text(encoding='utf-8'))
facts=json.loads((Path(__file__).with_name('benchmark-results.json')).read_text(encoding='utf-8'))
dataset=json.loads((root/'assets/overview-dataset.json').read_text(encoding='utf-8'))
models=[r for r in facts['results']['rows'] if r[1]!='Adapted']
scored=[r for r in models if r[2] is not None]
best=max(scored,key=lambda r:r[2])
weakest=min(scored,key=lambda r:(r[2]+r[3])/2)
overview_values={'tasks':f'{dataset["tasks"]:,}','scenarios':f'{dataset["scenarios"]:,}','snapshot':f'{dataset["snapshot"]:,}','trajectory':f'{dataset["trajectory"]:,}','best_model':best[0],'best_snapshot':f'{best[2]:.1f}%','best_trajectory':f'{best[3]:.1f}%','low_snapshot':f'{weakest[2]:.1f}%','low_trajectory':f'{weakest[3]:.1f}%'}
assert dataset['tasks']+0==1632 and dataset['snapshot']+dataset['trajectory']==dataset['tasks']
def overview_paragraphs():
    markup=''
    for en,zh in PARAGRAPHS:
        holder={}
        for lang,text in (('en',en),('zh',zh)):
            for tag in ('strong','em'):
                text=text.replace('{'+tag+'}','<'+tag+'>' if tag=='strong' else '').replace('{/'+tag+'}','</'+tag+'>' if tag=='strong' else '')
            holder[lang]=text.format(**overview_values)
        markup+=f'<p data-zh="{escape(holder["zh"])}">{holder["en"]}</p>'
    return markup
assert len(demos)==32
cards=[]
for i,d in enumerate(demos):
    zh_title=f' data-zh="{escape(d["titleZh"])}"'
    zh_instruction=f' data-zh="{escape(d["instructionZh"])}"'
    cards.append(f'''<article class="demo-card" data-environment="{escape(d['environment'])}"><div class="demo-media"><button class="demo-open" type="button" aria-label="Open example {i+1}: {escape(d['title'])}"><span aria-hidden="true">↗</span></button><video muted loop playsinline preload="none" data-src="{escape(d['src'])}" poster="{escape(d['poster'])}" aria-label="Example {i+1}: {escape(d['title'])}"></video></div><div class="demo-caption"><span class="demo-index">{i+1:02d}</span><div><h3{zh_title}>{escape(d['title'])}</h3><p{zh_instruction}>{escape(d['instruction'])}</p></div><span class="demo-environment">{escape(d['environment'])}</span></div></article>''')
filters=['<button class="demo-filter active" data-environment="all" aria-pressed="true">All <span>'+str(len(demos))+'</span></button>']
for env in ['Home','Kitchen','Office','Hospital','Industry','Laboratory','Public']:
    n=sum(d['environment']==env for d in demos)
    if n: filters.append(f'<button class="demo-filter" data-environment="{env}" aria-pressed="false">{env} <span>{n}</span></button>')
envs=[('Industrial workspace',20.8,'#247f73'),('Office',16.9,'#83a48b'),('Home',12.6,'#57aa9b'),('Kitchen',9.9,'#a5c2ab'),('Shopping mall',9.9,'#6d9980'),('Hospital',9.6,'#adcfc4'),('Warehouse',8.8,'#78948d'),('Laboratory',7.7,'#bdc9bb'),('Public space',1.5,'#91ad7b'),('Outdoor',1.2,'#8fa477'),('Other',1.1,'#d5e0da')]
envbar=''.join(f'<span style="width:{v}%;background:{color}" title="{label}: {v}%"></span>' for label,v,color in envs)
envkey=''.join(f'<span><i style="background:{color}"></i>{label}<b>{v}%</b></span>' for label,v,color in envs)
timeline=''.join(f'<button class="case-step" data-clip="{i}" aria-label="Play example {i+1:02d}" aria-pressed="{"true" if i==0 else "false"}"><span class="case-number">{i+1:02d}</span><span class="case-progress"><i></i></span></button>' for i in range(len(chapters)))

html='''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#147d73"><title>EmbodiSafety: Risk Understanding and Response in Embodied AI</title>
<meta name="description" content="Explore EmbodiSafety through DEMO_TOTAL visual demonstrations, a dataset of 1,632 safety decisions, and model evaluations across Snapshot and Trajectory tracks."><meta property="og:type" content="website"><meta property="og:title" content="EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI"><meta property="og:description" content="A visual benchmark for embodied safety: 1,632 tasks, 844 scenarios, and six response modes."><meta property="og:url" content="https://embodisafety-1.github.io/"><meta property="og:image" content="https://embodisafety-1.github.io/assets/figures/web-overview.webp"><meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="https://embodisafety-1.github.io/"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script><script src="i18n.js" defer></script></head>
<body><a class="skip-link" href="#overview">Skip to overview</a><nav class="topnav" id="topnav" aria-label="Main navigation"><div class="nav-inner"><a href="#top" class="brand">EmbodiSafety<span class="brand-mark" aria-hidden="true">/</span></a><div class="nav-links" id="navLinks"><a href="#overview">Overview</a><a href="#demos">Dataset & demos</a><a href="#construction">Construction</a><a href="#results">Results</a></div><div class="nav-actions"><button class="language-toggle" id="languageToggle" type="button" aria-label="Switch language">中文 / English</button><a class="nav-paper" href="#" data-coming="Paper">Paper ↗</a><a class="nav-github" href="#" data-coming="GitHub">GitHub ↗</a></div><button id="navToggle" class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span></button></div></nav>
<main><header class="hero" id="top"><video id="heroVideo" class="hero-video" muted loop playsinline preload="auto" poster="assets/posters/refuse-pharmacy-theft.webp" aria-label="Selected EmbodiSafety examples played continuously"><source src="assets/videos/hero-examples.mp4" type="video/mp4"></video><div class="hero-shade"></div><div class="hero-head"><p class="hero-kicker">Embodied AI safety benchmark</p><h1><span class="h1-name">EmbodiSafety</span><span class="h1-title">Benchmarking Risk Understanding<br>and Response in Embodied AI</span></h1><p class="subtitle">A visual benchmark for understanding risk and choosing safe responses.</p></div><div class="hero-footer"><div class="hero-example-nav"><span class="sequence-count" id="currentScene">01 / HERO_COUNT</span><div class="case-timeline" role="group" aria-label="Example sequence">CASE_TIMELINE</div><button id="heroPlay" type="button" aria-label="Pause background video" aria-pressed="false">Ⅱ</button></div></div></header>

<section class="overview section" id="overview" aria-labelledby="overview-title"><div class="content-wrap"><div class="section-heading"><p class="section-kicker">01 / Overview</p><h2 id="overview-title">EmbodiSafety in one view.</h2></div>NATIVE_OVERVIEW<div class="overview-text">OVERVIEW_TEXT</div></div></section>

<section class="demos section" id="demos" aria-labelledby="demos-title"><div class="wide-wrap"><div class="section-heading dataset-heading"><p class="section-kicker">02 / Dataset video examples</p><h2 id="demos-title" data-zh="EmbodiSafety：1,632个具身安全决策任务。">EmbodiSafety: 1,632 embodied safety decisions.</h2></div><div class="dataset-showcase"><div class="dataset-intro"><p data-zh="具身智能体需要识别风险，并决定下一步如何行动。EmbodiSafety 包含来自&lt;strong&gt;844个视觉场景&lt;/strong&gt;的&lt;strong&gt;1,632个决策任务&lt;/strong&gt;，覆盖家庭、办公、医疗和工业等环境。&lt;strong&gt;Snapshot&lt;/strong&gt; 任务使用单张图像，&lt;strong&gt;Trajectory&lt;/strong&gt; 任务使用2–8帧有序图像；六种响应模式涵盖安全执行、拒绝、澄清、约束执行、恢复和请求人工介入。">Embodied agents need to recognize risk and decide what to do next. EmbodiSafety pairs <strong>1,632 decision tasks</strong> with <strong>844 visual scenarios</strong> across homes, offices, hospitals, and industrial settings. <strong>Snapshot</strong> tasks use one image; <strong>Trajectory</strong> tasks use 2–8 ordered frames. Six response modes cover proceeding, refusing, clarifying, constrained execution, recovery, and human escalation.</p><div class="showcase-facts"><dl><dd>1,632</dd><dt>Decision tasks</dt></dl><dl><dd>844</dd><dt>Visual scenarios</dt></dl><dl><dd>1,092</dd><dt>Snapshot data</dt></dl><dl><dd>540</dd><dt>Trajectory data</dt></dl></div></div><div class="dataset-media"><div class="demo-gallery" id="demoGallery">DEMO_CARDS</div><div class="mosaic-footer"><p class="mosaic-note" data-zh="不同物体、场景与风险变化中的32个视频示例。">32 examples across diverse objects, environments, and changing risks.</p><button class="gallery-motion" id="galleryMotion" aria-pressed="false">Pause videos</button></div><div class="demo-toolbar"><div class="demo-filters" role="group" aria-label="Filter demonstrations by environment">DEMO_FILTERS</div><span id="demoCount" aria-live="polite">DEMO_TOTAL examples</span></div></div></div><div class="environment-mixture"><h3>Scenario environments</h3><div class="environment-bar" role="img" aria-label="Environment distribution: industrial workspace 20.8%, office 16.9%, home 12.6%, kitchen 9.9%, shopping mall 9.9%, hospital 9.6%, warehouse 8.8%, laboratory 7.7%, public space 1.5%, outdoor 1.2%, other 1.1%.">ENV_BAR</div><div class="environment-key">ENV_KEY</div></div><div class="track-pair"><article class="track" data-track="snapshot"><header><h3>Snapshot</h3><span>1,092 tasks · 1 image</span></header><p>The model judges the current scene: whether a task is safe, harmful, underspecified, or admissible under explicit constraints. Four response modes cover proceeding, refusing, asking for clarification, and constrained execution.</p></article><article class="track" data-track="trajectory"><header><h3>Trajectory</h3><span>540 tasks · 2–8 frames</span></header><p>Ordered observations reveal how risks develop during execution. This track includes all six response modes, adding autonomous recovery and human escalation when a task encounters failure.</p></article></div></div></section>

CONSTRUCTION_SECTION
<section class="results section" id="results" aria-labelledby="results-title"><div class="content-wrap"><div class="section-heading"><p class="section-kicker">04 / Benchmark results</p><h2 id="results-title">Complete-decision accuracy.</h2><p class="section-description">The strongest evaluated model, Claude-Opus-5.5, reaches 56.1% on Snapshot and 61.5% on Trajectory.</p></div>NATIVE_LEADERBOARD</div></section>

</main><dialog class="demo-dialog" id="demoDialog" aria-labelledby="demoDialogTitle"><button type="button" class="demo-dialog-close" aria-label="Close video">×</button><video controls playsinline muted></video><div class="demo-dialog-copy"><h3 id="demoDialogTitle"></h3><p></p></div></dialog>
<footer class="site-footer"><div class="content-wrap"><div class="footer-links"><a href="#" data-coming="Paper">Paper ↗</a><a href="#" data-coming="GitHub">GitHub ↗</a><a href="#top">Top ↑</a></div></div></footer><script id="heroChapters" type="application/json">HERO_CHAPTERS</script></body></html>'''
for token,value in [('CONSTRUCTION_SECTION',render_construction()),('NATIVE_LEADERBOARD',render_leaderboard(models)),('NATIVE_OVERVIEW',render_overview(models)),('DEMO_TOTAL',str(len(demos))),('CASE_TIMELINE',timeline),('HERO_COUNT',f'{len(chapters):02d}'),('DEMO_FILTERS',''.join(filters)),('DEMO_CARDS','\n'.join(cards)),('ENV_BAR',envbar),('ENV_KEY',envkey),('HERO_CHAPTERS',json.dumps(chapters).replace('<','\\u003c')),('OVERVIEW_TEXT',overview_paragraphs())]:
    html=html.replace(token,value)
(root/'index.html').write_text(html,encoding='utf-8')
print('Page built:',len(demos),'demos;',len(chapters),'hero scenes;',len(models),'evaluated models.')
