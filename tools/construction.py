from html import escape


def heading(letter, title):
    return f'<header><h3><span class="panel-letter">{letter}</span>{title}</h3></header>'


def detail():
    return '''<div class="process-detail">
      <strong class="detail-title"></strong><p class="detail-copy"></p>
      <div class="detail-progress" aria-hidden="true"><i></i></div>
    </div>'''


def render_construction():
    stages = [
        ('Scenario specification', 'Task · robot · viewpoint · hazard'),
        ('Script & video synthesis', 'Timed events → Seedance2.5'),
        ('Candidate sample', 'Instruction · frames · initial labels'),
    ]
    steps = ''.join(
        f'<button type="button" class="process-step"><span class="artifact-index" aria-hidden="true">0{i + 1}</span>'
        f'<strong>{title}</strong><small>{label}</small></button>'
        for i, (title, label) in enumerate(stages)
    )
    frames = ''.join(
        f'<button type="button" class="film-frame"><img src="assets/construction/pharmacy-f{index}.webp" '
        f'alt="" loading="lazy"><span><b>{time}</b> {label}</span></button>'
        for index, time, label in [
            (3, 't₀', 'Vials on tray'),
            (4, 't₁', 'Vials taken'),
            (5, 't₂', 'Empty tray'),
        ]
    )
    checks = ''.join(
        f'<tr><th scope="row"><button type="button" class="review-check">{title}</button></th>'
        f'<td>{evidence}</td><td>{criterion}</td></tr>'
        for title, evidence, criterion in [
            ('Visual grounding', 'Scene', 'Hazard is visible'),
            ('Temporal consistency', 'Frame order', 'Change is supported'),
            ('Label support', 'Mode prediction', 'Flag disagreement'),
            ('Action safety', 'Next action', 'Safe and feasible'),
        ]
    )
    experts = ''.join('<span class="expert-person" aria-hidden="true"></span>' for _ in range(5))
    return f'''<section class="construction section" id="construction" aria-labelledby="construction-title">
<div class="content-wrap">
  <div class="section-heading">
    <p class="section-kicker">03 / Data construction</p>
    <div class="construction-title-row">
      <h2 id="construction-title" data-zh="从场景设计到经核验的安全决策。">From designed scenarios to verified decisions.</h2>
      <button id="constructionMotion" class="construction-motion" type="button" aria-pressed="false">Pause motion</button>
    </div>
    <p class="section-description" data-zh="{escape('先生成并选取视觉证据，再由 AI 和五位博士级专家复核标注。')}">Generate and select visual evidence, then review annotations with AI and five PhD-level experts.</p>
  </div>
  <div class="construction-grid">
    <article class="process-panel generation-panel">
      {heading('a', 'Data generation')}
      <div class="generation-art" aria-hidden="true">
        <img src="assets/construction/generation-art.webp" alt="" loading="lazy" width="2172" height="724">
      </div>
      <div class="generation-flow" aria-label="Data generation stages">{steps}</div>
      {detail()}
    </article>
    <article class="process-panel selection-panel">
      {heading('b', 'From video to task evidence')}
      <div class="sample-tracks">
        <div class="sample-snapshot">
          <div class="sample-track"><strong>Snapshot</strong><small>One image</small></div>
          <div class="construction-frames">
            <button type="button" class="film-frame">
              <img src="assets/construction/scenario001-decision.webp" alt="A robot carries a steaming mug with a child ahead in the kitchen" loading="lazy">
              <span>Hot drink, child ahead</span>
            </button>
          </div>
          <div class="sample-instruction"><span>Instruction</span><strong>Take the cup to the dining table</strong></div>
        </div>
        <div class="sample-trajectory">
          <button type="button" class="sample-track"><strong>Trajectory</strong><small>3 ordered frames</small></button>
          <div class="construction-frames">{frames}</div>
          <div class="sample-instruction"><span>Instruction</span><strong>Open the fridge</strong></div>
        </div>
      </div>
      {detail()}
    </article>
    <article class="process-panel ai-panel">
      {heading('c', 'AI review')}
      <div class="review-input"><span>Evidence + instruction</span><span aria-hidden="true">→</span><strong>GPT-5.6 blind mode prediction</strong></div>
      <div class="review-table-wrap"><table class="review-table">
        <thead><tr><th scope="col">Check</th><th scope="col">Evidence</th><th scope="col">Criterion</th></tr></thead>
        <tbody>{checks}</tbody>
      </table></div>
      {detail()}
    </article>
    <article class="process-panel human-panel">
      {heading('d', 'Expert verification')}
      <div class="independent-review">
        <button type="button"><span class="expert-team" aria-hidden="true">{experts}</span><strong>5 PhD-level experts</strong></button>
        <button type="button"><span class="model-icon" aria-hidden="true">AI</span><strong>GPT-6-astra</strong></button>
      </div>
      <div class="review-merge" aria-hidden="true"></div>
      <div class="adjudication">Disagreement or both flag an error <span aria-hidden="true">→</span> Expert re-review</div>
      <div class="review-decisions">
        <button type="button"><span aria-hidden="true">✓</span><strong>Retain</strong><small>Evidence supports the label</small></button>
        <button type="button"><span aria-hidden="true">↻</span><strong>Revise</strong><small>Correct the annotation</small></button>
        <button type="button"><span aria-hidden="true">×</span><strong>Remove</strong><small>Evidence is insufficient</small></button>
      </div>
      {detail()}
    </article>
  </div>
</div></section>'''
