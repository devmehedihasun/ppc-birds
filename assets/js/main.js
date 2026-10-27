/*!
 * PPC Birds — main.js
 * Shared behaviour for every template. No dependencies.
 * Each module checks for its own markup, so the file can load on any page.
 * WordPress: wp_enqueue_script('ppcb-main', get_template_directory_uri().'/assets/js/main.js', [], '1.0.0', true);
 */
(function () {
  "use strict";

  var doc = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ------------------------------------------------------------------
   * 1. Broken / blocked images fall back to the brand fill behind them
   * ------------------------------------------------------------------ */
  function initImageFallback() {
    $$("img").forEach(function (img) {
      var hide = function () {
        img.classList.add("img-off");
        img.removeAttribute("srcset");
        img.src = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==";
      };
      if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) hide();
      else img.addEventListener("error", hide, { once: true });
    });
  }

  /* ------------------------------------------------------------------
   * 2. Marquees — duplicate the group once for a seamless CSS loop
   *    Markup: <div data-marquee><div>…items…</div></div>
   * ------------------------------------------------------------------ */
  function initMarquees() {
    $$("[data-marquee]").forEach(function (track) {
      if (track.children.length !== 1) return;
      var clone = track.firstElementChild.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      $$("a,button", clone).forEach(function (el) { el.setAttribute("tabindex", "-1"); });
      track.appendChild(clone);
    });
  }

  /* ------------------------------------------------------------------
   * 3. Header — solid pill once the page scrolls
   * ------------------------------------------------------------------ */
  function initHeader() {
    var header = $("#header");
    if (!header) return;
    var ticking = false;
    var update = function () {
      header.classList.toggle("stuck", window.scrollY > 60);
      ticking = false;
    };
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------
   * 4. Mobile navigation + sub-menu accordions
   * ------------------------------------------------------------------ */
  function initMobileNav() {
    var burger = $("#burger");
    var panel = $("#mnav");
    if (!burger || !panel) return;

    var setOpen = function (open) {
      panel.classList.toggle("on", open);
      burger.classList.toggle("on", open);
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };

    burger.addEventListener("click", function () {
      setOpen(!panel.classList.contains("on"));
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && panel.classList.contains("on")) { setOpen(false); burger.focus(); }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 1140 && panel.classList.contains("on")) setOpen(false);
    });

    $$("[data-mt]", panel).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = btn.nextElementSibling;
        btn.setAttribute("aria-expanded", String(sub.classList.toggle("on")));
      });
    });
  }


  /* ------------------------------------------------------------------
   * 4b. Mega menus — hover on desktop (CSS), click/tap + keyboard here.
   *     One panel open at a time; Escape or an outside click closes it.
   * ------------------------------------------------------------------ */
  function initMega() {
    var megas = $$("[data-mega]");
    if (!megas.length) return;
    var closeAll = function (except) {
      megas.forEach(function (m) {
        if (m === except) return;
        m.classList.remove("open");
        var b = $("button", m); if (b) b.setAttribute("aria-expanded", "false");
      });
    };
    megas.forEach(function (m) {
      var btn = $("button", m);
      if (!btn) return;
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = !m.classList.contains("open");
        closeAll(m);
        m.classList.toggle("open", open);
        btn.setAttribute("aria-expanded", String(open));
      });
      m.addEventListener("mouseleave", function () {
        if (m.classList.contains("open") && window.matchMedia("(hover: hover)").matches) {
          m.classList.remove("open"); btn.setAttribute("aria-expanded", "false");
        }
      });
      $(".mega__bridge", m).addEventListener("click", function (e) { e.stopPropagation(); });
    });
    document.addEventListener("click", function () { closeAll(null); });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      var open = megas.filter(function (m) { return m.classList.contains("open") || m.contains(document.activeElement); })[0];
      closeAll(null);
      if (open) { var b = $("button", open); if (b) b.focus(); }
    });
  }

  /* ------------------------------------------------------------------
   * 5. FAQ accordion — one open item per list
   * ------------------------------------------------------------------ */
  function initAccordions() {
    $$(".acc").forEach(function (list) {
      $$(".acc__q", list).forEach(function (q) {
        q.addEventListener("click", function () {
          var item = q.parentElement;
          var wasOpen = item.classList.contains("on");
          $$(".acc__i", list).forEach(function (i) {
            i.classList.remove("on");
            i.firstElementChild.setAttribute("aria-expanded", "false");
          });
          if (!wasOpen) { item.classList.add("on"); q.setAttribute("aria-expanded", "true"); }
        });
      });
    });
  }

  /* ------------------------------------------------------------------
   * 6. Newsletter — front-end validation only.
   *    Replace the submit handler with your form plugin / AJAX endpoint.
   * ------------------------------------------------------------------ */
  function initNewsletter() {
    var form = $("#nform");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = $("#nemail", form);
      if (!input.checkValidity()) { input.reportValidity(); return; }
      var ok = $("#nformOk", form);
      if (ok) ok.classList.add("on");
      input.value = "";
    });
  }

  /* ------------------------------------------------------------------
   * 7. Counters — data-count="350" data-prefix="$" data-suffix="+" data-dec="1"
   *    The final value is already in the HTML, so no-JS users see it.
   * ------------------------------------------------------------------ */
  function countUp(el) {
    var to = parseFloat(el.getAttribute("data-count"));
    if (isNaN(to)) return;
    var dec = parseInt(el.getAttribute("data-dec") || "0", 10);
    var pre = el.getAttribute("data-prefix") || "";
    var suf = el.getAttribute("data-suffix") || "";
    var start = null;
    var step = function (ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / 1600, 1);
      var v = to * (1 - Math.pow(1 - p, 3));
      el.textContent = pre + v.toFixed(dec) + suf;
      if (p < 1) window.requestAnimationFrame(step);
      else el.textContent = pre + to.toFixed(dec) + suf;
    };
    window.requestAnimationFrame(step);
  }

  /* ------------------------------------------------------------------
   * 8. Scroll reveal (.rv) + counters. Content stays visible without JS
   *    or with reduced motion: the hidden state only exists under .js
   * ------------------------------------------------------------------ */
  function initReveal() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    doc.classList.add("js");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        if (el.classList.contains("rv")) {
          var idx = Array.prototype.indexOf.call(el.parentElement.children, el);
          el.style.transitionDelay = Math.min(idx, 5) * 80 + "ms";
          el.classList.add("in");
        }
        if (el.hasAttribute("data-count")) countUp(el);
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    $$(".rv,[data-count]").forEach(function (el) { io.observe(el); });
  }


  /* ------------------------------------------------------------------
   * 9. Category filters (blog, portfolio)
   *    <div data-filter> … <button class="fchip" data-f="key"> … <article data-cat="a b">
   * ------------------------------------------------------------------ */
  function initFilters() {
    $$("[data-filter]").forEach(function (scope) {
      var chips = $$(".fchip", scope);
      var items = $$("[data-cat]", scope);
      var empty = $("[data-empty]", scope);
      chips.forEach(function (chip) {
        chip.setAttribute("aria-pressed", chip.classList.contains("on") ? "true" : "false");
        chip.addEventListener("click", function () {
          var key = chip.getAttribute("data-f");
          chips.forEach(function (c) { var on = c === chip; c.classList.toggle("on", on); c.setAttribute("aria-pressed", String(on)); });
          var shown = 0;
          items.forEach(function (it) {
            var match = key === "all" || it.getAttribute("data-cat").split(" ").indexOf(key) !== -1;
            it.classList.toggle("is-hidden", !match);
            if (match) { shown++; it.classList.add("in"); }
          });
          if (empty) empty.classList.toggle("on", shown === 0);
        });
      });
    });
  }

  /* ------------------------------------------------------------------
   * 10. Forms (contact, free audit, comments) — validation + success state.
   *     Replace with your form plugin's markup/handler in WordPress.
   * ------------------------------------------------------------------ */
  function initForms() {
    $$("form.js-form").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity(); return; }
        var ok = $(".form__ok", form);
        if (ok) { ok.classList.add("on"); ok.focus && ok.setAttribute("tabindex", "-1"); ok.focus(); }
        form.reset();
      });
    });
  }

  /* ------------------------------------------------------------------
   * 11. Scroll-spy for in-page topic navs (FAQ page)
   * ------------------------------------------------------------------ */
  function initSpy() {
    var nav = $("[data-spy]");
    if (!nav || !("IntersectionObserver" in window)) return;
    var links = $$("a[href^='#']", nav);
    var map = {};
    links.forEach(function (a) { var t = document.getElementById(a.getAttribute("href").slice(1)); if (t) map[t.id] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove("on"); });
        map[en.target.id].classList.add("on");
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
  }

  function init() {
    initMarquees();
    initImageFallback();
    initHeader();
    initMobileNav();
    initMega();
    initAccordions();
    initNewsletter();
    initFilters();
    initForms();
    initSpy();
    initReveal();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
