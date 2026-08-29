/* Growx Tech IT, shared behaviour. No libraries; every effect is transform/opacity only. */
(function(){
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero neural-network field (home page only)
  var c = document.getElementById('net');
  if(c){
    var ctx = c.getContext('2d');
    var pts = [], W, H;
    function size(){
      var r = c.parentElement.getBoundingClientRect();
      W = c.width = r.width; H = c.height = r.height;
    }
    size(); addEventListener('resize', size);
    var N = Math.min(60, Math.floor(W/20));
    for(var i=0;i<N;i++){
      pts.push({x:Math.random()*W, y:Math.random()*H, vx:(Math.random()-.5)*.35, vy:(Math.random()-.5)*.35});
    }
    var running = true;
    new IntersectionObserver(function(e){
      running = e[0].isIntersecting;
      if(running && !reduced) requestAnimationFrame(frame);
    }).observe(c);
    function frame(){
      ctx.clearRect(0,0,W,H);
      for(var i=0;i<pts.length;i++){
        var p=pts[i];
        if(!reduced){ p.x+=p.vx; p.y+=p.vy; }
        if(p.x<0||p.x>W)p.vx*=-1;
        if(p.y<0||p.y>H)p.vy*=-1;
        ctx.beginPath(); ctx.arc(p.x,p.y,1.5,0,7);
        ctx.fillStyle='rgba(79,216,255,.6)'; ctx.fill();
        for(var j=i+1;j<pts.length;j++){
          var q=pts[j], dx=p.x-q.x, dy=p.y-q.y, d=dx*dx+dy*dy;
          if(d<15000){
            ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y);
            ctx.strokeStyle='rgba(139,124,255,'+(0.14*(1-d/15000))+')';
            ctx.lineWidth=1; ctx.stroke();
          }
        }
      }
      if(running && !reduced) requestAnimationFrame(frame);
    }
    frame();
  }

  // Scroll reveals
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, {threshold:.12});
  document.querySelectorAll('.sr:not(.in)').forEach(function(el){ io.observe(el); });

  // Counters
  document.querySelectorAll('[data-count]').forEach(function(el){
    var target = +el.getAttribute('data-count');
    if(reduced){ el.textContent = target + '+'; return; }
    var start = null;
    function step(t){
      if(!start) start=t;
      var p = Math.min((t-start)/1400, 1);
      el.textContent = Math.floor(target * (1-Math.pow(1-p,3))) + (p===1 ? '+' : '');
      if(p<1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });

  // Cursor spotlight on cards
  if(!matchMedia('(hover:none)').matches){
    document.querySelectorAll('.jstep').forEach(function(card){
      card.addEventListener('pointermove', function(e){
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  // Mobile menu
  var tog = document.getElementById('navToggle'), menu = document.getElementById('navmenu');
  if(tog && menu){
    tog.addEventListener('click', function(){
      var open = document.body.classList.toggle('nav-open');
      tog.setAttribute('aria-expanded', open ? 'true' : 'false');
      tog.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    menu.addEventListener('click', function(e){
      if(e.target.tagName === 'A'){
        document.body.classList.remove('nav-open');
        tog.setAttribute('aria-expanded','false');
      }
    });
    addEventListener('keydown', function(e){
      if(e.key === 'Escape' && document.body.classList.contains('nav-open')){
        document.body.classList.remove('nav-open');
        tog.setAttribute('aria-expanded','false');
      }
    });
  }

  // Employer marquee, shuffled every load, never two of the same industry side by side
  var mq = document.getElementById('coMarquee');
  if(mq){
    var BY_INDUSTRY = {
      it:        ['Microsoft','Google','Amazon','Oracle','IBM','Salesforce','Adobe','Cisco','Intel','NVIDIA','Dell Technologies','ServiceNow'],
      health:    ['UnitedHealth Group','CVS Health','HCA Healthcare','Pfizer','Johnson & Johnson','Kaiser Permanente','Cigna','Abbott'],
      finance:   ['JPMorgan Chase','Bank of America','Goldman Sachs','Wells Fargo','Citi','American Express','Capital One','Fidelity'],
      engineer:  ['Boeing','Lockheed Martin','General Electric','Honeywell','Caterpillar','Raytheon','Tesla','3M'],
      retail:    ['Walmart','Target','Costco','The Home Depot','Nike','Starbucks','Lowe’s','Best Buy'],
      logistics: ['UPS','FedEx','Union Pacific','C.H. Robinson','XPO','Ryder'],
      consult:   ['Deloitte','PwC','EY','KPMG','Accenture','Booz Allen Hamilton'],
      hospitality:['Marriott International','Hilton','Delta Air Lines','United Airlines','Hyatt'],
      realestate:['Turner Construction','AECOM','Jacobs','CBRE','Bechtel'],
      education: ['Pearson','Chegg','2U','Grand Canyon Education'],
      energy:    ['ExxonMobil','Chevron','NextEra Energy','Duke Energy']
    };

    function shuffle(a){
      for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; }
      return a;
    }

    // pick a few from each industry, then interleave so industries never clump
    var buckets = [];
    Object.keys(BY_INDUSTRY).forEach(function(k){
      buckets.push({ k:k, list: shuffle(BY_INDUSTRY[k].slice()).slice(0,3) });
    });
    shuffle(buckets);
    var out = [], added = true, round = 0;
    while(added){
      added = false;
      for(var b=0;b<buckets.length;b++){
        if(buckets[b].list[round]){ out.push(buckets[b].list[round]); added = true; }
      }
      round++;
    }

    var html = out.map(function(n){
      return '<span>'+n.replace(/&/g,'&amp;')+'</span><span class="sep">◆</span>';
    }).join('');
    mq.querySelectorAll('.marquee-set').forEach(function(set){ set.innerHTML = html; });
    mq.style.setProperty('--mq-dur', Math.max(38, out.length * 2.1) + 's');
  }
})();
