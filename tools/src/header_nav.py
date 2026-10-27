# Generates the full-width header + mega menus (header.php).
# Structure follows the client's RightPath reference: full-bleed sticky bar,
# pill links, wide centred mega panels, phone block + CTA on the right.

B = 'assets/img/brands/'
ARROW = ('<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9 9 3M4.2 3H9v4.8" '
         'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CARET = ('<svg class="hcaret" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" '
         'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M21.5 16.9v2.6a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 0 0 1-6-6 19.6 19.6 0 0 1-3-8.6A2 2 0 0 1 3.8 1.7h2.6a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L7.5 9.6a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.8 2.1z"/></svg>')

def ic(paths):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{paths}</svg>')
I_LAYOUT = ic('<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9h18M9 21V9"/>')
I_GRID = ic('<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>')

# (group title, group href, [(label, href, logo file or None, icon svg, description)])
SERVICES = [
  [('PPC Management', '/ppc-management/', [
      ('Google Ads', '/ppc-management/google-ads-management/', 'google-ads.svg', 'Search, Shopping, PMax & YouTube'),
      ('Bing Ads', '/ppc-management/bing-ads/', 'microsoft-ads.svg', 'Microsoft Advertising at lower CPCs'),
      ('ChatGPT Ads', '/ppc-management/chatgpt-ads-management/', 'openai.svg', 'Ads inside AI assistants'),
   ]),
   ('Social Media Marketing', '/social-media-marketing/', [
      ('Meta Ads', '/social-media-marketing/meta-ads-management/', 'meta.svg', 'Facebook & Instagram campaigns'),
      ('TikTok Ads', '/social-media-marketing/tiktok-ads-management/', 'tiktok.svg', 'Native creative & Spark Ads'),
   ])],
  [('Conversion Tracking', '/conversion-tracking/', [
      ('Google Ads Conversions', '/conversion-tracking/enhanced-conversions/', 'google-ads.svg', 'Enhanced & offline conversions'),
      ('Meta Pixel & CAPI', '/conversion-tracking/meta-pixel-meta-capi/', 'meta.svg', 'Pixel + Conversions API'),
      ('Server-Side Tracking', '/conversion-tracking/server-side-tracking/', 'google-tag-manager.svg', 'Server-side Google Tag Manager'),
   ]),
   ('Call Tracking', '/call-tracking/', [
      ('CallTrackingMetrics', '/calltracking/calltrackingmetricssetup/', 'calltrackingmetrics.svg', 'Routing, scoring & attribution'),
      ('CallRail', '/call-tracking/callrail-setup/', 'callrail.svg', 'Know which ad made the phone ring'),
   ])],
  [('Web Design & Development', '/website-design-development/', [
      ('WordPress', '/website-design-development/wordpress', 'wordpress.svg', 'Custom themes & Elementor'),
      ('Wix', '/website-design-development/wix', 'wix.svg', 'Easy-to-edit business sites'),
      ('Squarespace', '/website-design-development/squarespace', 'squarespace.svg', 'Design-led websites'),
      ('GoDaddy', '/website-design-development/godaddy', 'godaddy.svg', 'Refresh or rebuild'),
      ('Shopify', '/website-design-development/shopify', 'shopify.svg', 'High-converting stores'),
   ]),
   ('Conversion', '/landing-page-design/', [
      ('Landing Page Design', '/landing-page-design/', None, 'One offer, one form, fast load'),
   ])],
]

INDUSTRIES = [
  ('Healthcare', '/industries/healthcare-google-ads/', 'Clinics, dental & medical practices',
   ic('<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>')),
  ('Mental Health', '/industries/mental-health-google-ads/', 'Therapists, counselors & centers',
   ic('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>')),
  ('Addiction Treatment', '/industries/addiction-treatment-google-ads/', 'Certified, compliant admissions',
   ic('<path d="M9 12l2 2 4-4"/><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6z"/>')),
  ('Ecommerce', '/industries/ecommerce-google-ads/', 'Shopping, PMax & social for stores',
   ic('<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.6 12.4a2 2 0 0 0 2 1.6h8.8a2 2 0 0 0 2-1.6L22 7H6"/>')),
  ('Home & Local Services', '/industries/home-and-local-services-google-ads/', 'LSAs & call-driven campaigns',
   ic('<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>')),
]

