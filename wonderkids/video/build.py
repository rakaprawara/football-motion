#!/usr/bin/env python3
"""Generate the HyperFrames project for "Top 3 Premier League Wonderkids Who Failed".

Source of truth: ../shot-plan.json (event times), ../captions.json (caption track).
Re-run after any re-timing:  python3 build.py
All timed elements are written as explicit HTML; scene timelines use the
production-system motion presets (no overshoot, stepped on twos).
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, '..', 'shot-plan.json')))
CAPS = json.load(open(os.path.join(HERE, '..', 'captions.json')))
EV = {e['id']: e['t_start'] for e in P['events']}
DUR = P['duration']
W, H = 1080, 1920

# ---------------------------------------------------------------- palette
C = dict(teal='#1F8079', royal='#3550B8', sky1='#6EB8F5', sky2='#5A86E0', navy='#2E3388',
         pink='#E0305E', mag1='#C44BD8', mag2='#7A2FA0', grass1='#5BD678', grass2='#3FB65A',
         charcoal='#333333', red='#E5484D', yellow='#FFE13A', gold='#FFC83D', gold2='#E09A1A',
         white='#FFFFFF', black='#000000', skin1='#E8B38F', skin2='#C98A5E', skin3='#8D5A3B')

# ---------------------------------------------------------------- figure rig
POSES = {  # (l_upper, l_fore, r_upper, r_fore, l_thigh, l_shin, r_thigh, r_shin, head_dy, head_dx)
    'stand':     (14, 6, 14, 6, 4, 2, 4, 2, 0, 0),
    'celebrate': (150, 165, 150, 165, 6, 0, 10, -4, -4, 0),
    'slump':     (5, -3, 5, -3, 3, 0, 3, 0, 26, 0),
    'shoot':     (70, 40, 55, 20, 8, 4, 58, 12, 0, 6),
    'limp':      (16, 6, 26, -38, 18, -24, 4, 2, 8, 0),
    'folded':    (10, -100, 10, -100, 3, 1, 3, 1, 0, 0),
    'thumbs':    (10, -100, 28, 172, 3, 1, 3, 1, 0, 0),
}

def _pt(x, y, ang, ln, side):
    a = math.radians(ang)
    dx = math.sin(a) * ln * (-1 if side == 'L' else 1)
    return x + dx, y + math.cos(a) * ln

def _limb(x, y, up, fo, l1, l2, side, w, col_upper, col_fore, sleeve=None):
    ex, ey = _pt(x, y, up, l1, side)
    hx, hy = _pt(ex, ey, fo, l2, side)
    s = (f'<path d="M{x:.0f},{y:.0f} L{ex:.0f},{ey:.0f}" stroke="{col_upper}" stroke-width="{w}" stroke-linecap="round"/>'
         f'<path d="M{ex:.0f},{ey:.0f} L{hx:.0f},{hy:.0f}" stroke="{col_fore}" stroke-width="{w}" stroke-linecap="round"/>')
    if sleeve:
        sx, sy = _pt(x, y, up, l1 * 0.45, side)
        s += f'<path d="M{x:.0f},{y:.0f} L{sx:.0f},{sy:.0f}" stroke="{sleeve}" stroke-width="{w+8}" stroke-linecap="round"/>'
    return s, (hx, hy)

def figure_svg(kit, shorts, socks, hair, skin, num='', numcol='#fff', poses=('stand',), coat=None, hair_style='short'):
    """Generic flat footballer (or manager when coat is given). No facial features."""
    out = []
    for pose in poses:
        lu, lf, ru, rf, lt, ls, rt, rs, hdy, hdx = POSES[pose]
        g = []
        trousers = coat or skin
        # legs
        for side, (tu, sh), hx in (('L', (lt, ls), 178), ('R', (rt, rs), 222)):
            kx, ky = _pt(hx, 540, tu, 150, side)
            fx, fy = _pt(kx, ky, sh, 150, side)
            col = coat if coat else skin
            g.append(f'<path d="M{hx},{540} L{kx:.0f},{ky:.0f}" stroke="{col}" stroke-width="46" stroke-linecap="round"/>')
            g.append(f'<path d="M{kx:.0f},{ky:.0f} L{fx:.0f},{fy:.0f}" stroke="{col}" stroke-width="44" stroke-linecap="round"/>')
            if not coat:
                sx, sy = _pt(kx, ky, sh, 40, side)
                g.append(f'<path d="M{sx:.0f},{sy:.0f} L{fx:.0f},{fy:.0f}" stroke="{socks}" stroke-width="48" stroke-linecap="round"/>')
            bx = fx + (-12 if side == 'L' else 12)
            g.append(f'<ellipse cx="{bx:.0f}" cy="{fy+14:.0f}" rx="34" ry="17" fill="#1b1b1b"/>')
        # shorts / coat body
        if coat:
            g.append(f'<path d="M138,262 L262,262 L272,660 L128,660 Z" fill="{coat}" stroke="{coat}" stroke-width="14" stroke-linejoin="round"/>')
            g.append('<path d="M200,270 L200,650" stroke="rgba(0,0,0,.18)" stroke-width="6"/>')
            g.append('<path d="M176,262 L200,318 L224,262 Z" fill="#E9E4DA"/>')
        else:
            g.append(f'<path d="M146,478 L254,478 L262,578 L210,578 L200,548 L190,578 L138,578 Z" fill="{shorts}" stroke="{shorts}" stroke-width="10" stroke-linejoin="round"/>')
            g.append(f'<path d="M142,262 L258,262 L250,505 L150,505 Z" fill="{kit}" stroke="{kit}" stroke-width="16" stroke-linejoin="round"/>')
            g.append(f'<path d="M180,258 Q200,282 220,258" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="8"/>')
            if num:
                g.append(f'<text x="200" y="420" text-anchor="middle" font-family="Archivo Black" font-size="92" fill="{numcol}" opacity=".92">{num}</text>')
        # arms
        armcol = coat or skin
        sleeve = None if coat else kit
        for side, (up, fo), sx in (('L', (lu, lf), 148), ('R', (ru, rf), 252)):
            s, (hx, hy) = _limb(sx, 280, up, fo, 122, 112, side, 38, armcol, armcol, sleeve)
            g.append(s)
            if coat:
                g.append(f'<circle cx="{hx:.0f}" cy="{hy:.0f}" r="21" fill="{skin}"/>')
                if pose == 'thumbs' and side == 'R':
                    g.append(f'<rect x="{hx-7:.0f}" y="{hy-48:.0f}" width="15" height="34" rx="7" fill="{skin}"/>')
        # head
        hx, hy = 200 + hdx, 170 + hdy
        g.append(f'<rect x="186" y="{215+hdy*0.4:.0f}" width="28" height="40" rx="10" fill="{skin}"/>')
        g.append(f'<circle cx="{hx}" cy="{hy}" r="62" fill="{skin}"/>')
        g.append(f'<circle cx="{hx-60}" cy="{hy+6}" r="13" fill="{skin}" opacity=".9"/>')
        if hair_style == 'short':
            g.append(f'<path d="M{hx-64},{hy-4} C{hx-66},{hy-86} {hx+66},{hy-86} {hx+64},{hy-4} C{hx+44},{hy-38} {hx-40},{hy-46} {hx-64},{hy-4} Z" fill="{hair}"/>')
        elif hair_style == 'manager':
            g.append(f'<path d="M{hx-64},{hy+8} C{hx-70},{hy-80} {hx+70},{hy-80} {hx+64},{hy+8} C{hx+50},{hy-30} {hx-50},{hy-30} {hx-64},{hy+8} Z" fill="{hair}"/>')
        out.append(f'<g class="pose pose-{pose}" opacity="{1 if pose == poses[0] else 0}">{"".join(g)}</g>')
    return f'<svg viewBox="0 0 400 830" width="100%" height="100%" overflow="visible">{"".join(out)}</svg>'

def star_svg(cracked=False, glow=False):
    pts = []
    for i in range(10):
        r = 60 if i % 2 == 0 else 26
        a = math.radians(-90 + i * 36)
        pts.append(f'{70 + r*math.cos(a):.1f},{70 + r*math.sin(a):.1f}')
    s = f'<svg viewBox="0 0 140 140" width="100%" height="100%" overflow="visible">'
    if glow:
        s += '<circle cx="70" cy="70" r="70" fill="rgba(255,255,255,.55)" filter="url(#softglow)"/>'
    s += f'<polygon points="{" ".join(pts)}" fill="{C["gold"]}" stroke="{C["gold2"]}" stroke-width="6" stroke-linejoin="round"/>'
    if cracked:
        s += '<path d="M62,18 L76,52 L58,70 L80,92 L66,124" fill="none" stroke="#7A4A00" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
    return s + '</svg>'

SPARK = '<svg viewBox="-10 -10 20 20" width="100%" height="100%"><path d="M0,-10 L2,-2 L10,0 L2,2 L0,10 L-2,2 L-10,0 L-2,-2 Z" fill="#fff"/></svg>'

def xmark(cls, sw=34):
    return (f'<svg viewBox="0 0 200 200" width="100%" height="100%" overflow="visible">'
            f'<path class="{cls}-1" d="M20,20 L180,180" stroke="{C["red"]}" stroke-width="{sw}" stroke-linecap="butt" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
            f'<path class="{cls}-2" d="M180,20 L20,180" stroke="{C["red"]}" stroke-width="{sw}" stroke-linecap="butt" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')

def cloud_svg(inner=''):
    return ('<svg viewBox="0 0 340 230" width="100%" height="100%" overflow="visible"><g fill="#fff">'
            '<circle cx="90" cy="120" r="72"/><circle cx="170" cy="80" r="80"/><circle cx="252" cy="118" r="72"/>'
            '<circle cx="130" cy="160" r="60"/><circle cx="215" cy="162" r="60"/></g>' + inner + '</svg>')

def mini_goal(bulged_cls):
    return (f'<g transform="translate(92,70)"><rect x="0" y="0" width="156" height="92" fill="none" stroke="#9AA3B5" stroke-width="7"/>'
            f'<g class="{bulged_cls}-flat" stroke="#C9CFDB" stroke-width="2">' + ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="92"/>' for x in range(14, 156, 16)) + ''.join(f'<line x1="0" y1="{y}" x2="156" y2="{y}"/>' for y in range(14, 92, 16)) + '</g>'
            f'<g class="{bulged_cls}-bulge" opacity="0" stroke="#C9CFDB" stroke-width="2">' + ''.join(f'<path d="M{x},0 Q{x+8},46 {x},92" fill="none"/>' for x in range(14, 156, 16)) + ''.join(f'<path d="M0,{y} Q78,{y-12} 156,{y}" fill="none"/>' for y in range(14, 92, 16)) + '</g>'
            f'<circle class="{bulged_cls}-ball" cx="128" cy="24" r="11" fill="#fff" stroke="#333" stroke-width="3"/></g>')

# ---------------------------------------------------------------- shared css / js
BASE_CSS = """
#root{position:absolute;inset:0;overflow:hidden;font-family:'Archivo Black',sans-serif;}
.abs{position:absolute;}
.full{position:absolute;left:0;top:0;width:1080px;height:1920px;}
.fig{position:absolute;}
.hid{opacity:0;}
.name{position:absolute;left:120px;top:412px;width:640px;color:#fff;}
.name .ctx{position:absolute;left:0;font-family:Inter,sans-serif;font-weight:700;font-size:30px;letter-spacing:.12em;white-space:nowrap;background:rgba(0,0,0,.42);padding:3px 12px;border-radius:6px;}
.name .ln{position:absolute;left:0;font-size:84px;line-height:1;white-space:nowrap;text-shadow:0 5px 0 rgba(0,0,0,.18);}
.tag{position:absolute;}
.tag span{display:inline-block;transform:rotate(-8.7deg);font-size:46px;padding:4px 18px 8px;white-space:nowrap;}
.tag.dark span{background:#000;color:#fff;}
.tag.light span{background:#fff;color:#000;}
.grainbg{background-image:url(assets/grain.png);background-size:540px 960px;opacity:.06;mix-blend-mode:multiply;}
"""

HELPERS = """
const TW=1/15;
function E(name,d){const b=gsap.parseEase(name);const n=Math.max(1,Math.round(d/TW));return p=>b(Math.min(1,Math.floor(p*n+1e-6)/n));}
const IR={immediateRender:false};
function show(s,t){tl.set(s,{opacity:1},t);}
function hide(s,t){tl.set(s,{opacity:0},t);}
function pop(s,t,d=.25,f=.7){show(s,t);tl.fromTo(s,{scale:f},{scale:1,duration:d,ease:E('expo.out',d),...IR},t);}
function popH(s,t,d=.45){show(s,t);tl.fromTo(s,{scale:0},{scale:1,duration:d,ease:E('power2.inOut',d),...IR},t);}
function slam(s,t,d=.33){show(s,t);tl.fromTo(s,{scale:1.12},{scale:1,duration:d,ease:E('expo.out',d),...IR},t);}
function rise(s,t,d=.35,dy=1000){show(s,t);tl.fromTo(s,{y:dy},{y:0,duration:d,ease:E('power3.out',d),...IR},t);}
function slideIn(s,t,d=.35,dx=1100){show(s,t);tl.fromTo(s,{x:dx},{x:0,duration:d,ease:E('power3.out',d),...IR},t);}
function slideOut(s,t,d=.25,dx=-1250){tl.fromTo(s,{x:0},{x:dx,duration:d,ease:E('power2.in',d),...IR},t);}
function drop(s,t,d=.45,dy=-560){show(s,t);tl.fromTo(s,{y:dy},{y:0,duration:d,ease:E('expo.out',d),...IR},t);}
function fall(s,t,d=.5,dy=1500,rot=14){tl.fromTo(s,{y:0,rotation:0},{y:dy,rotation:rot,duration:d,ease:E('power2.in',d),...IR},t);}
function draw(s,t,d=.22){show(s,t);tl.fromTo(s,{strokeDashoffset:1},{strokeDashoffset:0,duration:d,ease:E('power2.in',d),...IR},t);}
function pose(fig,name,t){tl.set(fig+' .pose',{opacity:0},t);tl.set(fig+' .pose-'+name,{opacity:1},t);}
function twinkle(sel,t0,t1,seed){let r=seed;const rnd=()=>{r=(r*9301+49297)%233280;return r/233280;};
  document.querySelectorAll(sel).forEach((el,i)=>{let t=t0+rnd()*0.4;while(t<t1-0.4){const d=0.3+rnd()*0.2;
    tl.fromTo(el,{opacity:0,scale:.4},{opacity:1,scale:1,duration:d/2,ease:E('power1.out',d/2),...IR},t);
    tl.to(el,{opacity:0,scale:.4,duration:d/2,ease:E('power1.in',d/2)},t+d/2);t+=d+0.3+rnd()*0.9;}});}
function jitter(s,t0,t1){let k=0;for(let t=t0;t<t1;t+=TW*2){tl.set(s,{x:[1,-1,2,0,-2,1][k%6],y:[0,1,-1,2,0,-1][k%6]},t);k++;}}
"""

def scene(cid, css, body, script, dur):
    return f"""<template>
  <style>{BASE_CSS}{css}</style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}" data-duration="{dur:.3f}">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{HELPERS}
{script}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""

def fig_div(id_, cx, feet, scale, svg, extra_cls=''):
    w, h = 400 * scale, 830 * scale
    return f'<div id="{id_}" class="fig {extra_cls}" data-layout-ignore style="left:{cx - w/2:.0f}px;top:{feet - 800*scale:.0f}px;width:{w:.0f}px;height:{h:.0f}px">{svg}</div>'

def star_div(id_, cx, cy, size=140, cracked=False, glow=False, extra=''):
    return f'<div id="{id_}" class="abs hid {extra}" style="left:{cx-size/2:.0f}px;top:{cy-size/2:.0f}px;width:{size}px;height:{size}px">{star_svg(cracked, glow)}</div>'

def sparks(prefix, pts, size=34):
    return ''.join(f'<div class="abs hid {prefix}" style="left:{x-size/2}px;top:{y-size/2}px;width:{size}px;height:{size}px">{SPARK}</div>' for x, y in pts)

def name_block(id_, ctx, l1, l2, ctx2=None):
    c2 = f'<div id="{id_}-ctx2" class="ctx hid" data-layout-allow-overlap style="top:0">{ctx2}</div>' if ctx2 else ''
    return (f'<div id="{id_}" class="name">'
            f'<div id="{id_}-ctx" class="ctx hid" data-layout-allow-overlap style="top:0">{ctx}</div>{c2}'
            f'<div id="{id_}-l1" class="ln hid" style="top:42px">{l1}</div>'
            f'<div id="{id_}-l2" class="ln hid" style="top:126px">{l2}</div></div>')

def name_anim(id_, t):
    return (f"drop('#{id_}-l2',{t:.3f});drop('#{id_}-l1',{t+0.2:.3f});drop('#{id_}-ctx',{t+0.4:.3f});")

def tag(id_, text, x, y, kind='dark', size=46):
    return f'<div id="{id_}" class="tag {kind} hid" data-layout-allow-overflow style="left:{x}px;top:{y}px"><span style="font-size:{size}px">{text}</span></div>'

DEFS = ('<svg width="0" height="0" style="position:absolute"><defs><filter id="softglow" x="-50%" y="-50%" width="200%" height="200%">'
        '<feGaussianBlur stdDeviation="14"/></filter></defs></svg>')

def L(t, base):  # absolute → local scene time
    return round(t - base, 3)

files = {}
SC = {}  # scene id -> (start, dur)

# ================================================================= HOOK
s0, e0 = 0.0, EV['A1'] + 0.25
SC['hook'] = (s0, e0 - s0)
kits = [('#D7263D', '#FFFFFF', '#D7263D', '#2A1A12', C['skin1'], '27', '#fff'),
        ('#2D5BD7', '#FFFFFF', '#2D5BD7', '#5A3A22', C['skin1'], '26', '#fff'),
        ('#D7263D', '#FFFFFF', '#D7263D', '#141414', C['skin3'], '49', '#fff')]
xs = [250, 540, 830]
body = [f'<div class="full" style="background:radial-gradient(ellipse at 50% 42%, {C["teal"]} 55%, #165C57 100%)"></div>',
        '<div class="abs" style="left:-40px;top:1440px;width:1160px;height:600px;background:#196A64;border-radius:50% 50% 0 0/60px 60px 0 0"></div>',
        f'<svg id="h-arrow" class="full" viewBox="0 0 1080 1920" overflow="visible">'
        f'<path id="h-arrow-rise" class="hid" d="M110,1380 L600,860" stroke="#fff" stroke-width="30" stroke-linecap="butt" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<polygon id="h-arrow-head1" class="hid" points="640,815 556,840 616,900" fill="#fff"/>'
        f'<path id="h-arrow-dive" class="hid" d="M600,860 Q760,730 960,1380" stroke="#fff" stroke-width="30" stroke-linecap="butt" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<polygon id="h-arrow-head2" class="hid" points="972,1438 924,1360 1004,1350" fill="#fff"/></svg>']
for i, (k, sh, so, hair, sk, n, nc) in enumerate(kits):
    body.append(fig_div(f'h-p{i}', xs[i], 1480, 0.85, figure_svg(k, sh, so, hair, sk, n, nc)))
    body.append(star_div(f'h-star{i}', xs[i], 770, 120))
body.append(sparks('h-spk', [(150, 720), (420, 680), (700, 720), (930, 680), (330, 820), (760, 830)], 30))
body.append(f'<div class="full grainbg"></div>')
js = [f"rise('#h-p0',0,.45,700);rise('#h-p1',.133,.45,700);rise('#h-p2',.267,.45,700);"]
t = L(EV['H2'], s0); js.append(f"popH('#h-star0',{t});popH('#h-star1',{t+.133:.3f});popH('#h-star2',{t+.267:.3f});twinkle('.h-spk',{t+.3:.3f},{L(EV['H4b'],s0)},7);")
t = L(EV['H3'], s0); js.append(f"draw('#h-arrow-rise',{t},.25);show('#h-arrow-head1',{t+.25:.3f});")
t = L(EV['H4'], s0); js.append(f"hide('#h-arrow-head1',{t});draw('#h-arrow-dive',{t},.33);show('#h-arrow-head2',{t+.33:.3f});")
t = L(EV['H4b'], s0); js.append(f"fall('#h-star0',{t},.5,1600,-14);fall('#h-star1',{t+.133:.3f},.5,1600,12);fall('#h-star2',{t+.267:.3f},.5,1600,-10);")
files['hook'] = scene('hook', '', '\n'.join(body), '\n'.join(js), e0 - s0)

# ================================================================= #3 MACHEDA
s1, e1 = EV['A1'], EV['B2']
SC['s3'] = (s1, e1 - s1)
mk = ('#D7263D', '#FFFFFF', '#D7263D', '#2A1A12', C['skin1'], '27', '#fff')
body = [f'<div id="s3-sheet" class="full" style="background:{C["royal"]}">',
        # scene A (royal)
        f'<div id="s3-A" class="full">' + fig_div('s3-figA', 640, 1560, 1.15, figure_svg(*mk, poses=('stand', 'celebrate')), 'hid') + '</div>',
        # scene B (pitch)
        f'<div id="s3-B" class="full hid"><div id="s3-Bbg" class="full">'
        f'<div class="full" style="background:repeating-linear-gradient(180deg,{C["grass1"]} 0 160px,#54CC70 160px 320px)"></div>'
        f'<svg class="full" viewBox="0 0 1080 1920"><rect x="540" y="640" width="460" height="260" fill="rgba(255,255,255,.12)" stroke="#fff" stroke-width="14"/>'
        f'<g id="s3-net" stroke="rgba(255,255,255,.55)" stroke-width="3">' + ''.join(f'<line x1="{x}" y1="640" x2="{x}" y2="900"/>' for x in range(570, 1000, 32)) + ''.join(f'<line x1="540" y1="{y}" x2="1000" y2="{y}"/>' for y in range(670, 900, 32)) + '</g>'
        f'<g id="s3-netb" opacity="0" stroke="rgba(255,255,255,.7)" stroke-width="3">' + ''.join(f'<path d="M{x},640 Q{x+16},770 {x},900" fill="none"/>' for x in range(570, 1000, 32)) + ''.join(f'<path d="M540,{y} Q770,{y-26} 1000,{y}" fill="none"/>' for y in range(670, 900, 32)) + '</g>'
        f'<rect x="0" y="1500" width="1080" height="8" fill="rgba(255,255,255,.6)"/></svg>'
        + fig_div('s3-figB', 300, 1500, 1.05, figure_svg(*mk, poses=('stand', 'shoot'))) +
        f'<div id="s3-ball" class="abs" style="left:478px;top:1398px;width:84px;height:84px"><svg viewBox="0 0 84 84" width="100%" height="100%"><circle cx="42" cy="42" r="38" fill="#fff" stroke="#2b2b2b" stroke-width="5"/><polygon points="42,26 55,36 50,52 34,52 29,36" fill="#2b2b2b"/></svg></div>'
        f'</div>'
        f'<div id="s3-score" class="abs hid" style="left:140px;top:640px;width:800px;height:240px;background:#23262E;border:5px solid #D9D9D9;border-radius:30px;color:#fff;text-align:center">'
        f'<div style="margin:22px auto 0;width:150px;background:#000;border-radius:10px;font-size:40px;padding:4px 0">90+3\'</div>'
        f'<div style="margin-top:22px;font-size:44px;letter-spacing:.01em;white-space:nowrap">MAN UTD <span style="color:{C["yellow"]}">3–2</span> ASTON VILLA</div></div>'
        f'</div>',
        # scene C (charcoal)
        f'<div id="s3-C" class="full hid" style="background:{C["charcoal"]}">' + fig_div('s3-figC', 640, 1560, 1.15, figure_svg(*mk, poses=('stand', 'slump'))) +
        f'<div id="s3-bub" class="abs hid" style="left:640px;top:300px;width:400px;height:300px">'
        f'<div class="abs" style="left:-4px;top:250px;width:30px;height:30px;border-radius:50%;background:#fff"></div><div class="abs" style="left:30px;top:215px;width:44px;height:44px;border-radius:50%;background:#fff"></div>'
        f'<div class="abs" style="left:60px;top:0;width:340px;height:230px">{cloud_svg(mini_goal("s3-mg"))}</div></div>'
        + star_div('s3-starC', 640, 670, 140, extra='') + f'<div id="s3-xC" class="abs" style="left:550px;top:580px;width:180px;height:180px">{xmark("s3x")}</div>' +
        star_div('s3-starCk', 640, 670, 140, cracked=True) +
        f'</div>',
        star_div('s3-starA', 640, 670, 140),
        sparks('s3-spk', [(520, 580), (770, 620), (540, 760), (770, 750)], 30),
        tag('s3-age', 'age 17', 390, 985),
        name_block('s3-name', 'MAN UTD · 2009', 'FEDERICO', 'MACHEDA'),
        '</div>', '<div class="full grainbg"></div>']
b = s1
js = [f"tl.fromTo('#s3-sheet',{{y:1920}},{{y:0,duration:.2,ease:E('expo.out',.2)}},0);",
      f"pop('#s3-age',{L(EV['A3'],b)});", f"rise('#s3-figA',{L(EV['A4'],b)},.35);", name_anim('s3-name', L(EV['A5'], b)),
      f"popH('#s3-starA',{L(EV['A6'],b)});pose('#s3-figA','celebrate',{L(EV['A6'],b)});twinkle('.s3-spk',{L(EV['A6'],b)+.3:.3f},{L(EV['A7'],b)},3);",
      # A7 hard cut to pitch
      f"t7={L(EV['A7'],b)};hide('#s3-A',t7);hide('#s3-starA',t7);hide('#s3-age',t7);show('#s3-B',t7);pose('#s3-figB','stand',t7);pose('#s3-figB','shoot',t7+.133);",
      f"t8={L(EV['A8'],b)};tl.fromTo('#s3-ball',{{x:0,y:0,scale:1}},{{x:440,y:-740,scale:.35,duration:.35,ease:E('expo.out',.35),...IR}},t8);tl.set('#s3-net',{{opacity:0}},t8+.3);tl.set('#s3-netb',{{opacity:1}},t8+.3);tl.set('#s3-net',{{opacity:1}},t8+.433);tl.set('#s3-netb',{{opacity:0}},t8+.433);",
      f"t9={L(EV['A9'],b)};pop('#s3-score',t9);tl.fromTo('#s3-Bbg',{{filter:'blur(0px)'}},{{filter:'blur(10px)',duration:.18,ease:'none',...IR}},t9);",
      # A10 hard cut to charcoal
      f"t10={L(EV['A10'],b)};hide('#s3-B',t10);hide('#s3-score',t10);show('#s3-C',t10);show('#s3-starC',t10);show('#s3-age',t10);twinkle('.s3-spk',t10,t10+1.4,11);",
      f"t=({L(EV['A10a'],b)});popH('#s3-bub',t,.3);tl.set('.s3-mg-flat',{{opacity:0}},t+.5);tl.set('.s3-mg-bulge',{{opacity:1}},t+.5);tl.set('.s3-mg-flat',{{opacity:1}},t+.633);tl.set('.s3-mg-bulge',{{opacity:0}},t+.633);",
      f"tl.to('#s3-bub',{{scale:0,duration:.25,ease:E('power2.in',.25)}},{L(EV['A10b'],b)});",
      f"t=({L(EV['A11'],b)});[6,-6,4,0].forEach((r,i)=>tl.set('#s3-starC',{{rotation:r}},t+i*.133));tl.to('#s3-starC',{{y:40,opacity:.6,duration:.45,ease:E('power2.in',.45)}},t+.533);",
      f"tl.set('#s3-xC',{{y:40}},0);draw('#s3xC1',{L(EV['A12'],b)},.2);draw('#s3xC2',{L(EV['A12b'],b)},.2);jitter('#s3-xC',{L(EV['A12b'],b)+.2:.3f},{L(EV['A13'],b)});",
      f"t=({L(EV['A13'],b)});hide('#s3-starC',t);tl.set('#s3-starCk',{{opacity:.6,y:40}},t);fall('#s3-starCk',t,.5,1400,16);fall('#s3-xC',t,.5,1400,16);pose('#s3-figC','slump',t);",
      f"t=({L(EV['B1'],b)});slideOut('#s3-figC',t);slideOut('#s3-age',t);slideOut('#s3-name',t);"]
files['s3'] = scene('s3', '', '\n'.join(body).replace('class="s3x-1"', 'id="s3xC1"').replace('class="s3x-2"', 'id="s3xC2"'), '\n'.join(js), e1 - s1)

# ================================================================= #2 RODWELL
s2, e2 = EV['B2'], EV['C1'] + 0.40
SC['s2'] = (s2, e2 - s2)
ev_ = ('#2D5BD7', '#FFFFFF', '#2D5BD7', '#5A3A22', C['skin1'], '26', '#fff')
city = ('#8CC8F2', '#FFFFFF', '#8CC8F2', '#5A3A22', C['skin1'], '26', '#1E2A55')
white = ('#F4F4F4', '#1E2A55', '#F4F4F4', '#5A3A22', C['skin1'], '', '#1E2A55')
blue_mini = ('#2D5BD7', '#FFFFFF', '#2D5BD7', '#5A3A22', C['skin1'], '', '#fff')
body = [f'<div id="s2-A" class="full" style="background:linear-gradient(180deg,{C["sky1"]},{C["sky2"]})">'
        + fig_div('s2-figA', 640, 1560, 1.15, figure_svg(*ev_), 'hid') +
        f'<div id="s2-bub" class="abs hid" style="left:640px;top:300px;width:400px;height:320px">'
        f'<div class="abs" style="left:-4px;top:270px;width:30px;height:30px;border-radius:50%;background:#fff"></div><div class="abs" style="left:30px;top:232px;width:44px;height:44px;border-radius:50%;background:#fff"></div>'
        f'<div class="abs" style="left:60px;top:0;width:340px;height:240px">{cloud_svg()}</div>'
        f'<div id="s2-mini-b" class="abs" style="left:180px;top:30px;width:96px;height:200px">{figure_svg(*blue_mini)}</div>'
        f'<div id="s2-mini-w" class="abs hid" style="left:180px;top:30px;width:96px;height:200px">{figure_svg(*white)}</div>'
        f'<div id="s2-mstar" class="abs hid" style="left:262px;top:14px;width:60px;height:60px">{star_svg()}</div></div>'
        f'</div>',
        f'<div id="s2-B" class="full hid" style="background:{C["navy"]}">'
        + fig_div('s2-figB', 290, 1560, 1.15, figure_svg(*city, poses=('stand', 'limp'))) +
        tag('s2-money', '£ MILLIONS', 150, 960, 'light') +
        f'<div id="s2-cross" class="abs hid" style="left:170px;top:1380px;width:84px;height:84px"><svg viewBox="0 0 84 84" width="100%" height="100%"><circle cx="42" cy="42" r="40" fill="#fff"/><path d="M42,18 L42,66 M18,42 L66,42" stroke="{C["red"]}" stroke-width="16"/></svg></div>'
        f'<div id="s2-ice" class="abs hid" style="left:250px;top:1340px;width:110px;height:70px"><svg viewBox="0 0 110 70" width="100%" height="100%"><rect x="4" y="8" width="102" height="56" rx="18" fill="#DCEFFF" stroke="#9CC7EE" stroke-width="5"/><rect x="40" y="0" width="30" height="16" rx="5" fill="#9CC7EE"/></svg></div>'
        f'<svg class="full" viewBox="0 0 1080 1920" overflow="visible">'
        f'<path id="s2-axis" class="hid" d="M580,700 L580,1060 L990,1060" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="butt" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<path id="s2-zig" class="hid" d="M600,1020 L660,790 L720,980 L780,750 L840,950 L900,830" stroke="{C["yellow"]}" stroke-width="12" fill="none" stroke-linejoin="round" stroke-linecap="butt" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<g id="s2-tail" class="hid"><path d="M900,830 L960,900" stroke="{C["yellow"]}" stroke-width="12" stroke-linecap="round"/></g></svg>'
        f'<div id="s2-zx" class="abs hid" style="left:872px;top:802px;width:56px;height:56px">{xmark("s2zx", 40)}</div>'
        f'</div>',
        f'<div id="s2-C" class="full hid" style="background:{C["pink"]}"><div id="s2-Cdark" class="full hid" style="background:{C["charcoal"]}"></div>'
        + fig_div('s2-figC', 540, 1560, 1.15, figure_svg(*city)) + star_div('s2-starC', 540, 670, 150, glow=True) + '</div>',
        name_block('s2-name', 'EVERTON · 2008', 'JACK', 'RODWELL', ctx2='EVERTON → MAN CITY · 2012'),
        '<div class="full grainbg"></div>']
b = s2
js = [f"slideIn('#s2-figA',{L(EV['B3'],b)});", name_anim('s2-name', L(EV['B3b'], b)),
      f"t=({L(EV['B4'],b)});popH('#s2-bub',t,.3);",
      f"t=({L(EV['B4b'],b)});hide('#s2-mini-b',t);show('#s2-mini-w',t);",
      f"popH('#s2-mstar',{L(EV['B5'],b)},.4);",
      # B6 whip push
      f"t=({L(EV['B6'],b)});tl.fromTo('#s2-A',{{x:0,filter:'blur(0px)'}},{{x:-1080,filter:'blur(18px)',duration:.3,ease:E('power2.in',.3),...IR}},t);show('#s2-B',t+.267);tl.fromTo('#s2-B',{{x:1080,filter:'blur(14px)'}},{{x:0,filter:'blur(0px)',duration:.16,ease:E('power3.out',.16),...IR}},t+.267);hide('#s2-A',t+.3);",
      f"t=({L(EV['B7'],b)});hide('#s2-name-ctx',t);show('#s2-name-ctx2',t);",
      f"pop('#s2-money',{L(EV['B7b'],b)});",
      f"t=({L(EV['B8'],b)});pose('#s2-figB','limp',t);popH('#s2-cross',t,.4);show('#s2-ice',t+.1);tl.fromTo('#s2-ice',{{y:-1100,rotation:10}},{{y:0,rotation:0,duration:.5,ease:E('power2.in',.5),...IR}},t+.1);",
      f"t=({L(EV['B9'],b)});draw('#s2-axis',t,.2);draw('#s2-zig',t+.2,.45);show('#s2-tail',t+.65);",
      f"t=({L(EV['B10'],b)});tl.fromTo('#s2-tail',{{y:0,rotation:0}},{{y:900,rotation:60,svgOrigin:'900 830',duration:.5,ease:E('power2.in',.5),...IR}},t);show('#s2-zx',t);tl.set('#s2zx1,#s2zx2',{{strokeDashoffset:0}},t);pop('#s2-zx',t);",
      f"t=({L(EV['B11'],b)});hide('#s2-B',t);show('#s2-C',t);",
      f"slam('#s2-starC',{L(EV['B11b'],b)});",
      f"t=({L(EV['B12'],b)});show('#s2-Cdark',t);tl.set('#s2-figC',{{filter:'grayscale(1) brightness(.85)'}},t);tl.set('#s2-name',{{opacity:.3}},t);fall('#s2-starC',t,.5,1400,-14);",
      f"t=({L(EV['C1'],b)});slideOut('#s2-figC',t);slideOut('#s2-name',t);"]
files['s2'] = scene('s2', '', '\n'.join(body).replace('class="s2zx-1"', 'id="s2zx1"').replace('class="s2zx-2"', 'id="s2zx2"'), '\n'.join(js), e2 - s2)

# ================================================================= #1 MORRISON
s3_, e3 = e2, EV['D1'] + 0.25
SC['s1'] = (s3_, e3 - s3_)
mo = ('#D7263D', '#FFFFFF', '#D7263D', '#141414', C['skin3'], '49', '#fff')
mgr = ('#2B2F3A', '#2B2F3A', '#2B2F3A', '#BDBDBD', C['skin1'])
body = [f'<div id="s1-A" class="full" style="background:linear-gradient(180deg,{C["mag1"]},{C["mag2"]})">'
        + fig_div('s1-mgr', 320, 1560, 1.05, figure_svg(*mgr, poses=('folded', 'thumbs'), coat='#2B2F3A', hair_style='manager'), 'hid')
        + tag('s1-mtag', 'SIR ALEX FERGUSON', 130, 1010, 'light', 36) +
        f'<div id="s1-sb" class="abs hid" style="left:110px;top:640px;width:440px;height:200px">'
        f'<svg viewBox="0 0 440 200" width="100%" height="100%" overflow="visible"><rect x="0" y="0" width="440" height="150" rx="34" fill="#fff"/><path d="M180,146 L200,196 L250,146 Z" fill="#fff"/></svg>'
        f'<div class="abs" style="left:24px;top:10px;width:392px;font-family:\'League Gothic\';font-size:62px;line-height:1.02;color:#1d1d1d;text-align:center">"ONE OF THE MOST GIFTED I\'VE SEEN"</div></div>'
        + fig_div('s1-mo', 750, 1560, 1.15, figure_svg(*mo), 'hid') + star_div('s1-starA', 750, 680, 140) +
        '<svg id="s1-burst" class="full hid" viewBox="0 0 1080 1920">' + ''.join(
            f'<line x1="{750+math.cos(math.radians(a))*170:.0f}" y1="{1000+math.sin(math.radians(a))*170:.0f}" x2="{750+math.cos(math.radians(a))*240:.0f}" y2="{1000+math.sin(math.radians(a))*240:.0f}" stroke="#fff" stroke-width="12" stroke-linecap="round"/>' for a in range(0, 360, 45)) + '</svg>'
        + sparks('s1-spk', [(630, 640), (880, 660), (640, 780), (870, 800)], 30) + '</div>',
        f'<div id="s1-B" class="full hid" style="background:linear-gradient(180deg,{C["grass1"]},{C["grass2"]})">'
        + fig_div('s1-moB', 290, 1520, 1.0, figure_svg(*mo)) + star_div('s1-starB', 290, 760, 110) + star_div('s1-starBk', 290, 760, 110, cracked=True) +
        f'<div id="s1-cloud" class="abs hid" style="left:100px;top:700px;width:130px;height:90px"><svg viewBox="0 0 130 90" width="100%" height="100%"><g fill="#6B7280"><circle cx="40" cy="52" r="30"/><circle cx="70" cy="36" r="34"/><circle cx="98" cy="54" r="28"/><rect x="30" y="52" width="80" height="30" rx="15"/></g><path d="M62,80 L52,104 L70,96 L60,122" stroke="{C["yellow"]}" stroke-width="7" fill="none"/></svg></div>'
        + ''.join(f'<div id="s1-warn{i}" class="abs hid" style="left:{x}px;top:{y}px;width:84px;height:76px"><svg viewBox="0 0 84 76" width="100%" height="100%"><path d="M42,4 L80,72 L4,72 Z" fill="{C["yellow"]}" stroke="#1d1d1d" stroke-width="6" stroke-linejoin="round"/><rect x="38" y="26" width="8" height="26" fill="#1d1d1d"/><circle cx="42" cy="61" r="5" fill="#1d1d1d"/></svg></div>' for i, (x, y) in enumerate([(100, 980), (420, 1030)])) +
        f'<svg class="full" viewBox="0 0 1080 1920" overflow="visible">'
        f'<path id="s1-pot" class="hid" d="M500,680 L880,680" stroke="#fff" stroke-width="8" stroke-dasharray="0.04 0.025" pathLength="1" fill="none"/>'
        f'<rect id="s1-gauge" class="hid" x="580" y="680" width="140" height="440" rx="14" fill="rgba(0,0,0,.12)" stroke="#fff" stroke-width="8"/>'
        f'<rect id="s1-bar" x="590" y="690" width="120" height="420" rx="8" fill="{C["gold"]}"/>'
        f'<rect id="s1-barrier" class="hid" x="550" y="800" width="200" height="26" fill="{C["red"]}"/></svg>'
        f'<div id="s1-potl" class="abs hid" style="left:600px;top:622px;font-family:Inter;font-weight:700;font-size:32px;letter-spacing:.1em;color:#fff">POTENTIAL</div>'
        f'<div id="s1-potx" class="abs" style="left:640px;top:592px;width:110px;height:110px">{xmark("s1px", 26)}</div>'
        f'<div class="abs" style="left:560px;top:1062px;width:180px;text-align:center;font-family:Inter;font-weight:700;font-size:28px;letter-spacing:.1em;color:#1d1d1d" id="s1-tal-l"><span id="s1-tal" class="hid" style="display:inline-block">TALENT</span></div>'
        f'</div>',
        name_block('s1-name', 'MAN UTD · 2010', 'RAVEL', 'MORRISON'),
        '<div class="full grainbg"></div>']
b = s3_
js = ["tl.set('#s1-bar',{scaleY:0,transformOrigin:'50% 100%'},0);",f"rise('#s1-mgr',{L(EV['C2'],b)},.35);pop('#s1-mtag',{L(EV['C2'],b)+.25:.3f});",
      f"popH('#s1-sb',{L(EV['C3'],b)},.3);tl.set('#s1-sb',{{transformOrigin:'48% 100%'}},0);",
      f"slideIn('#s1-mo',{L(EV['C4'],b)});", name_anim('s1-name', L(EV['C4b'], b)),
      f"t=({L(EV['C5'],b)});slam('#s1-starA',t);show('#s1-burst',t);tl.fromTo('#s1-burst',{{scale:.7,opacity:1,transformOrigin:'750px 1000px'}},{{scale:1.15,opacity:0,duration:.4,ease:E('power2.out',.4),...IR}},t);twinkle('.s1-spk',t+.3,{L(EV['C6'],b)},5);",
      f"pose('#s1-mgr','thumbs',{L(EV['C5b'],b)});",
      f"t=({L(EV['C6'],b)});hide('#s1-A',t);show('#s1-B',t);show('#s1-starB',t);draw('#s1-pot',t,.25);tl.set('#s1-pot',{{strokeDasharray:'0.04 0.025'}},t+.25);show('#s1-gauge',t);tl.fromTo('#s1-gauge',{{opacity:0}},{{opacity:1,duration:.2,ease:E('none',.2),...IR}},t);show('#s1-potl',t+.2);show('#s1-tal',t+.2);",
      f"tl.fromTo('#s1-bar',{{scaleY:0}},{{scaleY:.85,duration:.45,ease:E('expo.out',.45),...IR}},{L(EV['C7'],b)});",
      f"t=({L(EV['C8'],b)});popH('#s1-cloud',t,.4);pop('#s1-warn0',t+.45);pop('#s1-warn1',t+.583);",
      f"t=({L(EV['C9'],b)});[.55,.75,.4].forEach((v,i)=>tl.set('#s1-bar',{{scaleY:v}},t+(i+1)*.15));",
      f"t=({L(EV['C10'],b)});slam('#s1-barrier',t);tl.fromTo('#s1-bar',{{scaleY:.4}},{{scaleY:.74,duration:.3,ease:E('expo.out',.3),...IR}},t+1.1);",
      f"t=({L(EV['C10b'],b)});draw('#s1px1',t-.2,.2);draw('#s1px2',t+.05,.2);hide('#s1-starB',t);show('#s1-starBk',t);fall('#s1-starBk',t+.1,.5,1400,15);",
      ]
files['s1'] = scene('s1', '', '\n'.join(body).replace('class="s1px-1"', 'id="s1px1"').replace('class="s1px-2"', 'id="s1px2"'), '\n'.join(js), e3 - s3_)

# ================================================================= OUTRO
s4, e4 = EV['D1'], DUR
SC['outro'] = (s4, e4 - s4)
final = [('#D7263D', '#FFFFFF', '#D7263D', '#2A1A12', C['skin1'], '27', '#fff'),
         ('#8CC8F2', '#FFFFFF', '#8CC8F2', '#5A3A22', C['skin1'], '26', '#1E2A55'),
         ('#D7263D', '#FFFFFF', '#D7263D', '#141414', C['skin3'], '49', '#fff')]
body = [f'<div id="o-wrap" class="full">',
        f'<div class="full" style="background:radial-gradient(ellipse at 50% 42%, {C["teal"]} 55%, #165C57 100%)"></div>',
        '<div class="abs" style="left:-40px;top:1440px;width:1160px;height:600px;background:#196A64;border-radius:50% 50% 0 0/60px 60px 0 0"></div>',
        f'<svg class="full" viewBox="0 0 1080 1920" overflow="visible">'
        f'<path id="o-arrow-rise" class="hid" d="M110,1380 L600,860" stroke="#fff" stroke-width="30" stroke-linecap="butt" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<polygon id="o-head1" class="hid" points="640,815 556,840 616,900" fill="#fff"/>'
        f'<path id="o-arrow-dive" class="hid" d="M600,860 Q760,730 960,1380" stroke="#fff" stroke-width="30" stroke-linecap="butt" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        f'<polygon id="o-head2" class="hid" points="972,1438 924,1360 1004,1350" fill="#fff"/></svg>']
OX=[260,540,800]
for i, k in enumerate(final):
    body.append(fig_div(f'o-p{i}', OX[i], 1480, 0.8, figure_svg(*k, poses=('stand', 'slump'))))
    body.append(star_div(f'o-star{i}', OX[i], 800, 116))
    body.append(star_div(f'o-stark{i}', OX[i], 800, 116, cracked=True))
    body.append(f'<div id="o-rank{i}" class="tag dark" data-layout-allow-overflow style="left:{OX[i]-56}px;top:1062px"><span style="font-size:48px">#{3-i}</span></div>')
for i, (x, y, s) in enumerate([(170, 330, 170), (520, 300, 210), (800, 360, 160)]):
    body.append(f'<div id="o-q{i}" class="abs hid" style="left:{x-s/2:.0f}px;top:{y}px;width:{s}px;text-align:center;font-size:{s}px;line-height:1;color:#fff;text-shadow:0 8px 0 rgba(0,0,0,.15)">?</div>')
body += ['<div class="full grainbg"></div>', '</div>']
b = s4
js = [f"tl.fromTo('#o-wrap',{{clipPath:'inset(0% 0% 100% 0%)'}},{{clipPath:'inset(0% 0% 0% 0%)',duration:.2,ease:E('power2.out',.2),...IR}},0);",
      f"t=({L(EV['D2'],b)});popH('#o-star0',t);popH('#o-star1',t+.133);popH('#o-star2',t+.267);",
      f"t=({L(EV['D2b'],b)});draw('#o-arrow-rise',t,.25);show('#o-head1',t+.25);",
      f"t=({L(EV['D3'],b)});hide('#o-head1',t);draw('#o-arrow-dive',t,.33);show('#o-head2',t+.33);"
      + ''.join(f"hide('#o-star{i}',t);show('#o-stark{i}',t);fall('#o-stark{i}',{L(EV['D3'],b)+0.25+i*0.133:.3f},.5,1600,{[-14,12,-10][i]});" for i in range(3))
      + ''.join(f"pose('#o-p{i}','slump',{L(next(w for w in [e for e in P['events'] if e['id']=='D3'])['t_kw'],b)+0.66:.3f});" for i in range(3)),
      f"t=({L(EV['D4'],b)});popH('#o-q0',t,.4);popH('#o-q1',t+.133,.4);popH('#o-q2',t+.267,.4);"
      + ''.join(f"tl.to('#o-rank{i}',{{scale:1.08,duration:.15,ease:E('power2.out',.15)}},t+.4);tl.to('#o-rank{i}',{{scale:1,duration:.15,ease:E('power2.in',.15)}},t+.55);" for i in range(3))]
files['outro'] = scene('outro', '', '\n'.join(body), '\n'.join(js), e4 - s4)

# ================================================================= RANK BADGE overlay
sb, eb = EV['A2'], EV['D1']
SC['badge'] = (sb, eb - sb)
body = ['<div id="bd-box" class="tag dark hid" data-layout-allow-overflow style="left:120px;top:302px"><span style="font-size:72px;padding:2px 24px 8px">'
        '<b id="bd-3">#3</b><b id="bd-2" style="display:none">#2</b><b id="bd-1" style="display:none">#1</b></span></div>']
js = [f"pop('#bd-box',0);",
      f"tl.set('#bd-3',{{display:'none'}},{L(EV['B2'],sb)});tl.set('#bd-2',{{display:'inline'}},{L(EV['B2'],sb)});",
      f"tl.set('#bd-2',{{display:'none'}},{L(e2,sb)});tl.set('#bd-1',{{display:'inline'}},{L(e2,sb)});"]
files['badge'] = scene('badge', '', '\n'.join(body), '\n'.join(js), eb - sb)

# ================================================================= CAPTIONS
cap_css = """
.cap{position:absolute;left:0;width:1080px;text-align:center;font-family:'League Gothic',sans-serif;color:#fff;text-transform:uppercase;}
.cap.hook{top:410px;font-size:146px;line-height:.92;text-shadow:0 8px 3px rgba(30,30,30,.55);}
.cap.body{top:1128px;font-size:88px;line-height:1;text-shadow:4px 5px 6px rgba(0,0,0,.45);}
"""
body, js = [], []
for i, c in enumerate(CAPS):
    txt = c['text'].replace('|', '<br>') if c['mode'] == 'HOOK' else c['text']
    body.append(f'<div id="cap{i}" class="cap {"hook" if c["mode"]=="HOOK" else "body"} hid" data-layout-allow-caption-zone>{txt}</div>')
    js.append(f"tl.set('#cap{i}',{{opacity:1,visibility:'visible'}},{c['start']:.3f});tl.set('#cap{i}',{{opacity:0,visibility:'hidden'}},{c['end']:.3f});")
files['captions'] = scene('captions', cap_css, '\n'.join(body), '\n'.join(js), DUR)
SC['captions'] = (0, DUR)

# ================================================================= SFX map ([EXTENSION], quiet)
SFXDUR = {'click-soft': 0.365688, 'impact-bass-1': 2.115906, 'pop': 0.72, 'sparkle': 1.802438, 'whoosh-short': 0.574688}
VOL = {'pop': .07, 'whoosh-short': .06, 'click-soft': .09, 'impact-bass-1': .05, 'sparkle': .045}
SFX = [(.10, 'whoosh-short'), (EV['H2'], 'pop'), (EV['H3'], 'click-soft'), (EV['H4b'] + .05, 'impact-bass-1'),
       (EV['A1'], 'whoosh-short'), (EV['A6'], 'sparkle'), (EV['A8'] + .02, 'impact-bass-1'), (EV['A9'], 'click-soft'),
       (EV['A10a'], 'pop'), (EV['A12'], 'click-soft'), (EV['A12b'], 'click-soft'), (EV['A13'] + .25, 'impact-bass-1'),
       (EV['B1'], 'whoosh-short'), (EV['B4'], 'pop'), (EV['B6'] + .1, 'whoosh-short'), (EV['B7b'], 'click-soft'),
       (EV['B8'], 'pop'), (EV['B9'], 'click-soft'), (EV['B10'], 'impact-bass-1'), (EV['B11b'], 'sparkle'),
       (EV['B12'] + .1, 'impact-bass-1'), (EV['C1'], 'whoosh-short'), (EV['C3'], 'pop'), (EV['C4'], 'whoosh-short'),
       (EV['C5'], 'sparkle'), (EV['C7'], 'whoosh-short'), (EV['C8'], 'pop'), (EV['C10'], 'impact-bass-1'),
       (EV['C10b'] - .2, 'click-soft'), (EV['D1'], 'whoosh-short'), (EV['D2'], 'pop'), (EV['D2b'], 'click-soft'),
       (EV['D3'] + .25, 'impact-bass-1'), (EV['D4'], 'pop')]
SFX.sort()
for a, b2 in zip(SFX, SFX[1:]):
    assert b2[0] - a[0] >= 0.15, ('sfx too close', a, b2)

import subprocess
VDUR=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',os.path.join(HERE,'assets/voice/narration.wav')],capture_output=True,text=True).stdout)
# ================================================================= ROOT
order = [('hook', 1), ('s3', 2), ('s2', 3), ('s1', 4), ('outro', 5), ('badge', 10), ('captions', 20)]
hosts = []
for cid, z in order:
    st, du = SC[cid]
    kind = 'captions' if cid == 'captions' else 'graphics'
    lane = 0 if cid in ('hook', 's2', 'outro') else (1 if cid in ('s3', 's1') else (2 if cid == 'badge' else 3))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{st:.3f}" data-duration="{du:.3f}" '
                 f'data-track-index="{lane}" data-track-kind="{kind}" data-width="{W}" data-height="{H}" style="z-index:{z}"></div>')
aud = [f'      <audio id="voice" class="clip" src="assets/voice/narration.wav" data-start="0" data-duration="{VDUR:.3f}" data-track-index="5" data-volume="1"></audio>']
lane_end = {}
for i, (t, n) in enumerate(SFX):
    lane = 6 + next(k for k in range(8) if lane_end.get(k, -1) <= t); lane_end[lane-6] = t + SFXDUR[n]
    aud.append(f'      <audio id="sfx{i}" class="clip" src="assets/sfx/{n}.mp3" data-start="{t:.3f}" data-duration="{SFXDUR[n]:.3f}" data-track-index="{lane}" data-volume="{VOL[n]}"></audio>')
root = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: {C['teal']}; }}
      #root {{ position: relative; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    {DEFS}
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:.3f}" data-width="{W}" data-height="{H}">
{chr(10).join(hosts)}
{chr(10).join(aud)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
os.makedirs(os.path.join(HERE, 'compositions'), exist_ok=True)
for k, v in files.items():
    open(os.path.join(HERE, 'compositions', f'{k}.html'), 'w').write(v)
open(os.path.join(HERE, 'index.html'), 'w').write(root)

# grain texture (deterministic)
try:
    import numpy as np
    from PIL import Image
    rng = np.random.default_rng(42)
    g = (rng.normal(128, 60, (960, 540))).clip(0, 255).astype('uint8')
    Image.fromarray(g, 'L').save(os.path.join(HERE, 'assets', 'grain.png'))
except Exception as ex:
    print('grain skipped', ex)
print('scenes:', {k: (round(a, 2), round(d, 2)) for k, (a, d) in SC.items()}, 'sfx:', len(SFX), 'duration', DUR)
