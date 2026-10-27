# Industry pages, blog posts, portfolio and FAQ content.

INDUSTRIES = [
dict(slug='healthcare-google-ads', title='Healthcare', icon='cross', img='1519494026892-80bbd2d6fd0d', img2='1629909613654-28e377c37b09',
  short='Patient acquisition campaigns for clinics, dental groups and medical practices that stay inside healthcare ad policies.',
  overview=['Healthcare advertising has more rules than most industries. Google and Meta restrict certain treatments, keywords and audience targeting, and tracking pixels on patient-facing pages need careful handling.',
            'We build campaigns that bring in new patient enquiries while respecting those limits: compliant ad copy, location-based targeting, privacy-conscious tracking and call tracking that shows which campaigns fill your appointment book.'],
  features=[('search','Local Patient Search','Campaigns for treatments and services people search near them.'),
            ('phone','Appointment Call Tracking','See which ads turn into booked appointments.'),
            ('lock','Privacy-Conscious Tracking','Setups designed to avoid sending sensitive data to ad platforms.'),
            ('pin','Multi-Location Targeting','Separate budgets and pages for each clinic location.')],
  why=['Experience with healthcare advertising policies','Server-side tracking options for more data control','Landing pages that build trust quickly','Reporting by location and service line'],
  services=['google-ads-management','call-tracking','server-side-tracking'],
  case=('Watson Dental Group','+280%','Patient inquiries'),
  faqs=[('Can you advertise every medical treatment?','Not always. Some treatments and products are restricted or need certification. We check your services against current policies before launch.'),
        ('Is ad tracking allowed on healthcare websites?','It can be, with care. We design setups that limit what data reaches ad platforms, but your compliance advisor should approve the final configuration.'),
        ('Do you work with dental practices?','Yes. Dental is one of our most common healthcare verticals.')]),

dict(slug='mental-health-google-ads', title='Mental Health', icon='heart', img='1544367567-0f2fcb009e0b', img2='1527137342181-19aab11a8ee8',
  short='Sensitive, compliant campaigns that help therapists, counselors and treatment centers reach people ready to book.',
  overview=['People searching for mental health support are often anxious and comparing options carefully. Your ads and pages need to feel calm, credible and clear about next steps.',
            'Ad platforms also limit how health-related audiences can be targeted. We focus on search intent, location and respectful messaging, and track enquiries without exposing sensitive information.'],
  features=[('search','Intent-Based Search','Reach people actively looking for therapy or counseling near them.'),
            ('chat','Respectful Messaging','Ad copy that is supportive and policy-compliant.'),
            ('layout','Calm Landing Pages','Clear information on approach, insurance and first steps.'),
            ('lock','Careful Measurement','Tracking that avoids sharing sensitive details with ad platforms.')],
  why=['Understanding of health-related targeting limits','Messaging reviewed for sensitivity','Insurance and availability highlighted clearly','Booking flows that reduce drop-off'],
  services=['google-ads-management','landing-page-design','conversion-tracking'],
  case=None,
  faqs=[('Can I target people with specific conditions?','No. Major ad platforms do not allow personalized targeting based on health conditions. We rely on search intent and location instead.'),
        ('Do you work with private practices?','Yes, from solo therapists to multi-clinician groups and treatment centers.'),
        ('Can you promote telehealth services?','Yes, with targeting set to the regions where you are licensed to practice.')]),

dict(slug='addiction-treatment-google-ads', title='Addiction Treatment', icon='shield', img='1527137342181-19aab11a8ee8', img2='1576091160550-2173dba999ef',
  short='Certified, compliant addiction treatment advertising with call-level attribution.',
  overview=['Addiction treatment is one of the most regulated categories in paid search. In many regions, Google requires advertisers to be certified before they can run ads for addiction services.',
            'We help you through certification requirements, then run campaigns focused on admissions: compliant ads, call tracking that measures qualified admissions calls and reporting your intake team can trust.'],
  features=[('shield','Certification Support','Guidance on the certification Google requires for addiction services.'),
            ('phone','Admissions Call Tracking','Measure qualified admissions calls, not just clicks.'),
            ('pin','Geo Strategy','Target the regions your facility actually serves.'),
            ('filter','Lead Quality Filtering','Negative keywords and qualification to reduce unqualified calls.')],
  why=['Familiarity with addiction-services ad policies','Call tracking set up for intake teams','Reporting on cost per admission','Ethical, non-exploitative messaging'],
  services=['google-ads-management','calltrackingmetrics-setup','conversion-tracking'],
  case=None,
  faqs=[('Do I need certification to run Google Ads?','In many countries, yes. Google requires certification for addiction services advertising. We help you check requirements before launch.'),
        ('Can you track admissions, not just calls?','Yes. With CRM or call-tracking integration we can measure which calls became admissions.'),
        ('Do you run Meta ads for treatment centers?','Where policies allow, yes, mostly for awareness and remarketing with careful messaging.')]),

dict(slug='ecommerce-google-ads', title='Ecommerce', icon='cart', img='1472851294608-062f824d29cc', img2='1441986300917-64674bd600d8',
  short='Shopping feeds, Performance Max and social campaigns tuned to margin, not just ROAS.',
  overview=['Ecommerce advertising lives and dies on product data, creative and margin. Two products with the same ROAS can have very different profit.',
            'We optimize your product feed, structure Shopping and Performance Max campaigns around margin tiers, and run Meta and TikTok creative tests that bring new customers in at a sustainable cost.'],
  features=[('layers','Feed Optimization','Titles, attributes and categories that improve Shopping visibility.'),
            ('bag','Shopping & PMax','Campaigns split by margin and performance tier.'),
            ('users','Meta & TikTok Prospecting','Creative testing to find new customers at scale.'),
            ('refresh','Retention & Remarketing','Bring past buyers and cart abandoners back.')],
  why=['Profit-focused reporting, not just ROAS','Feed fixes that lift Shopping performance','Creative testing built into management','Shopify and WooCommerce tracking expertise'],
  services=['google-ads-management','meta-ads-management','shopify-development'],
  case=('GreenLeaf Organics','4.2x','ROAS in 90 days'),
  faqs=[('What ROAS should I target?','It depends on your margins. We calculate a break-even ROAS for your products and set targets above it.'),
        ('Do you manage product feeds?','Yes, in Merchant Center and Meta Commerce Manager, including supplemental feeds.'),
        ('Which platforms do you support?','Shopify, WooCommerce and most major ecommerce platforms.')]),

dict(slug='home-and-local-services-google-ads', title='Home & Local Services', icon='home', img='1581578731548-c64695cc6952', img2='1621905251918-48416bd8575a',
  short='Local Services Ads, search campaigns and call tracking that fill the calendar for plumbers, HVAC, cleaners and contractors.',
  overview=['Local service businesses win on speed and trust. When someone needs a plumber or an electrician, they call one of the first few businesses they see.',
            'We combine Google Local Services Ads, tightly targeted search campaigns and call tracking, so you appear when people nearby need you and can see which jobs each campaign produced.'],
  features=[('pin','Local Services Ads','Google Guaranteed listings at the top of local search results.'),
            ('search','Emergency Search Campaigns','Ad scheduling and bids for urgent, high-value searches.'),
            ('phone','Call Tracking & Recording','Know which calls turned into booked jobs.'),
            ('wrench','Service-Area Targeting','Budgets focused on the areas you want to work in.')],
  why=['Built for phone-first lead generation','Ad scheduling around your working hours','Reporting on cost per booked job','Landing pages for each service and area'],
  services=['google-ads-management','callrail-setup','landing-page-design'],
  case=None,
  faqs=[('What are Local Services Ads?','A Google ad format for local service businesses that appears above regular ads and charges per lead rather than per click.'),
        ('Can you run ads only during business hours?','Yes, or schedule higher bids for after-hours emergency work if you offer it.'),
        ('Do you work with multi-location businesses?','Yes, with separate campaigns and tracking per location.')]),
]
IND_BY_SLUG = {i['slug']: i for i in INDUSTRIES}

