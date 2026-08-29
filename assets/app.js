/* Growx Tech IT, shared behaviour. No libraries; every effect is transform/opacity only. */
(function(){
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero "Career Ascent" field (home page only) — a field of small "candidate"
  // nodes drifting slowly upward, a few larger glowing "placement" nodes that
  // breathe, warm connecting lines between them, and the occasional bright
  // pulse travelling along a connection — a live, ambient nod to candidates
  // rising toward placements via Growx's AI-matched network, not a copy of
  // any reference art, built from the site's own cyan/violet/gold palette.
  var c = document.getElementById('net');
  if(c){
    var ctx = c.getContext('2d');
    var pts = [], pulses = [], W, H;
    function size(){
      var r = c.parentElement.getBoundingClientRect();
      W = c.width = r.width; H = c.height = r.height;
    }
    size(); addEventListener('resize', size);
    var N = Math.min(85, Math.floor(W/13));
    var LINK_D2 = 19000;
    for(var i=0;i<N;i++){
      var milestone = Math.random() < 0.14;
      pts.push({
        x: Math.random()*W, y: Math.random()*H,
        vx: (Math.random()-.5)*.22,
        vy: -.10 - Math.random()*.24,
        r: milestone ? 2.6+Math.random()*1.2 : 1+Math.random()*.9,
        milestone: milestone,
        phase: Math.random()*Math.PI*2
      });
    }
    var running = true, t = 0;
    new IntersectionObserver(function(e){
      running = e[0].isIntersecting;
      if(running && !reduced) requestAnimationFrame(frame);
    }).observe(c);

    function maybeSpawnPulse(edges){
      if(reduced || edges.length === 0 || pulses.length >= 4 || Math.random() > .02) return;
      var e = edges[Math.floor(Math.random()*edges.length)];
      pulses.push({p: e.p, q: e.q, t: 0});
    }

    function frame(){
      ctx.clearRect(0,0,W,H);
      t += 1;
      var edges = [];
      for(var i=0;i<pts.length;i++){
        var p=pts[i];
        if(!reduced){
          p.x+=p.vx; p.y+=p.vy;
          if(p.y < -12){ p.y = H+12; p.x = Math.random()*W; }
        }
        if(p.x<-12) p.x = W+12; else if(p.x>W+12) p.x = -12;

        var glow = p.milestone ? (.7 + .3*Math.sin(t*.02 + p.phase)) : 1;
        ctx.beginPath(); ctx.arc(p.x,p.y,p.r*glow,0,7);
        ctx.fillStyle = p.milestone ? 'rgba(245,195,107,'+(.55*glow)+')' : 'rgba(79,216,255,.55)';
        ctx.fill();
        if(p.milestone){
          ctx.beginPath(); ctx.arc(p.x,p.y,p.r*glow*2.6,0,7);
          ctx.fillStyle = 'rgba(245,195,107,'+(.10*glow)+')';
          ctx.fill();
        }

        for(var j=i+1;j<pts.length;j++){
          var q=pts[j], dx=p.x-q.x, dy=p.y-q.y, d=dx*dx+dy*dy;
          if(d<LINK_D2){
            var warm = p.milestone || q.milestone;
            var a = (warm ? .22 : .13) * (1-d/LINK_D2);
            ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y);
            ctx.strokeStyle = warm ? 'rgba(243,159,27,'+a+')' : 'rgba(139,124,255,'+a+')';
            ctx.lineWidth = warm ? 1.1 : 1;
            ctx.stroke();
            edges.push({p:p, q:q});
          }
        }
      }

      maybeSpawnPulse(edges);
      for(var k=pulses.length-1; k>=0; k--){
        var pu = pulses[k];
        pu.t += .035;
        if(pu.t >= 1){ pulses.splice(k,1); continue; }
        var x = pu.p.x + (pu.q.x-pu.p.x)*pu.t, y = pu.p.y + (pu.q.y-pu.p.y)*pu.t;
        var fade = Math.sin(pu.t*Math.PI);
        ctx.beginPath(); ctx.arc(x,y,2,0,7);
        ctx.fillStyle = 'rgba(255,255,255,'+(.85*fade)+')';
        ctx.fill();
        ctx.beginPath(); ctx.arc(x,y,4.5,0,7);
        ctx.fillStyle = 'rgba(79,216,255,'+(.35*fade)+')';
        ctx.fill();
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
