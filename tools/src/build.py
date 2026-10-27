#!/usr/bin/env python3
"""
PPC Birds static site builder.
Generates every page in ../ppc-birds from shared partials + content data.
Run:  python3 build.py
"""
import os, re, html
from icons import icon, ARROW, CHEV, PLUS
from data_services import SERVICES, BY_SLUG, PARENTS, STATS, STEPS
from data_content import INDUSTRIES, IND_BY_SLUG, POSTS, POST_BY_SLUG, CASES, FAQ_GROUPS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '..')
SRC = lambda f: open(os.path.join(HERE, f), encoding='utf-8').read()

HEADER = SRC('header.html')
FOOTER = SRC('footer.html')
HOME_MAIN = SRC('home_main.html')
SVC_MAIN = SRC('services_main.html')

PHONE, EMAIL = '763241567889', 'ppcbirds@gmail.com'
E = html.escape

def U(pid, w=900, h=None):
    q = f'&h={h}' if h else ''
    return f'https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}{q}&q=70'

def block(src, start, end=None):
    """Cut a section out of a source page by its banner comment."""
    i = src.index(start)
    j = src.index(end, i) if end else len(src)
    return src[i:j].strip()

# Reusable blocks lifted from the approved pages
CTA = block(HOME_MAIN, '<!-- ====================== 14 · CTA')
HOME_FAQ = block(HOME_MAIN, '<!-- ====================== 13 · FAQ', '<!-- ====================== 14 · CTA')
FLOW = block(SVC_MAIN, '<!-- ====================== 06 · WORK PROCESS', '<!-- ====================== 07')
BENTO = block(SVC_MAIN, '<!-- ====================== 07 · IMPACT', '<!-- ====================== 08')
LOGOS = block(SVC_MAIN, '<!-- ====================== 08 · PLATFORMS', '<!-- ====================== 09')
TMARQ = block(SVC_MAIN, '<!-- ====================== 09 · TESTIMONIALS', '<!-- ====================== 10')

# ------------------------------------------------------------------ URL map
LINKS = {
  '/home': 'index.html', '/about/': 'about.html', '/contact/': 'contact.html', '/blog/': 'blog.html',
  '/portfolio/': 'portfolio.html', '/results/': 'portfolio.html', '/faq/': 'faq.html', '/free-audit/': 'free-audit.html',
  '/privacy-policy/': 'privacy-policy.html', '/terms/': 'terms.html',
  '/ppc-management/': 'ppc-management.html',
  '/ppc-management/google-ads-management/': 'google-ads-management.html',
  '/ppc-management/bing-ads/': 'bing-ads.html',
  '/ppc-management/chatgpt-ads-management/': 'chatgpt-ads-management.html',
  '/social-media-marketing/': 'social-media-marketing.html',
  '/social-media-marketing/meta-ads-management/': 'meta-ads-management.html',
  '/social-media-marketing/tiktok-ads-management/': 'tiktok-ads-management.html',
  '/conversion-tracking/': 'conversion-tracking.html',
  '/conversion-tracking/enhanced-conversions/': 'enhanced-conversions.html',
  '/conversion-tracking/meta-pixel-meta-capi/': 'meta-pixel-meta-capi.html',
  '/conversion-tracking/server-side-tracking/': 'server-side-tracking.html',
  '/call-tracking/': 'call-tracking.html',
  '/calltracking/calltrackingmetricssetup/': 'calltrackingmetrics-setup.html',
  '/call-tracking/callrail-setup/': 'callrail-setup.html',
  '/landing-page-design/': 'landing-page-design.html',
  '/website-design-development/': 'website-design-development.html',
  '/website-design-development/wordpress': 'wordpress-development.html',
  '/website-design-development/wix': 'wix-development.html',
  '/website-design-development/squarespace': 'squarespace-development.html',
  '/website-design-development/godaddy': 'godaddy-development.html',
  '/website-design-development/shopify': 'shopify-development.html',
}
for i in INDUSTRIES:
    LINKS[f"/industries/{i['slug']}/"] = f"{i['slug']}.html"

def map_links(x):
    return re.sub(r'href="(/[^"#]*)"', lambda m: f'href="{LINKS.get(m.group(1), m.group(1))}"', x)

# Header tweaks: the Industries top item opens the homepage industries section


MENU = {'home': '>Home<', 'services': '>Our Services', 'industries': '>Industries We Help', 'about': '>About Us', 'resources': '>Resources'}

def header(cur):
    h = HEADER
    if cur == 'home':
        h = h.replace('class="hlink" data-key="home"', 'class="hlink is-cur" aria-current="page" data-key="home"', 1)
    elif cur:
        h = re.sub(r'class="(mega(?: mega--sm)?)" data-mega data-key="' + cur + '"',
                   lambda m: f'class="{m.group(1)} is-cur" data-mega data-key="{cur}"', h, count=1)
    return h

def page(fname, title, desc, body, cur=None, css=('main', 'sections', 'pages'), body_cls='inner'):
    css_links = '\n'.join(f'  <link rel="stylesheet" href="assets/css/{c}.css">' for c in css)
    doc = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
  <meta name="theme-color" content="#073B36">
  <link rel="icon" href="assets/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{E(title)}">
  <meta property="og:description" content="{E(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
{css_links}
  <script src="assets/js/main.js" defer></script>
</head>
<body class="page-{body_cls}">
<a class="skip" href="#main">Skip to content</a>

{header(cur)}

<main id="main">
{body}
</main>

{FOOTER}
</body>
</html>
'''
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(map_links(doc))
    return fname

# ------------------------------------------------------------------ shared components
def hl_last(t):
    parts = t.rsplit(' ', 1)
    return f'{parts[0]} <span class="hl">{parts[1]}</span>' if len(parts) == 2 else f'<span class="hl">{t}</span>'

def hero(title_html, crumbs, sub, chips=None, cls='', extra=''):
    cr = []
    for k, (label, href) in enumerate(crumbs):
        if k: cr.append(CHEV)
        cr.append(f'<a href="{href}">{E(label)}</a>' if href else f'<span aria-current="page">{E(label)}</span>')
    ch = ''
    if chips:
        ch = '<div class="phero__chips">' + ''.join(f'<span>{c}</span>' for c in chips) + '</div>'
    return f'''<section class="s-hero s-hero--page" id="top">
  <div class="hero hero--page {cls}">
    <div class="deco hero__aura" aria-hidden="true"></div>
    <div class="deco hero__ring" aria-hidden="true"></div>
    <div class="deco hero__grid hero__grid--tl" aria-hidden="true"><i></i><i></i></div>
    <div class="deco hero__grid hero__grid--br" aria-hidden="true"><i></i><i></i></div>
    <div class="hero__in">
      <nav class="crumbs" aria-label="Breadcrumb">{''.join(cr)}</nav>
      <h1>{title_html}</h1>
      <p class="hero__sub">{sub}</p>
      {ch}{extra}
    </div>
  </div>