ABOUT = [
  ('About PPC Birds', '/about/', 'Who we are and how we work', ic('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M17 11a3 3 0 1 0-1-5.8M21.5 20a5.5 5.5 0 0 0-3.5-5"/>')),
  ('Results & Portfolio', '/portfolio/', 'Case studies with real numbers', ic('<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/>')),
  ('Contact', '/contact/', 'Talk to a strategist', ic('<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3.5 6.5 8.5 6 8.5-6"/>')),
]
RESOURCES = [
  ('Blog', '/blog/', 'Playbooks & tracking guides', ic('<path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h8M8 16h5"/>')),
  ('Portfolio', '/portfolio/', 'Client results by industry', ic('<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5H9l2 2.5h8.5A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>')),
  ('FAQ', '/faq/', 'Pricing, contracts & process', ic('<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"/>')),
  ('Free Audit', '/free-audit/', 'Get a prioritised fix list', ic('<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>')),
]

def logo_tile(logo, label):
    if logo:
        return f'<span class="mi__logo"><img src="{B}{logo}" alt="" width="24" height="24" loading="lazy"></span>'
    return f'<span class="mi__logo mi__logo--icon">{I_LAYOUT}</span>'

def mi(label, href, logo, desc):
    return (f'<a class="mi" href="{href}">{logo_tile(logo, label)}'
            f'<span class="mi__t"><b>{label}</b><small>{desc}</small></span></a>')

def services_panel():
    cols = []
    for col in SERVICES:
        groups = ''
        for title, href, items in col:
            groups += (f'<div class="mgrp"><a class="mgrp__t" href="{href}">{title}<i>{ARROW}</i></a>'
                       + ''.join(mi(*it) for it in items) + '</div>')
        cols.append(f'<div class="mcol">{groups}</div>')
    promo = f'''<div class="mpromo">
            <span class="mpromo__tag">Free · No obligation</span>
            <h4>Not sure where your ad budget is leaking?</h4>
            <p>We audit your account structure, tracking and landing pages, then send a prioritised fix list.</p>
            <ul><li>Ad account review</li><li>Tracking check</li><li>Landing page review</li></ul>
            <a class="hbtn" href="/free-audit/"><span>Get a Free Audit</span><span class="hbtn__box">{ARROW}</span></a>
          </div>'''
    return f'''<div class="mega__box mega__box--svc">
          <div class="mega__head">
            <div><span class="mega__eyebrow">Full-funnel paid media</span><h4>Every channel that drives revenue</h4></div>
            <a class="mega__all" href="services.html">{I_GRID}View all services</a>
          </div>
          <div class="mega__grid">{''.join(cols)}{promo}</div>
        </div>'''

def industries_panel():
    cards = ''.join(f'''<a class="icard" href="{href}"><span class="icard__n">0{n}</span><span class="icard__ic">{svg}</span>
              <b>{t}</b><small>{d}</small></a>''' for n, (t, href, d, svg) in enumerate(INDUSTRIES, 1))
    return f'''<div class="mega__box">
          <div class="mega__head">
            <div><span class="mega__eyebrow">Vertical expertise</span><h4>We already know your ad policies, seasonality and keywords</h4></div>
            <a class="mega__all" href="index.html#industries">{I_GRID}See all industries</a>
          </div>
          <div class="icards">{cards}</div>
        </div>'''

def list_panel(items):
    links = ''.join(f'<a class="mi mi--list" href="{h}"><span class="mi__logo mi__logo--icon">{svg}</span>'
                    f'<span class="mi__t"><b>{t}</b><small>{d}</small></span></a>' for t, h, d, svg in items)
    return f'<div class="mega__box mega__box--list">{links}</div>'