# ------------------------------------------------------------------ BLOG
POSTS = [
dict(slug='server-side-tracking-guide', title='Why Your Ad Platforms Are Missing Conversions (and How Server-Side Tracking Fixes It)',
  cat='Tracking', date='October 14, 2026', read='7 min read', img='1551288049-bebda4e38f71',
  excerpt='Browser privacy changes have quietly broken conversion tracking for many advertisers. Here is how to tell, and what to do about it.',
  tags=['Tracking','Google Ads','Meta Ads'],
  body='''<p>If your CRM shows more leads than Google Ads or Meta reports, you are not imagining it. Ad blockers, browser privacy features and consent banners all reduce how many conversions the platforms can see. The result is weaker optimization and higher costs.</p>
<p>The good news: most of that lost signal can be recovered with a better tracking setup.</p>
<blockquote>“Ad platforms optimize toward whatever you tell them is a conversion. If half the signal is missing, the algorithm is working with half the picture.”<cite>PPC Birds tracking team</cite></blockquote>
<h2>Signs your tracking is underreporting</h2>
<ul><li>Conversions in your ad accounts are well below the leads in your CRM.</li><li>Results dropped suddenly after a website or consent banner change.</li><li>Meta shows a low Event Match Quality score.</li><li>Google Ads flags enhanced conversions as not set up.</li></ul>
<h2>What server-side tracking changes</h2>
<p>With server-side tagging, your website sends data to a tagging server you control first. That server forwards events to Google, Meta and TikTok. Because it runs on your own subdomain, cookies last longer and fewer requests are blocked.</p>
<p>It also gives you control. You can remove or transform data before any platform receives it, which matters a lot in regulated industries such as healthcare.</p>
<h2>Where to start</h2>
<p>Start with an audit of what is firing today. Then add Google Ads enhanced conversions and the Meta Conversions API, which recover a large share of lost signal on their own. Server-side GTM is the next step once those basics are solid.</p>'''),

dict(slug='google-vs-microsoft-ads', title='Google Ads vs Microsoft Ads: Where Should Your Next Dollar Go?',
  cat='PPC', date='September 29, 2026', read='6 min read', img='1504868584819-f8e8b4b6d7e3',
  excerpt='Microsoft Ads is often the cheapest second channel for businesses already on Google. Here is how to decide.',
  tags=['Google Ads','Bing Ads','Budgeting'],
  body='''<p>Google captures most search demand, so it is the natural first channel. Once your Google Ads account is profitable, the question becomes where to put the next dollar: more Google budget, or a new channel?</p>
<h2>Why Microsoft Ads is worth testing</h2>
<ul><li>You can import existing Google campaigns and launch quickly.</li><li>Competition is usually lighter, which can mean lower CPCs.</li><li>LinkedIn profile targeting makes it strong for B2B.</li><li>The audience skews older and higher-income.</li></ul>
<blockquote>“The best second channel is usually the one that reuses what already works. For search advertisers, that is Microsoft.”<cite>PPC Birds paid media team</cite></blockquote>
<h2>When to stay focused on Google</h2>
<p>If your Google campaigns are still limited by budget on profitable keywords, more Google spend usually beats a new channel. Expand where you already know the returns.</p>
<h2>How we run the test</h2>
<p>We import your best campaigns, re-check bids, negatives and extensions, install UET tracking and set a separate test budget. After a few weeks of data, we compare cost per lead side by side.</p>'''),

dict(slug='landing-page-fixes', title='5 Landing Page Fixes That Lower Cost Per Lead',
  cat='Conversion', date='September 10, 2026', read='5 min read', img='1559028012-481c04fa702d',
  excerpt='Before you raise your ad budget, fix the page the traffic lands on. These five changes make the biggest difference.',
  tags=['Landing Pages','CRO'],
  body='''<p>Many campaigns that look like ad problems are actually landing page problems. The ad does its job, then the visitor lands somewhere slow, generic or confusing.</p>
<h2>1. Match the message to the ad</h2>
<p>If the ad promises emergency plumbing, the page headline should say emergency plumbing, not “Welcome to our company.”</p>
<h2>2. Load fast on mobile</h2>
<p>Most paid clicks come from phones. Compress images, remove unnecessary scripts and test on a real mobile connection.</p>
<h2>3. One page, one action</h2>
<p>Remove navigation menus and competing links. Give visitors one clear thing to do.</p>
<h2>4. Show proof early</h2>
<ul><li>Reviews and star ratings</li><li>Recognizable client logos</li><li>Specific results with numbers</li></ul>
<h2>5. Ask for less</h2>
<p>Every extra form field costs conversions. Ask only for what you need to follow up, and collect the rest later.</p>
<blockquote>“A better landing page lowers your cost per lead on every channel at once.”<cite>PPC Birds CRO team</cite></blockquote>'''),

dict(slug='agency-portfolio-essentials', title='Essential Portfolios Every Digital Marketing Agency Must Have',
  cat='Digital Marketing', date='August 22, 2026', read='6 min read', img='1460925895917-afdab827c52f',
  excerpt='What a strong agency portfolio shows, and why case studies with real numbers beat pretty screenshots.',
  tags=['Agency','Case Studies'],
  body='''<p>Prospects hiring an agency want proof that you can solve a problem like theirs. A portfolio is where you provide it.</p>
<h2>What every portfolio needs</h2>
<ul><li>Case studies in the industries you want more of</li><li>The starting problem, not just the result</li><li>Specific numbers: cost per lead, ROAS, conversion rate</li><li>A short quote from the client</li></ul>
<blockquote>“Screenshots show what you made. Numbers show what it did.”<cite>PPC Birds</cite></blockquote>
<h2>Structure each case study the same way</h2>
<p>Challenge, approach, results. Keep it short, lead with the headline metric and link to the service that delivered it.</p>
<h2>Keep it current</h2>
<p>Review your portfolio every quarter. Replace older work with recent results in the verticals you are targeting.</p>'''),

dict(slug='high-converting-agency-website', title='Building a High-Converting Portfolio Website for Agencies',
  cat='Website', date='August 5, 2026', read='8 min read', img='1467232004584-a241de8bcf5d',
  excerpt='The pages, proof and calls to action that turn agency website visitors into booked calls.',
  tags=['Web Design','Agency','CRO'],
  body='''<p>An agency website has one job: convince the right prospect to book a call. Everything on the site should support that.</p>
<h2>The pages that matter most</h2>
<ul><li>Service pages that speak to one problem each</li><li>Industry pages for your best verticals</li><li>Case studies with real numbers</li><li>A simple, low-friction audit or contact form</li></ul>
<h2>Make the next step obvious</h2>
<p>Use one primary call to action across the site, such as a free audit. Repeat it in the header, after key sections and at the end of every page.</p>
<blockquote>“If a visitor has to think about what to do next, many of them will not do anything.”<cite>PPC Birds web team</cite></blockquote>
<h2>Track every enquiry</h2>
<p>Install analytics and conversion tracking before launch so you know which pages and channels bring in clients.</p>'''),

dict(slug='marketing-narratives', title='Crafting Compelling Narratives for Digital Marketing Success',
  cat='Digital Marketing', date='July 18, 2026', read='5 min read', img='1552664730-d307ca884978',
  excerpt='How a clear story about your customer’s problem makes every ad, page and email perform better.',
  tags=['Messaging','Copywriting'],
  body='''<p>The best-performing ads rarely talk about the business first. They talk about the customer’s problem, then show a clear way out.</p>
<h2>A simple narrative framework</h2>
<ul><li><strong>Problem:</strong> what is frustrating your customer right now</li><li><strong>Stakes:</strong> what it costs them to leave it unsolved</li><li><strong>Solution:</strong> how you fix it, in plain language</li><li><strong>Proof:</strong> results, reviews or numbers</li><li><strong>Next step:</strong> one clear action</li></ul>
<h2>Use it everywhere</h2>
<p>Once the story is clear, reuse it across search ads, social creative, landing pages and follow-up emails. Consistency builds trust.</p>
<blockquote>“People remember stories about themselves far better than facts about you.”<cite>PPC Birds</cite></blockquote>'''),
]
POST_BY_SLUG = {p['slug']: p for p in POSTS}