</section>'''

def head(tag, h2, lede=None, cls='head--c', right=None):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ''
    if cls == 'head--row':
        r = right if right is not None else lede_html
        return f'''<div class="head head--row rv">
      <div class="head__t"><span class="tag">{tag}</span><h2 class="h2">{h2}</h2></div>
      {r}
    </div>'''
    return f'''<div class="head {cls} rv"><span class="tag">{tag}</span><h2 class="h2">{h2}</h2>{lede_html}</div>'''

def more(label, href):
    return f'<a class="more" href="{href}">{label} <i>{ARROW}</i></a>'

def btn(label, href, kind='g', tag='a', extra=''):
    if tag == 'button':
        return f'<button class="btn btn--{kind}" type="submit"{extra}>{label} <i>{ARROW}</i></button>'
    return f'<a class="btn btn--{kind}" href="{href}"{extra}>{label} <i>{ARROW}</i></a>'

def acc(faqs, first_open=True):
    out = []
    for k, (q, a) in enumerate(faqs):
        on = k == 0 and first_open
        out.append(f'''<div class="acc__i{' on' if on else ''}">
          <button class="acc__q" type="button" aria-expanded="{'true' if on else 'false'}">{E(q)}
            <span class="acc__s" aria-hidden="true">{PLUS}</span></button>
          <div class="acc__a"><div><p>{E(a)}</p></div></div>
        </div>''')
    return '<div class="acc">' + ''.join(out) + '</div>'

def side_cta(topic):
    return f'''<div class="side__cta">
        <div class="deco" aria-hidden="true"></div>
        <h3>Need help with {E(topic)}?</h3>
        <p>Get a free audit of your account, tracking and landing pages. No obligation.</p>
        {btn('Get a Free Audit', '/free-audit/')}
        <div class="side__phone"><i>{icon('phone')}</i><span><small>Call us</small><b>{PHONE}</b></span></div>
      </div>'''

def svc_href(slug): return f'{slug}.html'
def nav_name(s): return s.get('nav', s['title'])

SIDE_IMGS = ['1522071820081-009f0129c71c', '1553877522-43269d4ea984', '1600880292203-757bb62b4baf',
             '1542744173-8e7e53415bb0', '1521737604893-d14cc237f11d', '1551836022-d5d88e9218df']

# ================================================================== SERVICE + INDUSTRY DETAIL
def detail(item, kind):
    is_svc = kind == 'service'
    title = item['title']; name = nav_name(item) if is_svc else title
    parent = BY_SLUG.get(item.get('parent')) if is_svc else None

    if is_svc:
        crumbs = [('Home', 'index.html'), ('Services', 'services.html')]
        if parent: crumbs.append((parent['title'], svc_href(parent['slug'])))
        crumbs.append((title, None))
        h1 = hl_last(title)
    else:
        crumbs = [('Home', 'index.html'), ('Industries', 'index.html#industries'), (title, None)]
        h1 = f'{E(title)} <span class="hl">Marketing</span>'

    chips = [f'<b>Free</b> audit included', '<b>Month-to-month</b> contracts', '<b>Weekly</b> ROI reporting']
    top = hero(h1, crumbs, E(item['short']), chips)

    # ---- sidebar navigation
    if is_svc:
        cur_parent = parent['slug'] if parent else item['slug']
        links = []
        for p in PARENTS:
            on = ' class="on"' if p['slug'] == item['slug'] else ''
            links.append(f'<a href="{svc_href(p["slug"])}"{on}>{E(p["title"])} {CHEV}</a>')
            if p['slug'] == cur_parent and p.get('children'):
                subs = ''.join(f'<a href="{svc_href(c)}"{" class=\"on\"" if c == item["slug"] else ""}>{E(nav_name(BY_SLUG[c]))}</a>' for c in p['children'])
                links.append(f'<div class="snav__sub">{subs}</div>')
        nav_box = f'<div class="side__box"><h3 class="side__t">All Services</h3><nav class="snav" aria-label="Services">{"".join(links)}</nav></div>'
    else:
        links = ''.join(f'<a href="{i["slug"]}.html"{" class=\"on\"" if i["slug"] == item["slug"] else ""}>{E(i["title"])} {CHEV}</a>' for i in INDUSTRIES)
        nav_box = f'<div class="side__box"><h3 class="side__t">Industries We Help</h3><nav class="snav" aria-label="Industries">{links}</nav></div>'

    # ---- what's included
    if is_svc and item.get('children'):
        cards = ''.join(f'''<a class="incl__c" href="{svc_href(c)}">
            <span class="incl__ic">{icon(BY_SLUG[c]['icon'])}</span>
            <div><h3>{E(nav_name(BY_SLUG[c]))}</h3><p>{E(BY_SLUG[c]['short'])}</p>{more('Learn more', svc_href(c)).replace('<a class="more" href', '<span class="more" data-href').replace('</a>', '</span>')}</div>
          </a>''' for c in item['children'])
        incl_tag, incl_h = 'Our Specialisms', f'{E(title)} <em>Services</em>'
    else:
        cards = ''.join(f'''<div class="incl__c">
            <span class="incl__ic">{icon(ic)}</span>
            <div><h3>{E(t)}</h3><p>{E(d)}</p></div>
          </div>''' for ic, t, d in item['features'])
        incl_tag = "What's Included" if is_svc else 'What We Do'
        incl_h = "What's <em>Included</em>" if is_svc else f'What We Run for <em>{E(title)}</em>'

    # ---- stats
    stats = list(STATS)
    if not is_svc and item.get('case'):
        c = item['case']; stats = [(c[1], f'{c[2]} — {c[0]}')] + stats[:2]
    kst = ''.join(f'<div class="kstat"><b class="num">{E(v)}</b><span>{E(l)}</span></div>' for v, l in stats)

    why = ''.join(f'<li>{E(w)}</li>' for w in item['why'])
    steps = ''.join(f'<div class="mstep"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in STEPS)
    idx = (SERVICES.index(item) if is_svc else INDUSTRIES.index(item))
    split_img = item.get('img2') or SIDE_IMGS[idx % len(SIDE_IMGS)]
    paras = ''.join(f'<p>{E(p)}</p>' for p in item['overview'])

    main = f'''<section class="s-detail sec">
  <div class="wrap sdet">
    <div class="sdet__main">
      <figure class="sdet__fig rv" style="margin:0">
        <img src="{U(item['img'], 1200)}" alt="{E(title)}" loading="eager">
        <figcaption class="sdet__badge"><i>{icon(item['icon'])}</i><span><b>{E(name)}</b><small>{'Managed by PPC Birds specialists' if is_svc else 'Industry specialists'}</small></span></figcaption>
      </figure>

      <div class="sblock rv">
        <span class="tag">Overview</span>
        <h2 style="margin-top:16px">{'Built Around the Numbers That Matter' if is_svc else f'Advertising for {E(title)}, Done Right'}</h2>
        <div class="prose" style="margin-top:16px">{paras}</div>
      </div>

      <div class="kstats rv">{kst}</div>

      <div class="sblock rv">
        <span class="tag">{incl_tag}</span>
        <h2 style="margin-top:16px">{incl_h}</h2>
        <div class="incl">{cards}</div>
      </div>

      <div class="ssplit rv">
        <img src="{U(split_img, 800)}" alt="" loading="lazy">
        <div>
          <span class="tag">Why PPC Birds</span>
          <h2 style="margin-top:14px">Why Choose Us for {E(name)}</h2>
          <p>Specialists who manage ads, tracking and landing pages together, so nothing falls between teams.</p>
          <div class="prose"><ul>{why}</ul></div>
        </div>
      </div>

      <div class="sblock rv">
        <span class="tag">How We Work</span>
        <h2 style="margin-top:16px">Our Proven <em>Process</em></h2>
        <div class="msteps">{steps}</div>
      </div>

      <div class="sblock rv">
        <span class="tag">FAQ</span>
        <h2 style="margin-top:16px">Common <em>Questions</em></h2>
        {acc(item['faqs'])}
      </div>
    </div>

    <aside class="side" aria-label="Sidebar">
      {nav_box}
      {side_cta(name)}
    </aside>
  </div>