def mobile_nav():
    def acc(label, inner):
        return (f'<div class="mrow"><button class="mtog" type="button" aria-expanded="false" data-mt>{label}'
                f'{CARET}</button><div class="mpanel">{inner}</div></div>')
    svc = ''
    for col in SERVICES:
        for title, href, items in col:
            svc += f'<a class="mgrp-m" href="{href}">{title}</a>'
            svc += ''.join(f'<a class="mlink" href="{h}">{logo_tile(lg, l)}<span>{l}</span></a>' for l, h, lg, d in items)
    ind = ''.join(f'<a class="mlink" href="{h}"><span class="mi__logo mi__logo--icon">{s}</span><span>{t}</span></a>' for t, h, d, s in INDUSTRIES)
    ab = ''.join(f'<a class="mlink" href="{h}"><span class="mi__logo mi__logo--icon">{s}</span><span>{t}</span></a>' for t, h, d, s in ABOUT)
    rs = ''.join(f'<a class="mlink" href="{h}"><span class="mi__logo mi__logo--icon">{s}</span><span>{t}</span></a>' for t, h, d, s in RESOURCES)
    return f'''<div class="mnav" id="mnav">
    <div class="hwrap mnav__in">
      <div class="mrow"><a class="mtog" href="/home">Home</a></div>
      <div class="mrow"><a class="mtog" href="services.html">All Services</a></div>
      {acc('Our Services', svc)}
      {acc('Industries We Help', ind)}
      {acc('About Us', ab)}
      {acc('Resources', rs)}
      <div class="mnav__cta">
        <a class="hphone" href="tel:+763241567889"><span class="hphone__ic">{PHONE}</span><span><small>Call us</small><b>763241567889</b></span></a>
        <a class="hbtn" href="/free-audit/"><span>Get a Free Audit</span><span class="hbtn__box">{ARROW}</span></a>
      </div>
    </div>
  </div>'''

def header_html():
    return f'''<!-- ====================== 02 · HEADER (full-width, sticky) ====================== -->
<header class="s-header" id="header">
  <div class="hwrap hrow">
    <a class="hbrand" href="/home" aria-label="PPC Birds home">
      <img class="hbrand__mark" src="assets/img/logo-mark-white-128.png" alt="" width="46" height="46">
      <span class="hbrand__txt"><b>PPC <span>Birds</span></b><small>Data-Driven Ad Agency</small></span>
    </a>

    <nav class="hnav" aria-label="Primary">
      <a class="hlink" data-key="home" href="/home">Home</a>
      <div class="mega" data-mega data-key="services">
        <button class="hlink" type="button" aria-expanded="false" aria-haspopup="true">Our Services{CARET}</button>
        <div class="mega__bridge">{services_panel()}</div>
      </div>
      <div class="mega" data-mega data-key="industries">
        <button class="hlink" type="button" aria-expanded="false" aria-haspopup="true">Industries{CARET}</button>
        <div class="mega__bridge">{industries_panel()}</div>
      </div>
      <div class="mega mega--sm" data-mega data-key="about">
        <button class="hlink" type="button" aria-expanded="false" aria-haspopup="true">About Us{CARET}</button>
        <div class="mega__bridge">{list_panel(ABOUT)}</div>
      </div>
      <div class="mega mega--sm" data-mega data-key="resources">
        <button class="hlink" type="button" aria-expanded="false" aria-haspopup="true">Resources{CARET}</button>
        <div class="mega__bridge">{list_panel(RESOURCES)}</div>
      </div>
    </nav>

    <div class="hright">
      <a class="hphone" href="tel:+763241567889"><span class="hphone__ic">{PHONE}</span><span><small>Free consultation</small><b>763241567889</b></span></a>
      <a class="hbtn" href="/free-audit/"><span>Get a Free Audit</span><span class="hbtn__box">{ARROW}</span></a>
    </div>

    <div class="hmob">
      <a class="hmob__call" href="/free-audit/">Free Audit</a>
      <button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span></button>
    </div>
  </div>
  {mobile_nav()}
</header>'''
