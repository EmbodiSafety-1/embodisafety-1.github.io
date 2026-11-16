from html import escape

def medal(rank):
    return f'<span class="award award-{rank}" aria-label="Rank {rank}"><svg viewBox="0 0 64 76" aria-hidden="true"><path d="M17 42L12 73l20-10 20 10-5-31" fill="currentColor" opacity=".4"/><circle cx="32" cy="29" r="26" fill="currentColor" opacity=".18"/><circle cx="32" cy="29" r="21" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="32" cy="29" r="17" fill="none" stroke="currentColor" stroke-width=".7" stroke-dasharray="1 3"/><text x="32" y="36" text-anchor="middle" fill="currentColor" font-family="Georgia,serif" font-weight="bold" font-size="23">{rank}</text></svg></span>'

def render_leaderboard(models):
    models=[r for r in models if r[2] is not None or r[3] is not None]
    leaders=['Claude-Opus-5.5','GPT-6-astra','GPT-5.5']
    ordered=[next(r for r in models if r[0]==name) for name in leaders]+[r for r in models if r[0] not in leaders]
    podium=''
    for rank,row in enumerate(ordered[:3],1):
        podium+=f'<article class="podium-card podium-{rank}">{medal(rank)}<h3>{escape(row[0])}</h3><div class="podium-scores"><span><small>Snapshot</small><b>{row[2]:.1f}%</b></span><span><small>Trajectory</small><b>{row[3]:.1f}%</b></span></div></article>'
    rows='';bars=''
    for row in ordered:
        rank=leaders.index(row[0])+1 if row[0] in leaders else None
        scores=['—' if v is None else f'{v:.1f}' for v in row[2:]]
        rows+=f'<tr><th scope="row"><span class="model-cell">{medal(rank) if rank else ""}<span>{escape(row[0])}</span></span></th><td>{scores[0]}</td><td>{scores[1]}</td></tr>'
        if row[2] is not None and row[3] is not None:
            bars+=f'<div class="result-bar-row"><strong>{escape(row[0])}</strong><div class="result-pair">'
            for value,track in zip(row[2:],['snapshot','trajectory']):bars+=f'<div class="mini-bar {track}"><i style="--value:{value}%"></i><span>{value:.1f}</span></div>'
            bars+='</div></div>'
    return f'<div class="podium">{podium}</div><div class="full-results-chart"><div class="chart-head"><span class="legend">Snapshot</span><span class="legend">Trajectory</span></div>{bars}<div class="mini-axis"><span>0</span><span>50</span><span>100%</span></div></div><div class="leaderboard-scroll"><table class="leaderboard"><thead><tr><th>Model</th><th>Snapshot</th><th>Trajectory</th></tr></thead><tbody>{rows}</tbody></table></div>'