</section>'''

    # ---- related
    if is_svc:
        pool = []
        if parent: pool += [c for c in parent['children'] if c != item['slug']]
        if item.get('children'): pool += []
        pool += [p['slug'] for p in PARENTS if p['slug'] not in (item['slug'], item.get('parent'))]
        rel = [BY_SLUG[s] for s in pool[:3]]
        rel_tag, rel_h = 'Related Services', 'Explore More <em>Services</em>'
    else:
        rel = [BY_SLUG[s] for s in item['services']]
        rel_tag, rel_h = 'Services We Use', f'How We Grow <em>{E(title)}</em> Businesses'
    rel_cards = ''.join(f'''<article class="rel rv">
        <span class="rel__ic">{icon(r['icon'])}</span>
        <h3><a href="{svc_href(r['slug'])}">{E(nav_name(r))}</a></h3>
        <p>{E(r['short'])}</p>
        {more('Learn more', svc_href(r['slug']))}
      </article>''' for r in rel)
    related = f'''<section class="s-related sec sec--tint">
  <div class="wrap">
    {head(rel_tag, rel_h, cls='head--row', right=btn('All Services', 'services.html', 'o'))}
    <div class="related">{rel_cards}</div>
  </div>
</section>'''

    body = '\n\n'.join([top, main, related, TMARQ, CTA])
    fname = f"{item['slug']}.html"
    desc = item['short']
    page_title = f"{title} — PPC Birds" if is_svc else f"{title} Marketing & Google Ads — PPC Birds"
    return page(fname, page_title, desc, body, cur='services' if is_svc else 'industries', body_cls=kind)

# ================================================================== ABOUT
def about():
    top = hero('About <span class="hl">Us</span>', [('Home', 'index.html'), ('About Us', None)],
               'A full-service digital marketing agency specializing in paid advertising, web development and conversion optimization.',
               ['<b>350+</b> happy clients', '<b>4.9★</b> average rating', '<b>$10M+</b> ad spend managed'])
    intro = f'''<section class="s-abi sec">
  <div class="wrap abi">
    <div class="abi__media rv">
      <img class="abi__a" src="{U('1522071820081-009f0129c71c', 800)}" alt="The PPC Birds team" loading="lazy">
      <div class="abi__rev"><b class="num" data-count="350" data-suffix="+">350+</b><span>Happy clients</span><span class="stars" aria-label="Rated 4.9 out of 5">★★★★★</span><span>4.9/5 average rating</span></div>
      <img class="abi__b" src="{U('1552664730-d307ca884978', 600)}" alt="" loading="lazy">
    </div>
    <div class="abi__body rv">
      <span class="tag">About PPC Birds</span>
      <h2 class="h2">Dedicated to Growing Your Business With <em>Paid Media</em></h2>
      <p class="lede">We help businesses fly beyond limits with data-driven advertising. Paid search, paid social, conversion tracking and the websites that carry the traffic, all managed by one team and measured against your revenue.</p>
      <div class="abi__nums">
        <div class="abi__num"><small>Brands scaled</small><b class="num" data-count="50" data-suffix="+">50+</b></div>
        <div class="abi__num"><small>Client retention</small><b class="num" data-count="94" data-suffix="%">94%</b></div>
      </div>
      <ul class="who__checks">
        <li>{icon('check')}Paid search, social and tracking under one roof</li>
        <li>{icon('check')}Transparent weekly reporting and live dashboards</li>
        <li>{icon('check')}A named account manager for every client</li>
      </ul>
      {btn('Contact Us Now', '/contact/')}
    </div>
  </div>
</section>'''
    approach = f'''<section class="s-approach sec sec--tint">
  <div class="wrap">
    {head('Our Approach', 'Our Proven Growth <em>Approach</em>', 'From discovery to execution, we follow a collaborative process that turns ad spend into sustainable growth.')}
    <div class="appr">
      <article class="appr__c appr__c--big rv">
        <span class="appr__ic">{icon('chart')}</span>
        <h3>Data-Driven Strategy</h3>
        <p>We analyze your business goals, audience behaviour and market opportunities to build a strong foundation before a single dollar is spent.</p>
        <div class="bar"><div class="bar__top"><span>Client retention</span><span>94%</span></div><div class="bar__track"><div class="bar__fill"></div></div></div>
      </article>
      <article class="appr__c rv">
        <span class="appr__ic">{icon('target')}</span>
        <h3>Outcome-Oriented Execution</h3>
        <p>Every campaign is measured on leads, sales and cost per result, not clicks or impressions.</p>
      </article>
      <article class="appr__c rv">
        <span class="appr__ic">{icon('refresh')}</span>
        <h3>Weekly Optimization</h3>
        <p>Search terms, bids, creative and landing pages reviewed every week, with a report you can read in five minutes.</p>
      </article>
    </div>
    <p class="svc__foot rv"><b>Free</b> Let's make something great work together. <a href="/free-audit/">Get a free audit</a></p>
  </div>
