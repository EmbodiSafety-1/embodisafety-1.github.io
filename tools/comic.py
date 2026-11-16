def robot():
    return '''<g stroke="#47685f" stroke-width="2.5" stroke-linejoin="round"><ellipse cx="92" cy="175" rx="55" ry="8" fill="#dfeae5" stroke="none"/><path d="M64 118 Q48 120 43 145 M120 118 Q142 120 145 141" fill="none" stroke-width="13"/><path d="M68 151 L64 170 H81 L85 151 M102 151 L108 170 H125 L120 149" fill="#dbe6df"/><rect x="61" y="104" width="64" height="51" rx="22" fill="#f5f8f1"/><path d="M87 121 l9 -5 9 5 -2 13 -7 6 -7 -6z" fill="#9cc9b6"/><path d="M90 127 l5 5 7 -9" fill="none"/><rect x="46" y="39" width="94" height="69" rx="32" fill="#f6f8f1"/><ellipse cx="45" cy="75" rx="9" ry="16" fill="#a7cbbd"/><ellipse cx="141" cy="75" rx="9" ry="16" fill="#a7cbbd"/><rect x="59" y="55" width="69" height="37" rx="18" fill="#405d58"/><ellipse cx="79" cy="72" rx="5" ry="8" fill="#e8f5e9" stroke="none"/><ellipse cx="110" cy="72" rx="5" ry="8" fill="#e8f5e9" stroke="none"/><path d="M93 39 v-12"/><circle cx="93" cy="23" r="6" fill="#a7cbbd"/></g>'''


def scene(x, y, wet=False):
    puddle = '<ellipse cx="40" cy="55" rx="25" ry="6" fill="#88baa8"/><path d="M24 55h18m3 0h10" stroke="#fff"/>' if wet else ''
    return f'''<g transform="translate({x} {y})"><rect width="96" height="75" rx="8" fill="#fff" stroke="#b5ccc0" stroke-width="2"/><path d="M8 61h80M18 52V15h53v37M28 52V25h33v27" fill="#eef4ed" stroke="#849f91" stroke-width="2"/>{puddle}</g>'''


def render_comic():
    panels = []
    for temporal in (False, True):
        title = 'Trajectory' if temporal else 'Snapshot'
        frames = ''.join(scene(18+i*105, 18, temporal and i>0) for i in range(3)) if temporal else scene(123, 18, True)
        labels = '<text x="66" y="110">t₁</text><text x="171" y="110">t₂</text><text x="276" y="110">t₃</text>' if temporal else '<text x="171" y="110">One observation</text>'
        panels.append(f'''<article class="comic-panel"><header><span>0{2 if temporal else 1}</span><h4>{title}</h4><p>{'Follow how the scene changes' if temporal else 'Read the current scene'}</p></header><svg viewBox="0 0 342 345" role="img" aria-label="{title}: visual evidence, robot reasoning, safe decision">{frames}<g fill="#667f74" font-size="12" text-anchor="middle">{labels}</g><path class="comic-signal" d="M171 118v32" stroke="#589781" stroke-width="3" stroke-dasharray="5 5"/><g transform="translate(76 146) scale(.85)">{robot()}</g><g transform="translate(224 194)"><rect width="105" height="62" rx="16" fill="#e6f1e9"/><text x="52" y="25" text-anchor="middle" fill="#285f49" font-size="12" font-weight="600">{'Track the risk' if temporal else 'Spot the risk'}</text><text x="52" y="44" text-anchor="middle" fill="#547b68" font-size="11">{'across time' if temporal else 'in this frame'}</text></g><path d="M171 308v17m-5 -5 5 5 5 -5" stroke="#589781" stroke-width="2" fill="none"/></svg><div class="comic-decision"><b>{'Adapt to new evidence' if temporal else 'Choose a safe response'}</b><p>{'A changing scene can call for recovery or human assistance.' if temporal else 'Ground the response in what is visible, and ask when information is missing.'}</p></div></article>''')
    return '<div class="dataset-comic" lang="en">'+''.join(panels)+'</div>'
