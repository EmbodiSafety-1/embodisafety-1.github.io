'use strict';
history.scrollRestoration='manual';
if(location.hash)history.replaceState(null,'',location.pathname+location.search);
window.scrollTo({top:0,left:0,behavior:'instant'});
window.addEventListener('pageshow',()=>window.scrollTo({top:0,left:0,behavior:'instant'}),{once:true});
const nav=document.querySelector('#topnav');
const navToggle=document.querySelector('#navToggle');
const navLinks=[...document.querySelectorAll('.nav-links a')];
function closeMenu(){nav.classList.remove('open');navToggle.setAttribute('aria-expanded','false');navToggle.setAttribute('aria-label','Open menu');}
navToggle.addEventListener('click',()=>{const open=navToggle.getAttribute('aria-expanded')!=='true';nav.classList.toggle('open',open);navToggle.setAttribute('aria-expanded',String(open));navToggle.setAttribute('aria-label',open?'Close menu':'Open menu');});
navLinks.forEach(link=>link.addEventListener('click',closeMenu));
function updateNav(){nav.classList.toggle('scrolled',window.scrollY>70);}
window.addEventListener('scroll',updateNav,{passive:true});
updateNav();
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav.classList.contains('open')){closeMenu();navToggle.focus();}});
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
const hero=document.querySelector('.hero');
const heroVideo=document.querySelector('#heroVideo');
const heroPlay=document.querySelector('#heroPlay');
const chapters=JSON.parse(document.querySelector('#heroChapters').textContent);
const steps=[...document.querySelectorAll('.case-step')];
let heroPaused=reducedMotion.matches,heroVisible=true,currentChapter=-1;
function updateChapter(){
  const time=heroVideo.currentTime;
  const active=Math.max(0,chapters.findLastIndex(chapter=>time>=chapter.start));
  if(active!==currentChapter){
    currentChapter=active;heroVideo.style.objectPosition=`${chapters[active].focus}% center`;
    document.querySelector('#currentScene').textContent=`${String(active+1).padStart(2,'0')} / ${String(chapters.length).padStart(2,'0')}`;
    steps.forEach((step,index)=>{const selected=index===active;step.setAttribute('aria-pressed',String(selected));if(selected)step.setAttribute('aria-current','step');else step.removeAttribute('aria-current');});
  }
  steps.forEach((step,index)=>{const chapter=chapters[index];const progress=Math.min(1,Math.max(0,(time-chapter.start)/chapter.duration));step.querySelector('.case-progress i').style.width=`${progress*100}%`;});
}
function updateHeroButton(){heroPlay.textContent=heroPaused?'▷':'Ⅱ';heroPlay.setAttribute('aria-label',heroPaused?'Play background video':'Pause background video');heroPlay.setAttribute('aria-pressed',String(heroPaused));}
function playVideo(video){return video.play().catch(error=>{if(error.name==='AbortError'||error.name==='NotAllowedError')return;throw error;});}
function updateHero(){if(heroPaused||!heroVisible||document.hidden)heroVideo.pause();else playVideo(heroVideo);updateHeroButton();}
heroPlay.addEventListener('click',()=>{heroPaused=!heroPaused;updateHero();});
steps.forEach((step,index)=>step.addEventListener('click',()=>{heroVideo.currentTime=chapters[index].start;updateChapter();updateHero();}));
heroVideo.addEventListener('timeupdate',updateChapter);heroVideo.addEventListener('seeked',updateChapter);
new IntersectionObserver(entries=>{heroVisible=entries[0].isIntersecting;updateHero();},{threshold:.08}).observe(hero);
updateChapter();updateHero();