</section>'''
    roles = [('Paid Search Lead', 'Google, Microsoft and ChatGPT ads', '1560250097-0b93528c311a'),
             ('Paid Social Lead', 'Meta and TikTok campaigns and creative', '1573497019940-1c28c88b4f3e'),
             ('Tracking & Analytics Lead', 'GA4, server-side and call tracking', '1519085360753-af0119f7cbe7'),
             ('Web & CRO Lead', 'Websites, landing pages and testing', '1573496359142-b8d87734a5a2')]
    li = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.9 8.9V20H3.6V8.9zM5.25 3.6A1.9 1.9 0 1 1 5.2 7.4a1.9 1.9 0 0 1 .05-3.8M20.4 20h-3.3v-5.6c0-1.4-.5-2.3-1.7-2.3-.9 0-1.45.6-1.7 1.2-.1.2-.1.55-.1.9V20H10.1V8.9h3.3v1.45a3.3 3.3 0 0 1 3-1.65c2.2 0 4 1.45 4 4.55z"/></svg>'
    team_cards = ''.join(f'''<article class="tm rv">
        <img src="{U(img, 600, 750)}" alt="" loading="lazy">
        <div class="tm__b"><h3>{E(r)}</h3><p>{E(d)}</p><div class="tm__soc"><a href="#" aria-label="LinkedIn">{li}</a><a href="mailto:{EMAIL}" aria-label="Email">{icon('mail')}</a></div></div>
      </article>''' for r, d, img in roles)
    team = f'''<section class="s-team sec">
  <div class="wrap">
    {head('Our Team', 'The Specialists Behind Your <em>Campaigns</em>', cls='head--row', right='<p class="lede">Every account gets a strategist, a tracking specialist and a web lead, coordinated by one named account manager.</p>')}
    <div class="team">{team_cards}</div>
  </div>
</section>'''
    body = '\n\n'.join([top, intro, approach, team, FLOW.replace('class="s-flow sec"', 'class="s-flow sec sec--tint"'),
                        BENTO.replace('class="s-impact sec sec--tint"', 'class="s-impact sec"'), TMARQ, CTA])
    return page('about.html', 'About Us — PPC Birds', 'Meet PPC Birds, a full-service digital marketing agency specializing in paid advertising, web development and conversion optimization.', body, cur='about', body_cls='about')

# ================================================================== CONTACT
def service_options():
    opts = ['<option value="">Select a service</option>']
    for p in PARENTS: opts.append(f'<option>{E(p["title"])}</option>')
    opts.append('<option>Not sure yet</option>')
    return ''.join(opts)

def contact():
    top = hero('Contact <span class="hl">Us</span>', [('Home', 'index.html'), ('Contact Us', None)],
               'Have a project in mind? Tell us about your business and we will reply within one working day.')
    soc = FOOTER[FOOTER.index('<div class="fsoc">'):FOOTER.index('</div>', FOOTER.index('<div class="fsoc">')) + 6]
    sec = f'''<section class="s-contact sec">
  <div class="wrap">
    {head('Get In Touch', "Let's Grow Your Business <em>Together</em>")}
    <div class="cgrid">
      <div class="cinfo rv">
        <div class="deco" aria-hidden="true"></div>
        <h2>Contact Information</h2>
        <p>Have a project in mind? Get in touch with our team to discuss your goals, and we'll help turn them into a clear plan.</p>
        <div class="crow"><i>{icon('phone')}</i><span><small>Phone Number</small><b>{PHONE}</b></span></div>
        <div class="crow"><i>{icon('mail')}</i><span><small>Email Address</small><b>{EMAIL}</b></span></div>
        <div class="crow"><i>{icon('clock')}</i><span><small>Working Hours</small><b>Mon–Fri, 9:00–18:00</b></span></div>
        {soc}
      </div>
      <div class="cform rv">
        <h2>Send Us a Message</h2>
        <p>Fill in the form and a strategist will get back to you within one working day.</p>
        <form class="form js-form" novalidate>
          <div class="fld"><label for="c-first">First name <i>*</i></label><input id="c-first" name="first_name" type="text" autocomplete="given-name" placeholder="Jane" required></div>
          <div class="fld"><label for="c-last">Last name <i>*</i></label><input id="c-last" name="last_name" type="text" autocomplete="family-name" placeholder="Doe" required></div>
          <div class="fld"><label for="c-email">Email address <i>*</i></label><input id="c-email" name="email" type="email" autocomplete="email" placeholder="jane@company.com" required></div>
          <div class="fld"><label for="c-phone">Phone number</label><input id="c-phone" name="phone" type="tel" autocomplete="tel" placeholder="+1 555 000 1234"></div>
          <div class="fld"><label for="c-service">Service you need</label><select id="c-service" name="service">{service_options()}</select></div>
          <div class="fld"><label for="c-budget">Monthly ad budget</label><select id="c-budget" name="budget"><option value="">Select a range</option><option>Under $2,000</option><option>$2,000 – $10,000</option><option>$10,000 – $50,000</option><option>$50,000+</option><option>Not running ads yet</option></select></div>
          <div class="fld fld--full"><label for="c-msg">Your message <i>*</i></label><textarea id="c-msg" name="message" placeholder="Tell us about your business and what you'd like to improve." required></textarea></div>
          <div class="form__foot">
            {btn('Send Message', '', 'g', 'button')}
            <span class="form__note">{icon('lock')}We never share your details.</span>
          </div>
          <p class="form__ok" role="status">{icon('check')}Thanks! Your message is ready to send. Connect this form to your form plugin to go live.</p>
        </form>
      </div>
    </div>
  </div>