# ------------------------------------------------------------------ PORTFOLIO (from client content)
CASES = [
dict(name='GreenLeaf Organics', cats=['ecommerce','google'], tags=['Google Ads','E-commerce'], img='1542838132-92c53300491e',
  summary='An organic food brand spending $5K a month with no clear return. We rebuilt Shopping and Performance Max around margin tiers and fixed conversion tracking.',
  metrics=[('4.2x','ROAS in 90 days'),('-58%','Cost per acquisition'),('$45K','Monthly revenue')],
  quote=('We went from burning $5K/month with no results to generating $45K in monthly revenue with a 4.2x ROAS.','Mehedi Hasan, CEO')),
dict(name='TechVault Solutions', cats=['b2b','social'], tags=['Meta Ads','B2B SaaS'], img='1551434678-e076c223a692',
  summary='A B2B SaaS company with expensive, low-quality leads. We rebuilt the funnel, added lead qualification and fed Meta better data through the Conversions API.',
  metrics=[('+312%','Qualified leads'),('$34','Cost per lead'),('$120','Previous CPL')],
  quote=('They rebuilt our entire funnel and we saw a 312% increase in qualified leads within the first quarter.','David Chen, Marketing Director')),
dict(name='Bella Vita Fashion', cats=['ecommerce','web'], tags=['Shopify','E-commerce'], img='1441986300917-64674bd600d8',
  summary='A fashion brand whose Shopify store was holding back its ads. We rebuilt product pages, improved speed and set up full ecommerce tracking.',
  metrics=[('3.8%','Conversion rate'),('+47%','Average order value'),('300%','ROAS')],
  quote=None),
dict(name='Watson Dental Group', cats=['healthcare','google'], tags=['Google Ads','Healthcare'], img='1629909613654-28e377c37b09',
  summary='A multi-chair dental practice relying on referrals. We launched local search campaigns, dedicated treatment landing pages and call tracking.',
  metrics=[('+280%','Patient inquiries'),('#1','for 12 local keywords'),('30 days','To first results')],
  quote=('Patient inquiries increased 280% and we rank #1 for 12 local keywords. Best investment we\'ve made.','Emily Watson, Owner')),
]