const demoCards=[...document.querySelectorAll('.demo-card')];
const demoVideos=demoCards.map(card=>card.querySelector('video'));
const visibleVideos=new Set();
const galleryMotion=document.querySelector('#galleryMotion');
let galleryPaused=reducedMotion.matches;
const userPausedVideos=new Set(),userPlayingVideos=new Set();
const programPauses=new WeakSet(),programPlays=new WeakSet();
function ensureSource(video){if(!video.getAttribute('src')){video.src=video.dataset.src;video.load();}}
function pauseDemo(video){if(!video.paused){programPauses.add(video);video.pause();}}
function playDemo(video){
  if(!video.paused)return;
  programPlays.add(video);
  video.play().catch(error=>{if(error.name==='NotAllowedError'){programPlays.delete(video);return;}if(error.name==='AbortError')return;throw error;});
}
function updateGallery(){
  demoVideos.forEach(video=>{const show=visibleVideos.has(video)&&!video.closest('.demo-card').hidden;
    if(!show||document.hidden||userPausedVideos.has(video)||(galleryPaused&&!userPlayingVideos.has(video)))pauseDemo(video);else{ensureSource(video);playDemo(video);}
  });
  galleryMotion.textContent=galleryPaused?'Play videos':'Pause videos';galleryMotion.setAttribute('aria-pressed',String(galleryPaused));
}
const demoObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){visibleVideos.add(entry.target);ensureSource(entry.target);}else visibleVideos.delete(entry.target);});updateGallery();},{threshold:.2});
demoVideos.forEach(video=>{
  video.addEventListener('pause',()=>{if(!programPauses.delete(video)){userPausedVideos.add(video);userPlayingVideos.delete(video);}});
  video.addEventListener('play',()=>{if(!programPlays.delete(video)){userPausedVideos.delete(video);userPlayingVideos.add(video);}});
  demoObserver.observe(video);
});
galleryMotion.addEventListener('click',()=>{galleryPaused=!galleryPaused;userPlayingVideos.clear();if(!galleryPaused)userPausedVideos.clear();updateGallery();});
document.querySelectorAll('.demo-filter').forEach(button=>button.addEventListener('click',()=>{
  const environment=button.dataset.environment;let count=0;
  demoCards.forEach(card=>{const show=environment==='all'||card.dataset.environment===environment;card.hidden=!show;if(show)count++;else pauseDemo(card.querySelector('video'));});
  document.querySelector('#demoGallery').classList.toggle('filtered',environment!=='all');
  document.querySelector('#demoCount').textContent=`${count} ${count===1?'example':'examples'}`;
  document.querySelectorAll('.demo-filter').forEach(control=>{const selected=control===button;control.classList.toggle('active',selected);control.setAttribute('aria-pressed',String(selected));});
  updateGallery();
}));
reducedMotion.addEventListener('change',event=>{heroPaused=event.matches;galleryPaused=event.matches;userPlayingVideos.clear();updateHero();updateGallery();});
document.addEventListener('visibilitychange',()=>{updateHero();updateGallery();});
const sectionObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting)navLinks.forEach(link=>{const active=link.hash===`#${entry.target.id}`;link.classList.toggle('active',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}),{rootMargin:'-12% 0px -65% 0px'});
document.querySelectorAll('main>section').forEach(section=>sectionObserver.observe(section));
// Reveal each block once as it enters the viewport.
const revealElements=[...document.querySelectorAll('.section-heading,.native-panel,.overview-text,.demo-card,.dataset-facts,.track,.environment-mixture,.score-highlights,.score-chart,.table-scroll,.podium-card,.leaderboard-scroll')];
if(!reducedMotion.matches){
 const revealObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');revealObserver.unobserve(entry.target);}});},{threshold:.08,rootMargin:'0px 0px -24px 0px'});
 revealElements.forEach((el,index)=>{el.classList.add('reveal');el.style.setProperty('--reveal-delay',`${el.classList.contains('demo-card')?(index%4)*65:0}ms`);revealObserver.observe(el);});
 document.documentElement.classList.add('motion-ready');
}
const modeExamples={
  "Proceed": [
    "Snapshot \u00b7 Trajectory",
    "The task is permissible and the available observations are sufficient to act. No visible hazard or execution failure requires a change of plan.",
    "Risk",
    "Risk identifies the hazard grounded in the observations. For a safe PROCEED decision, it can be reported as none."
  ],
  "Refuse": [
    "Snapshot \u00b7 Trajectory",
    "Completing the requested goal would cause harm or enable a prohibited outcome. The robot should decline the request rather than carry it out with a different technique.",
    "Next step",
    "Next step specifies the immediate safe action after the decision. For REFUSE, it should stop the harmful action and avoid enabling the requested outcome."
  ],
  "Clarify": [
    "Snapshot \u00b7 Trajectory",
    "A decision-critical detail is missing or ambiguous in the available observations. The robot should ask for that information before acting.",
    "Clarifying question",
    "Clarifying question states the specific information needed to resolve the ambiguity. It should target the missing detail so that execution can resume once it is answered."
  ],
  "Constrain": [
    "Snapshot \u00b7 Trajectory",
    "The goal is acceptable, but the current way of executing it creates a visible risk. The robot should preserve the goal while changing its actions to satisfy explicit safety constraints.",
    "Safety constraints",
    "Safety constraints specify the conditions that must hold for safe execution. They turn a general safety judgment into concrete limits on how the task is performed."
  ],
  "Recover": [
    "Trajectory",
    "The current attempt has failed to complete the task successfully. The robot should replan its actions and choose a feasible autonomous recovery strategy.",
    "Recoverability",
    "Recoverability describes whether the observed failure can be resolved through autonomous action. A recoverable failure supports selecting a new strategy and reassessing the result."
  ],
  "Escalate": [
    "Trajectory",
    "The task has encountered a failure that the robot cannot safely resolve on its own. It should stop autonomous attempts and request human assistance.",
    "Recoverability",
    "Recoverability describes whether autonomous recovery remains feasible after the failure. An unrecoverable situation calls for human intervention instead of further autonomous attempts."
  ]
};
function selectMode(button){const name=button.dataset.mode,detail=modeExamples[name];document.querySelectorAll('.mode-choice').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));document.querySelector('#modeDetailName').textContent=name;document.querySelector('#modeDetailTrack').textContent=detail[0];document.querySelector('#modeDetailScene').textContent=detail[1];document.querySelector('#modeDetailTerm').textContent=detail[2];document.querySelector('#modeDetailAction').textContent=detail[3];}
document.querySelectorAll('.mode-choice').forEach(button=>button.addEventListener('click',()=>selectMode(button)));
selectMode(document.querySelector('.mode-choice'));

const comingToast=document.createElement('div');comingToast.className='coming-toast';comingToast.setAttribute('role','status');document.body.append(comingToast);let toastTimer;
document.querySelectorAll('[data-coming]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();clearTimeout(toastTimer);comingToast.textContent=`${link.dataset.coming} is coming soon`;const box=link.getBoundingClientRect();comingToast.style.left=`${Math.max(12,Math.min(innerWidth-230,box.right-210))}px`;comingToast.style.top=`${Math.min(innerHeight-52,box.bottom+10)}px`;comingToast.classList.add('visible');toastTimer=setTimeout(()=>comingToast.classList.remove('visible'),2400);}));