</section>'''
    nx = [('Step 01', 'We review your message', 'A strategist reads your enquiry and looks at your website and current ads.', 'Within 1 working day'),
          ('Step 02', 'Free audit call', 'A short call to understand your goals and walk through what we found.', '30 minutes'),
          ('Step 03', 'Your action plan', 'A clear plan with priorities, budget and expected timeline. No obligation.', 'Within 1 week')]
    nexts = ''.join(f'<article class="nx rv"><span class="nx__n">{a}</span><h3>{E(b)}</h3><p>{E(c)}</p><span class="nx__t">{icon("clock")}{E(d)}</span></article>' for a, b, c, d in nx)
    nxt = f'''<section class="s-next sec sec--tint">
  <div class="wrap">
    {head('What Happens Next', 'From First Message to <em>Action Plan</em>', 'No sales scripts and no long-term contracts. Here is exactly what to expect after you get in touch.')}
    <div class="nexts">{nexts}</div>
  </div>
</section>'''
    body = '\n\n'.join([top, sec, nxt, HOME_FAQ])
    return page('contact.html', 'Contact Us — PPC Birds', 'Get in touch with PPC Birds. Tell us about your business and get a reply within one working day.', body, cur='about', body_cls='contact')

# ================================================================== BLOG
CATS = []
for p in POSTS:
    if p['cat'] not in CATS: CATS.append(p['cat'])
def cat_key(c): return re.sub(r'[^a-z]+', '-', c.lower()).strip('-')

def post_card(p, extra_cls=''):
    return f'''<article class="post rv{extra_cls}" data-cat="{cat_key(p['cat'])}">
        <div class="post__media"><img src="{U(p['img'], 800)}" alt="" loading="lazy"><span class="post__cat">{E(p['cat'])}</span></div>
        <div class="post__b">
          <div class="post__meta"><span>{icon('calendar')}{E(p['date'])}</span><span>{icon('clock')}{E(p['read'])}</span></div>
          <h3><a href="{p['slug']}.html">{E(p['title'])}</a></h3>
          {more('Read More', p['slug'] + '.html')}
        </div>
      </article>'''

def blog():
    top = hero('Our <span class="hl">Blog</span>', [('Home', 'index.html'), ('Blog', None)],
               'Playbooks, teardowns and tracking guides from the team running the accounts.')
    chips = '<button class="fchip on" type="button" data-f="all">All Posts</button>' + ''.join(
        f'<button class="fchip" type="button" data-f="{cat_key(c)}">{E(c)}</button>' for c in CATS)
    lead_p = POSTS[0]
    lead = f'''<article class="lead post rv" data-cat="{cat_key(lead_p['cat'])}">
        <div class="lead__media"><img src="{U(lead_p['img'], 1000)}" alt="" loading="eager"></div>
        <div class="lead__b">
          <span class="post__cat">Featured · {E(lead_p['cat'])}</span>
          <h2><a href="{lead_p['slug']}.html">{E(lead_p['title'])}</a></h2>
          <p>{E(lead_p['excerpt'])}</p>
          <div class="post__meta"><span>{icon('calendar')}{E(lead_p['date'])}</span><span>{icon('clock')}{E(lead_p['read'])}</span></div>
          {btn('Read Article', lead_p['slug'] + '.html')}
        </div>
      </article>'''
    grid = ''.join(post_card(p) for p in POSTS[1:])
    sec = f'''<section class="s-bloglist sec">
  <div class="wrap" data-filter>
    <div class="fbar-chips rv" role="toolbar" aria-label="Filter posts by category">{chips}</div>
    {lead}
    <div class="posts">{grid}</div>
    <p class="empty" data-empty>No posts in this category yet.</p>
  </div>
</section>'''
    body = '\n\n'.join([top, sec, CTA])
    return page('blog.html', 'Blog — PPC Birds', 'PPC, paid social, tracking and conversion guides from the PPC Birds team.', body, cur='resources', body_cls='blog')

def article(p):
    k = POSTS.index(p)
    prev_p = POSTS[k - 1] if k > 0 else None
    next_p = POSTS[k + 1] if k + 1 < len(POSTS) else None
    meta = f'''<div class="pmeta"><span>{icon('calendar')}{E(p['date'])}</span><span>{icon('folder')}{E(p['cat'])}</span><span>{icon('clock')}{E(p['read'])}</span><span>{icon('user')}PPC Birds</span></div>'''
    top = hero(E(p['title']), [('Home', 'index.html'), ('Blog', 'blog.html'), (p['cat'], None)], E(p['excerpt']), cls='hero--post', extra=meta)
    tags = ''.join(f'<a href="blog.html">{E(t)}</a>' for t in p['tags'])
    share = ''.join(f'<a href="#" aria-label="Share on {n}">{svg}</a>' for n, svg in [
        ('Facebook', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.25-1.5 1.55-1.5h1.65V4.6c-.3 0-1.3-.1-2.45-.1-2.4 0-4.05 1.5-4.05 4.2v2.2H7.5V14h2.7v8z"/></svg>'),
        ('LinkedIn', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.9 8.9V20H3.6V8.9zM5.25 3.6A1.9 1.9 0 1 1 5.2 7.4a1.9 1.9 0 0 1 .05-3.8M20.4 20h-3.3v-5.6c0-1.4-.5-2.3-1.7-2.3-.9 0-1.45.6-1.7 1.2-.1.2-.1.55-.1.9V20H10.1V8.9h3.3v1.45a3.3 3.3 0 0 1 3-1.65c2.2 0 4 1.45 4 4.55z"/></svg>'),
        ('X', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 3h3.2l-7 8 8.2 10h-6.4l-5-6.1L4.7 21H1.5l7.5-8.6L1.1 3h6.6l4.5 5.6zm-1.1 16h1.8L7.7 4.9H5.8z"/></svg>')])
    pnav = '<nav class="pnav" aria-label="More posts">'
    pnav += f'<a href="{prev_p["slug"]}.html"><small>← Previous</small><b>{E(prev_p["title"])}</b></a>' if prev_p else '<span></span>'
    pnav += f'<a href="{next_p["slug"]}.html"><small>Next →</small><b>{E(next_p["title"])}</b></a>' if next_p else '<span></span>'
    pnav += '</nav>'
    counts = {c: sum(1 for x in POSTS if x['cat'] == c) for c in CATS}
    cats = ''.join(f'<a href="blog.html">{E(c)}<span>{n}</span></a>' for c, n in counts.items())
    recent = ''.join(f'<a href="{x["slug"]}.html"><img src="{U(x["img"], 160, 160)}" alt="" loading="lazy"><span><small>{E(x["date"])}</small><b>{E(x["title"])}</b></span></a>'
                     for x in [y for y in POSTS if y is not p][:3])
    logo = '<img src="assets/img/logo-mark-white-128.png" alt="" width="44" height="44">'
    main = f'''<section class="s-article sec">
  <div class="wrap art">
    <article class="art__main">
      <figure class="art__fig" style="margin:0 0 36px"><img src="{U(p['img'], 1200)}" alt="" loading="eager"></figure>
      <div class="prose">{p['body']}</div>
      <div class="art__foot">
        <div class="tags"><b>Tags:</b>{tags}</div>
        <div class="share"><b>Share:</b>{share}</div>
      </div>
      <div class="author"><span class="author__av">{logo}</span><div><b>PPC Birds Team</b><p>Paid media, tracking and web specialists sharing what we learn from running real accounts every week.</p></div></div>
      {pnav}
      <div class="reply">
        <h2>Leave a Reply</h2>
        <p>Your email address will not be published. Required fields are marked <span style="color:var(--g500)">*</span></p>
        <form class="form js-form" novalidate>
          <div class="fld fld--full"><label for="r-comment">Comment <i>*</i></label><textarea id="r-comment" name="comment" required></textarea></div>
          <div class="fld"><label for="r-name">Name <i>*</i></label><input id="r-name" name="author" type="text" autocomplete="name" required></div>
          <div class="fld"><label for="r-email">Email <i>*</i></label><input id="r-email" name="email" type="email" autocomplete="email" required></div>
          <div class="fld fld--full"><label for="r-url">Website</label><input id="r-url" name="url" type="url" autocomplete="url" placeholder="https://"></div>
          <div class="fld fld--full"><label class="chip"><input id="r-save" type="checkbox" name="save"><span>Save my name, email and website in this browser for the next time I comment.</span></label></div>
          <div class="form__foot">{btn('Post Comment', '', 'g', 'button')}</div>
          <p class="form__ok" role="status">{icon('check')}Thanks! Comments are handled by WordPress once the theme is live.</p>
        </form>
      </div>
    </article>
    <aside class="side" aria-label="Sidebar">
      <div class="side__box swidget"><h3 class="side__t">Search</h3><form role="search" action="blog.html"><input id="s-q" type="search" name="s" placeholder="Search articles" aria-label="Search articles"><button type="submit" aria-label="Search">{icon('search')}</button></form></div>
      <div class="side__box"><h3 class="side__t">Categories</h3><div class="cats">{cats}</div></div>
      <div class="side__box"><h3 class="side__t">Recent Posts</h3><div class="recent">{recent}</div></div>
      {side_cta('your ads')}
    </aside>
  </div>
