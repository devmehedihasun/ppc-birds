# PPC Birds — Front-end

Complete static HTML/CSS/JS build of the PPC Birds website (43 pages), ready to convert into a WordPress theme.
No frameworks, no jQuery, no build step needed to view it. Open `index.html` in a browser.

## Structure

```
ppc-birds/
├── *.html                  43 pages (see page map below)
├── partials/
│   ├── header.html         Top bar, sticky nav, mega menu, mobile menu → header.php
│   └── footer.html         Newsletter, footer columns, bottom bar     → footer.php
├── assets/
│   ├── css/
│   │   ├── main.css        Global: tokens, base, buttons, header, hero, footer, shared components
│   │   ├── sections.css    Section blocks shared across templates (homepage, services, about)
│   │   └── pages.css       Inner templates: service/industry detail, about, contact, blog, article,
│   │                       portfolio, FAQ, free audit, legal, 404, forms, sidebar
│   ├── js/main.js          All behaviour; every module checks for its own markup
│   └── img/                logo-mark(.png/-128), logo-mark-white(.png/-128), favicon.png,
│                           apple-touch-icon.png, brands/ (platform logos for the mega menu)
└── tools/src/              Optional generator (Python 3.12+). Edit content, run build.py, all pages update.
```

Every page loads `main.css` + `sections.css`. Inner pages also load `pages.css`.

## Page map → WordPress templates

| Static file(s) | Count | Final URL (sitemap) | WordPress template |
|---|---|---|---|
| `index.html` | 1 | `/` | `front-page.php` |
| `services.html` | 1 | `/services/` | `page-services.php` |
| `ppc-management.html`, `social-media-marketing.html`, `conversion-tracking.html`, `call-tracking.html`, `landing-page-design.html`, `website-design-development.html` | 6 | `/ppc-management/` … | `single-service.php` (parent service) |
| `google-ads-management.html`, `bing-ads.html`, `chatgpt-ads-management.html`, `meta-ads-management.html`, `tiktok-ads-management.html`, `enhanced-conversions.html`, `meta-pixel-meta-capi.html`, `server-side-tracking.html`, `calltrackingmetrics-setup.html`, `callrail-setup.html`, `wordpress-development.html`, `wix-development.html`, `squarespace-development.html`, `godaddy-development.html`, `shopify-development.html` | 15 | `/ppc-management/google-ads-management/` … | `single-service.php` (child service) |
| `healthcare-google-ads.html`, `mental-health-google-ads.html`, `addiction-treatment-google-ads.html`, `ecommerce-google-ads.html`, `home-and-local-services-google-ads.html` | 5 | `/industries/…/` | `single-industry.php` |
| `about.html` | 1 | `/about/` | `page-about.php` |
| `contact.html` | 1 | `/contact/` | `page-contact.php` |
| `blog.html` | 1 | `/blog/` | `home.php` / `archive.php` |
| 6 article files (e.g. `server-side-tracking-guide.html`) | 6 | `/{post-slug}/` | `single.php` |
| `portfolio.html` | 1 | `/portfolio/`, `/results/` | `page-portfolio.php` |
| `faq.html` | 1 | `/faq/` | `page-faq.php` |
| `free-audit.html` | 1 | `/free-audit/` | `page-free-audit.php` |
| `privacy-policy.html`, `terms.html` | 2 | `/privacy-policy/`, `/terms/` | `page-legal.php` |
| `404.html` | 1 | — | `404.php` |

**One template, many pages.** All 21 service pages share one layout (hero → overview → stats → what's included →
why us → process → FAQ, with a sticky service sidebar). Parent services show their child services in the
"What's included" grid. The 5 industry pages use the same layout with an industry sidebar.
In WordPress, register a `service` and an `industry` custom post type (or use child pages) and store the
per-page content in ACF fields: `short`, `overview`, `features` (repeater: icon, title, text), `why` (repeater),
`faqs` (repeater: question, answer).

## Brand tokens (top of `main.css`)

| Token | Value | Use |
|---|---|---|
| `--g800` | `#073B36` | Deep Green: dark blocks, headings accents |
| `--g500` | `#159A7C` | Light Green: buttons, highlights, icons |
| `--ink` | `#0A1F1C` | Headings |
| `--text` | `#5B6F6B` | Body copy |
| `--bg2` | `#F4F8F6` | Tinted section bands |
| `--font` | Plus Jakarta Sans | 400–800 |
| `--wrap` | `1300px` | Container width |

## WordPress conversion notes

**Enqueue** (functions.php):