# ------------------------------------------------------------------ FAQ PAGE
FAQ_GROUPS = [
('general','General','help',[
  ('Who is PPC Birds?','A full-service digital marketing agency specializing in paid advertising, web development and conversion optimization.'),
  ('Which businesses do you work with?','Mostly healthcare, mental health, addiction treatment, ecommerce and home and local service businesses, plus B2B companies.'),
  ('Do you work with businesses outside the US?','Yes. We manage campaigns across multiple countries and time zones.'),
  ('What is included in the free audit?','A review of your ad accounts, tracking and landing pages, with a prioritised list of fixes and a recommended budget.')]),
('pricing','Pricing & Contracts','dollar',[
  ('What\'s your pricing model?','A flat monthly management fee based on scope, not a percentage of your ad spend.'),
  ('Do you require long-term contracts?','No. We work month to month with 30 days\' notice.'),
  ('Is ad spend included in your fee?','No. Ad spend is paid directly to Google, Microsoft, Meta or TikTok, so you always see what is media and what is management.'),
  ('Is there a setup fee?','No setup fee on our management plans.')]),
('ppc','PPC & Social Ads','search',[
  ('How long does it take to see results?','Most clients see measurable improvements within 30–60 days. Paid campaigns typically show initial results within 2 weeks.'),
  ('Who owns the ad accounts?','You do. We work inside accounts in your name, so you keep everything if you leave.'),
  ('How often do you report?','Weekly reports plus a live dashboard you can check any time.'),
  ('Do you create ad creative?','Yes. We write ad copy and produce static and simple video creative, and brief your team or creators for filmed content.')]),
('tracking','Tracking','trend',[
  ('Can you fix tracking on my existing site?','Yes, without rebuilding your site. We work in your Google Tag Manager containers.'),
  ('Do you set up server-side tracking?','Yes, including server-side GTM, Meta Conversions API and TikTok Events API.'),
  ('Do you track phone calls?','Yes, with CallRail or CallTrackingMetrics connected to your ad platforms.')]),
('web','Websites','browser',[
  ('Which platforms do you build on?','WordPress, Wix, Squarespace, GoDaddy and Shopify.'),
  ('Can I update my website after it\'s built?','Yes. We train your team and choose a setup that makes editing easy.'),
  ('Do you offer ongoing maintenance?','Yes, including updates, backups and speed checks.')]),
]