</section>'''
    rel = ''.join(post_card(x) for x in [y for y in POSTS if y is not p][:3])
    related = f'''<section class="s-relposts sec sec--tint">
  <div class="wrap">
    {head('Keep Reading', 'Related <em>Articles</em>', cls='head--row', right=btn('View All Posts', 'blog.html', 'o'))}
    <div class="posts">{rel}</div>
  </div>
</section>'''
    body = '\n\n'.join([top, main, related, CTA])
    return page(f"{p['slug']}.html", f"{p['title']} — PPC Birds", p['excerpt'], body, cur='resources', body_cls='single')

# ================================================================== PORTFOLIO
def portfolio():
    top = hero('Our <span class="hl">Portfolio</span>', [('Home', 'index.html'), ('Portfolio', None)],
               'Real accounts, real numbers. A selection of results from campaigns, tracking and websites we manage.')
    filt = [('all', 'All Work'), ('ecommerce', 'Ecommerce'), ('healthcare', 'Healthcare'), ('b2b', 'B2B'), ('google', 'Google Ads'), ('social', 'Social Ads'), ('web', 'Websites')]
    chips = ''.join(f'<button class="fchip{" on" if k == "all" else ""}" type="button" data-f="{k}">{E(l)}</button>' for k, l in filt)
    cards = []
    for c in CASES:
        tags = ''.join(f'<span>{E(t)}</span>' for t in c['tags'])
        m = ''.join(f'<div><b class="num">{E(v)}</b><span>{E(l)}</span></div>' for v, l in c['metrics'])
        q = f'<p class="pfc__q">“{E(c["quote"][0])}”<small>{E(c["quote"][1])}</small></p>' if c['quote'] else ''
        cards.append(f'''<article class="pfc rv" data-cat="{' '.join(c['cats'])}">
        <div class="pfc__media"><img src="{U(c['img'], 1000)}" alt="" loading="lazy"><div class="pfc__tags">{tags}</div></div>
        <div class="pfc__b"><h3>{E(c['name'])}</h3><p>{E(c['summary'])}</p><div class="pfc__m">{m}</div>{q}{more('Discuss a similar project', '/contact/')}</div>
      </article>''')
    sec = f'''<section class="s-portfolio sec">
  <div class="wrap" data-filter>
    {head('Case Studies', "Results We've <em>Delivered</em>", cls='head--row', right='<p class="lede">Every number below comes from a live client account managed by PPC Birds.</p>')}
    <div class="fbar-chips rv" role="toolbar" aria-label="Filter case studies">{chips}</div>
    <div class="pf">{''.join(cards)}</div>
    <p class="empty" data-empty>No case studies in this category yet.</p>
  </div>
</section>'''
    strip = f'''<section class="s-rstrip sec sec--tint">
  <div class="wrap">
    <div class="rstrip rv">
      <div><b class="num" data-count="10" data-prefix="$" data-suffix="M+">$10M+</b><span>Ad spend managed</span></div>
      <div><b class="num" data-count="350" data-suffix="+">350+</b><span>Happy clients</span></div>
      <div><b class="num" data-count="94" data-suffix="%">94%</b><span>Retention rate</span></div>
      <div><b class="num" data-count="4.9" data-dec="1" data-suffix="/5">4.9/5</b><span>Average rating</span></div>
    </div>
  </div>