```php
add_action('wp_enqueue_scripts', function () {
  $v = '1.0.0'; $uri = get_template_directory_uri() . '/assets';
  wp_enqueue_style('ppcb-font', 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap', [], null);
  wp_enqueue_style('ppcb-main', "$uri/css/main.css", ['ppcb-font'], $v);
  wp_enqueue_style('ppcb-sections', "$uri/css/sections.css", ['ppcb-main'], $v);
  if (!is_front_page()) wp_enqueue_style('ppcb-pages', "$uri/css/pages.css", ['ppcb-sections'], $v);
  wp_enqueue_script('ppcb-main', "$uri/js/main.js", [], $v, true);
});
```

**Header & mega menus.** Full-width sticky header (`.s-header`, 1720px `.hwrap` container) following the client's
RightPath reference: pill links (`.hlink`), wide centred mega panels (`.mega` → `.mega__bridge` → `.mega__box`),
phone block (`.hphone`) and CTA (`.hbtn`). Panels open on hover (desktop) and on click/tap/keyboard (`initMega()` in
main.js); Escape or an outside click closes them. Below 1140px the header switches to a burger and a full-width drawer
(`#mnav`). Each service item (`.mi`) shows its platform logo from `assets/img/brands/`. In WordPress, build the menu with
`wp_nav_menu()` + a custom walker or an Elementor mega-menu widget, keeping these class names, and store each item's
logo as a menu-item custom field. Map `current-menu-item` / `current-menu-ancestor` to `is-cur`.

**Logos.** `logo-mark.png` (colour, for light backgrounds) and `logo-mark-white.png` (white bars, for the dark header and
footer) are cleaned from the client's file with the colours snapped to #073B36 / #159A7C. Platform logos and their
licences are listed in `assets/img/brands/LICENSES.txt`. **`callrail.svg` and `calltrackingmetrics.svg` are placeholders**:
drop the official SVGs in with the same file names and they appear everywhere.

**Rich text.** Article bodies and service overviews use `.prose`, which styles `h2`, `h3`, `ul` (check bullets),
`ol`, `blockquote` + `cite`, links and images. Wrap `the_content()` in `<div class="prose">`.

**Forms.** Contact (`contact.html`), Free Audit (`free-audit.html`) and blog comments use `form.js-form`,
which validates in the browser and shows `.form__ok`. Swap in your form plugin (Fluent Forms, Gravity Forms, CF7)
and reuse the `.form`, `.fld`, `.chip` classes for styling. The newsletter form is `#nform`.
Blog comments should use `comment_form()` with the same classes.

**Filters.** Blog and portfolio use `[data-filter]` with `.fchip[data-f]` buttons and `[data-cat]` items.
In WordPress, output category slugs into `data-cat`.

**Other behaviour.** `data-count` animates numbers; `data-marquee` loops any single-child track;
`data-spy` highlights in-page topic links (FAQ page).

**Images.** All photos are Unsplash placeholders. Replace with Media Library images via `wp_get_attachment_image()`,
keeping the classes. Images that fail to load fall back to a brand-green fill.

## Editing with the generator (optional)

`tools/src/` holds the content and templates used to generate the pages. Edit `data_services.py`
(services), `data_content.py` (industries, posts, portfolio, FAQ) or the shared `header.html` / `footer.html`, then:

```
cd tools/src && python3 build.py
```

All pages are regenerated in place, and the script reports any broken internal links.
`tools/` is not needed on the live site.

## Quality checks

- Tested at 1440, 1024 and 390px on all 43 pages: no horizontal scroll, no script errors, no missing local files.
- Every internal link resolves to a page in the build.
- Responsive breakpoints at 1240, 1180, 1080, 767 and 480px. Hamburger menu below 1080px.
- `prefers-reduced-motion` disables animation; content is visible without JavaScript.
- Skip link, visible focus states, labelled form fields, `aria-expanded` on toggles, `aria-current` on breadcrumbs.

## Content to confirm with the client before launch

- **Pricing:** all three tiers read $500/month; Startup and Enterprise list overlapping features.
- **Team (About page):** cards show roles with stock photos. Replace with real team photos and names.
- **Working hours** (Mon–Fri, 9:00–18:00) were assumed. Confirm them.
- **Phone number** `763241567889` has no country code or formatting.
- **Social links** are `#` placeholders.
- **Blog posts:** three titles come from the supplied content. The other three posts and all article bodies are draft copy to review.
- **Service and industry copy** is written from the sitemap and should be reviewed by the client. Industry pages mention
  healthcare and addiction-treatment ad policies; confirm against current Google/Meta policy for the client's markets.
- **Legal pages** are generic templates. Have them reviewed by the client's legal advisor.