</section>'''
    body = '\n\n'.join([top, sec, strip, TMARQ, CTA])
    return page('portfolio.html', 'Portfolio & Results — PPC Birds', 'Case studies and results from PPC Birds clients across ecommerce, healthcare and B2B.', body, cur='resources', body_cls='portfolio')

# ================================================================== FAQ
def faq():
    top = hero('Frequently Asked <span class="hl">Questions</span>', [('Home', 'index.html'), ('FAQ', None)],
               'Straight answers about how we work, what we charge and what to expect.')
    nav = ''.join(f'<a href="#faq-{k}"{" class=\"on\"" if n == 0 else ""}>{icon(ic)}{E(t)}</a>' for n, (k, t, ic, _) in enumerate(FAQ_GROUPS))
    groups = ''.join(f'''<div class="faqp__grp rv" id="faq-{k}"><h2>{E(t)} <span>{len(items)}</span></h2>{acc(items, first_open=(n == 0))}</div>'''
                     for n, (k, t, ic, items) in enumerate(FAQ_GROUPS))
    sec = f'''<section class="s-faqpage sec">
  <div class="wrap faqp">
    <div>
      <nav class="faqp__nav" aria-label="FAQ topics" data-spy>{nav}</nav>
      <div class="help" style="margin-top:22px">
        <h3>Still have questions?</h3>
        <p>Talk to a strategist about your account, free of charge.</p>
        <div class="help__row">
          <div class="help__chip"><i>{icon('mail')}</i><span><small>Email us</small><b>{EMAIL}</b></span></div>
          <div class="help__chip"><i>{icon('phone')}</i><span><small>Call us</small><b>{PHONE}</b></span></div>
        </div>
      </div>
    </div>
    <div class="faqp__main">{groups}</div>
  </div>
</section>'''
    body = '\n\n'.join([top, sec, CTA])
    return page('faq.html', 'FAQ — PPC Birds', 'Answers to common questions about PPC Birds pricing, contracts, ads, tracking and websites.', body, cur='resources', body_cls='faq')

# ================================================================== FREE AUDIT
def free_audit():
    top = hero('Get a Free <span class="hl">Audit</span>', [('Home', 'index.html'), ('Free Audit', None)],
               'We review your ad accounts, tracking and landing pages, then send a prioritised list of fixes. Free, with no obligation.',
               ['<b>Free</b> no obligation', '<b>1 working day</b> reply', '<b>Action plan</b> included'])
    items = [('search', 'Ad Account Review', 'Structure, keywords, search terms, bidding and wasted spend.'),
             ('target', 'Tracking Check', 'Are your conversions, calls and forms counted correctly?'),
             ('layout', 'Landing Page Review', 'Speed, message match and conversion blockers.'),
             ('chart', 'Budget & Action Plan', 'Prioritised fixes and a recommended monthly budget.')]
    li = ''.join(f'<div class="aud__li"><span class="feat__ic">{icon(i)}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div></div>' for i, t, d in items)
    plats = ['Google Ads', 'Microsoft Ads', 'Meta Ads', 'TikTok Ads', 'ChatGPT Ads', 'Not running ads yet']
    chips = ''.join(f'<label class="chip"><input type="checkbox" name="platforms[]" value="{E(p)}" id="a-p{n}"><span>{E(p)}</span></label>' for n, p in enumerate(plats))
    sec = f'''<section class="s-audit sec">
  <div class="wrap aud">
    <div class="aud__l rv">
      <span class="tag">What You Get</span>
      <h2 class="h2">A Clear Plan to Lower Your <em>Cost Per Lead</em></h2>
      <p class="lede">A strategist reviews your account by hand. No automated reports and no sales pressure.</p>
      <div class="aud__list">{li}</div>
      <div class="aud__trust">
        <span class="faces" aria-hidden="true"><img src="{U('1494790108377-be9c29b29330', 96, 96)}" alt=""><img src="{U('1500648767791-00dcc994a43e', 96, 96)}" alt=""><img src="{U('1534528741775-53994a69daeb', 96, 96)}" alt=""></span>
        <div><b>4.9/5 <span class="stars" aria-hidden="true">★★★★★</span></b><small>Trusted by 350+ businesses</small></div>
      </div>
    </div>
    <div class="aud__form rv">
      <h2>Request Your Free Audit</h2>
      <p>Takes about two minutes. We reply within one working day.</p>
      <form class="form js-form" novalidate>
        <p class="aud__step">1 · About you</p>
        <div class="fld"><label for="a-name">Full name <i>*</i></label><input id="a-name" name="name" type="text" autocomplete="name" placeholder="Jane Doe" required></div>
        <div class="fld"><label for="a-company">Company</label><input id="a-company" name="company" type="text" autocomplete="organization" placeholder="Acme Dental"></div>
        <div class="fld"><label for="a-email">Email <i>*</i></label><input id="a-email" name="email" type="email" autocomplete="email" placeholder="jane@company.com" required></div>
        <div class="fld"><label for="a-phone">Phone</label><input id="a-phone" name="phone" type="tel" autocomplete="tel" placeholder="+1 555 000 1234"></div>
        <p class="aud__step">2 · Your marketing</p>
        <div class="fld fld--full"><label for="a-site">Website URL <i>*</i></label><input id="a-site" name="website" type="url" placeholder="https://yourwebsite.com" required></div>
        <fieldset class="fld fld--full"><legend>Where do you advertise today?</legend><div class="chips" style="margin-top:8px">{chips}</div></fieldset>
        <div class="fld"><label for="a-spend">Monthly ad spend</label><select id="a-spend" name="spend"><option value="">Select a range</option><option>Under $2,000</option><option>$2,000 – $10,000</option><option>$10,000 – $50,000</option><option>$50,000+</option></select></div>
        <div class="fld"><label for="a-service">Main interest</label><select id="a-service" name="service">{service_options()}</select></div>
        <div class="fld fld--full"><label for="a-goal">What's your biggest challenge right now?</label><textarea id="a-goal" name="goal" placeholder="e.g. Our cost per lead doubled this year and we don't know why."></textarea></div>
        <div class="form__foot">{btn('Request My Free Audit', '', 'g', 'button')}<span class="form__note">{icon('lock')}No obligation. We never share your details.</span></div>
        <p class="form__ok" role="status">{icon('check')}Thanks! Your audit request is ready. Connect this form to your form plugin or CRM to go live.</p>
      </form>
    </div>
  </div>
</section>'''
    body = '\n\n'.join([top, sec, TMARQ, HOME_FAQ.replace('class="s-faq sec"', 'class="s-faq sec sec--tint"')])
    return page('free-audit.html', 'Get a Free Audit — PPC Birds', 'Request a free audit of your ad accounts, tracking and landing pages from PPC Birds.', body, cur=None, body_cls='audit')

# ================================================================== LEGAL
LEGAL = {
 'privacy-policy': ('Privacy Policy', 'How PPC Birds collects, uses and protects your information.', [
   ('Information we collect', '<p>We collect information you give us directly, such as your name, email address, phone number, company and website when you fill in a form or contact us. We also collect technical information automatically, such as pages visited, device type and approximate location, through cookies and analytics tools.</p>'),
   ('How we use your information', '<ul><li>To respond to enquiries and provide our services</li><li>To prepare audits and proposals you request</li><li>To send updates you have subscribed to</li><li>To measure and improve our website and marketing</li></ul>'),
   ('Cookies and tracking', '<p>Our website uses cookies and similar technologies for analytics and advertising measurement, including tools from Google and Meta. You can control cookies through your browser settings and our consent banner where available.</p>'),
   ('Sharing your information', '<p>We do not sell your personal information. We share it only with service providers that help us operate our business, such as hosting, email and CRM providers, and when required by law.</p>'),
   ('Data retention', '<p>We keep personal information only as long as needed for the purposes described in this policy, or as required by law.</p>'),
   ('Your rights', '<p>Depending on where you live, you may have the right to access, correct, delete or restrict the use of your personal information. To make a request, contact us using the details below.</p>'),
   ('Security', '<p>We use reasonable technical and organizational measures to protect your information. No method of transmission over the internet is completely secure.</p>'),
   ('Contact us', f'<p>Questions about this policy? Email <strong>{EMAIL}</strong> or call <strong>{PHONE}</strong>.</p>')]),
 'terms': ('Terms of Service', 'The terms that apply when you use the PPC Birds website and services.', [
   ('Our services', '<p>PPC Birds provides digital marketing services including paid advertising management, conversion tracking, landing page design and website development. The specific scope of each engagement is set out in a proposal or agreement.</p>'),
   ('Fees and payment', '<p>Management fees are billed monthly in advance unless agreed otherwise. Fees are separate from advertising spend.</p>'),
   ('Advertising spend', '<p>Advertising spend is paid directly by you to the relevant platforms, such as Google, Microsoft, Meta or TikTok. You remain responsible for those charges.</p>'),
   ('Your responsibilities', '<ul><li>Provide accurate information and timely access to accounts</li><li>Make sure your products, services and claims comply with applicable laws and platform policies</li><li>Review and approve campaigns and content where requested</li></ul>'),
   ('Account ownership', '<p>Ad accounts, tracking containers and analytics properties are created or kept in your name. You retain ownership if our engagement ends.</p>'),
   ('Results', '<p>We work to improve your marketing results, but advertising performance depends on many factors outside our control, so specific outcomes cannot be guaranteed.</p>'),
   ('Cancellation', '<p>Our management plans run month to month and can be cancelled with 30 days’ written notice.</p>'),
   ('Changes to these terms', '<p>We may update these terms from time to time. The latest version will always be available on this page.</p>'),
   ('Contact us', f'<p>Questions about these terms? Email <strong>{EMAIL}</strong>.</p>')]),
}

def legal(slug):
    title, sub, secs = LEGAL[slug]
    top = hero(hl_last(title), [('Home', 'index.html'), (title, None)], E(sub))
    toc = ''.join(f'<li><a href="#s{n}">{E(t)}</a></li>' for n, (t, _) in enumerate(secs, 1))
    content = ''.join(f'<h2 id="s{n}">{n}. {E(t)}</h2>{b}' for n, (t, b) in enumerate(secs, 1))
    sec = f'''<section class="s-legal sec">
  <!-- Template text: have this reviewed by the client's legal advisor before launch. -->
  <div class="wrap legal">
    <nav class="toc" aria-label="On this page"><b>On this page</b><ol>{toc}</ol></nav>
    <div><span class="legal__upd">{icon('calendar')}Last updated: October 2026</span><div class="prose">{content}</div></div>
  </div>
</section>'''
    return page(f'{slug}.html', f'{title} — PPC Birds', sub, '\n\n'.join([top, sec]), cur=None, body_cls='legal')

# ================================================================== 404
def not_found():
    body = f'''<section class="s-hero s-hero--page" id="top">
  <div class="hero hero--page">
    <div class="deco hero__aura" aria-hidden="true"></div>
    <div class="deco hero__ring" aria-hidden="true"></div>
    <div class="deco hero__grid hero__grid--tl" aria-hidden="true"><i></i><i></i></div>
    <div class="deco hero__grid hero__grid--br" aria-hidden="true"><i></i><i></i></div>
    <div class="hero__in">
      <span class="nf__code" aria-hidden="true">404</span>
      <h1>This Page <span class="hl">Flew Away</span></h1>
      <p class="hero__sub">The page you are looking for has moved or no longer exists. Try one of these instead.</p>
      <div class="hero__act">{btn('Back to Home', 'index.html')}{btn('Contact Us', '/contact/', 'glass')}</div>
      <div class="nf__links"><a href="services.html">Services</a><a href="/about/">About</a><a href="/blog/">Blog</a><a href="/portfolio/">Portfolio</a><a href="/faq/">FAQ</a><a href="/free-audit/">Free Audit</a></div>
    </div>
  </div>
</section>'''
    return page('404.html', 'Page Not Found — PPC Birds', 'The page you are looking for could not be found.', body, cur=None, body_cls='404')

# ================================================================== home + services overview (approved; links mapped)
def home_and_services():
    page('index.html', 'PPC Birds — Data-Driven PPC & Digital Marketing Agency',
         'PPC Birds runs Google Ads, Meta and TikTok ads, conversion tracking and high-converting websites. Transparent reporting, measurable results.',
         HOME_MAIN, cur='home', css=('main', 'sections'), body_cls='home')
    page('services.html', 'Our Services — PPC Birds',
         'PPC management, social media ads, conversion and call tracking, landing pages and web development from PPC Birds.',
         SVC_MAIN, cur='services', css=('main', 'sections', 'pages'), body_cls='services')

if __name__ == '__main__':
    built = []
    home_and_services(); built += ['index.html', 'services.html']
    for s in SERVICES: built.append(detail(s, 'service'))
    for i in INDUSTRIES: built.append(detail(i, 'industry'))
    built += [about(), contact(), blog(), portfolio(), faq(), free_audit(), legal('privacy-policy'), legal('terms'), not_found()]
    for p in POSTS: built.append(article(p))
    # link check
    files = set(os.listdir(OUT))
    bad = set()
    for f in built:
        for h in re.findall(r'href="([^"]+)"', open(os.path.join(OUT, f), encoding='utf-8').read()):
            if h.startswith(('http', 'mailto:', 'tel:', '#')) or h.startswith('assets/'): continue
            target = h.split('#')[0]
            if target and target not in files: bad.add((f, h))
    print(f'Built {len(built)} pages')
    print('Broken internal links:', sorted(bad) if bad else 'none')
