#!/usr/bin/env python3
"""
GI Oncology Daily Digest Engine
================================
Stable generation engine that reads a daily JSON data file and produces:
  1. digests/digest-YYYY-MM-DD.html  (main digest page)
  2. digests/x-thread-YYYY-MM-DD.html (X/Twitter thread draft)
  3. digests/digest-feed.json (updated feed, single source of truth)
  4. digests/index_digest.html (rebuilt archive page)

Usage:
  python3 digest_engine.py digests/data/2026-04-18.json

The JSON schema is documented in digests/data/README_SCHEMA.md
"""

import json
import os
import sys
import html as html_mod
from datetime import datetime

# ---------------------------------------------------------------------------
# Resolve paths relative to this script (works whether called from repo root
# or from another directory).
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIGESTS_DIR = os.path.join(SCRIPT_DIR, "digests")
FEED_PATH = os.path.join(DIGESTS_DIR, "digest-feed.json")

# ---------------------------------------------------------------------------
# HTML TEMPLATE PIECES  (stable — edit only when site design changes)
# ---------------------------------------------------------------------------

# Shared: anti-flash IIFE
IIFE_OPEN = """    <script>
      (function () {
        try {
          var saved = localStorage.getItem('site-theme');
          if (saved === 'dark' || saved === 'light') {
            document.documentElement.setAttribute('data-theme', saved);
          }
        } catch (e) {}
      }());
    </script>"""

# Shared: theme-toggle script block
THEME_TOGGLE_JS = """    <script>
      (function () {
        var btn = document.getElementById('btn-theme');
        if (!btn) return;
        btn.addEventListener('click', function () {
          var current = document.documentElement.getAttribute('data-theme');
          var isDark = current === 'dark' || (!current && window.matchMedia('(prefers-color-scheme: dark)').matches);
          var next = isDark ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', next);
          try { localStorage.setItem('site-theme', next); } catch (e) {}
        });
      }());
    </script>"""

# Shared: navbar HTML
NAVBAR = """    <nav class="navbar navbar-expand-lg navbar-light sticky-top site-nav" id="collapseExample">
      <div class="container">
        <a class="navbar-brand" href="../index.html">Dr. Allan Pereira</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSite" id="btnCollapse"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarSite">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item"><a class="nav-link" href="../index.html#curriculo">CV</a></li>
            <li class="nav-item"><a class="nav-link" href="../index.html#">Testimonials</a></li>
            <li class="nav-item"><a class="nav-link" href="../index.html#contact">Contact</a></li>
            <li class="nav-item"><a class="nav-link font-weight-bold" href="index_digest.html">GI Digest</a></li>
          </ul>
          <div class="d-flex align-items-center ml-3">
            <button class="btn-lang mr-1" id="btn-pt">PT</button>
            <button class="btn-lang" id="btn-en">EN</button>
            <button class="btn-theme" id="btn-theme" aria-label="Toggle dark mode">
              <i class="fas fa-moon icon-moon" aria-hidden="true"></i>
              <i class="fas fa-sun icon-sun" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      </div>
    </nav>"""

# Shared: full footer with social links
FOOTER_FULL = """    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-md-4 mb-5 mb-md-0">
            <h5>Dr. Allan Pereira</h5>
            <p data-i18n="hero-badge">Clinical Oncologist</p>
            <a href="https://www.moffitt.org/eforms/patientregistrationform/" style="font-size:.875rem;" data-i18n="footer-book-btn">Book appointment</a>
            <a href="https://www.moffitt.org/eforms/international-form/" class="d-flex align-items-center mb-2" style="gap:.5rem; font-size:.875rem;" data-i18n="hero-cta-intl">International Patient Appointment</a>
          </div>
          <div class="col-md-4 mb-5 mb-md-0">
            <h5>Social Media</h5>
            <div class="mt-1">
              <a class="social-icon" href="https://www.facebook.com/allan.pereira.311" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
              <a class="social-icon" href="https://twitter.com/DrAllanPereira" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
              <a class="social-icon" href="https://www.linkedin.com/in/allan-pereira-onco/" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
              <a class="social-icon" href="https://www.instagram.com/DrAllanPereira/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
              <a class="social-icon" href="https://www.youtube.com/channel/UCVR9xfo3yI7U8VjuKQt7a7A" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            </div>
          </div>
          <div class="col-md-4">
            <h5 data-i18n="footer-offices-title">Locations &amp; Directions</h5>
            <p data-i18n="footer-offices-cta">Click for details:</p>
            <button type="button" class="btn-ghost d-block mb-2" style="font-size:.8rem; padding:.4rem 1rem;" data-toggle="modal" data-target="#modalRegular" data-i18n="footer-unit1">Moffitt Magnolia Campus</button>
          </div>
        </div>
        <div class="footer-divider"></div>
        <div class="row">
          <div class="col-12 text-center footer-copyright">
            <small>Copyright &copy; Dr. Allan Pereira 2025</small>
          </div>
        </div>
      </div>
    </footer>"""

# Shared: minimal footer for index page
FOOTER_MINIMAL = """    <footer class="site-footer">
      <div class="container">
        <div class="footer-divider"></div>
        <div class="row"><div class="col-12 text-center footer-copyright"><small>Copyright &copy; Dr. Allan Pereira 2025</small></div></div>
      </div>
    </footer>"""

# Shared: bottom scripts
BOTTOM_SCRIPTS = """    <a id="back-to-top" href="#page-top" role="button" aria-label="Back to top"><i class="fas fa-chevron-up"></i></a>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>"""


# ===================================================================
#  1. DIGEST HTML
# ===================================================================
def build_digest_html(data):
    """Generate the main digest HTML page from the data dict."""
    date_str = data["date"]              # e.g. "2026-04-18"
    date_nice = data["date_display"]     # e.g. "April 18, 2026"
    subtitle = data.get("subtitle", "")  # e.g. "AACR 2026 Special Edition"
    papers = data["papers"]              # list of top-5 paper dicts
    additional = data["additional"]      # list of additional paper dicts

    date_line = date_nice
    if subtitle:
        date_line += " — " + subtitle

    meta_desc = ("GI Oncology Daily Digest — " + date_nice + ". "
                 + (subtitle + ". " if subtitle else "")
                 + "Curated by Dr. Allan Pereira.")

    # --- build paper cards ---
    cards_html = ""
    for i, p in enumerate(papers, 1):
        cards_html += '\n        <div class="paper-card">\n'
        cards_html += '          <span class="paper-rank">#' + str(i) + '</span>\n'
        cards_html += '          <div class="paper-title"><a href="' + html_mod.escape(p["url"]) + '" target="_blank">' + html_mod.escape(p["title"]) + '</a></div>\n'
        cards_html += '          <div class="paper-meta"><b>Source:</b> ' + html_mod.escape(p["source"]) + ' &nbsp;|&nbsp; <b>Authors:</b> ' + html_mod.escape(p["authors"]) + ' &nbsp;|&nbsp; <b>Published:</b> ' + html_mod.escape(p["published"]) + '</div>\n'
        cards_html += '          <div class="score-line"><span class="score-badge">Score: ' + str(p["score"]) + '/20</span><span class="score-rationale"> — ' + html_mod.escape(p["score_rationale"]) + '</span></div>\n'
        cards_html += '          <div class="paper-summary">' + html_mod.escape(p["summary"]) + '</div>\n'
        cards_html += '          <div class="post-angle"><b>Post angle:</b> ' + html_mod.escape(p["post_angle"]) + '</div>\n'
        cards_html += '        </div>\n'

    # --- build additional list ---
    add_html = ""
    for a in additional:
        add_html += '          <li>\n'
        add_html += '            <div class="add-title"><a href="' + html_mod.escape(a["url"]) + '" target="_blank">' + html_mod.escape(a["title"]) + '</a></div>\n'
        add_html += '            <div class="add-source">' + html_mod.escape(a["source_line"]) + '</div>\n'
        add_html += '          </li>\n'

    page = '<!DOCTYPE html>\n<html lang="en">\n  <head>\n'
    page += '    <meta charset="utf-8">\n'
    page += '    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'
    page += '    <meta name="description" content="' + html_mod.escape(meta_desc) + '" />\n'
    page += '    <meta name="author" content="Allan Andresson Lima Pereira" />\n\n'
    page += '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">\n'
    page += '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">\n'
    page += '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    page += '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    page += '    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
    page += '    <link rel="stylesheet" href="../site.css?v=3">\n\n'
    page += '    <title>GI Oncology Digest — ' + date_nice + ' | Dr. Allan Pereira</title>\n\n'
    page += IIFE_OPEN + '\n\n'

    # Digest CSS (stable)
    page += """    <style>
      .digest-header { background: linear-gradient(135deg, #003366 0%, #00528A 100%); color: #fff; padding: 3rem 0 2.5rem; text-align: center; }
      .digest-header h1 { font-size: 2rem; font-weight: 700; margin-bottom: .25rem; }
      .digest-header .digest-date { font-size: 1rem; color: #99ccff; }
      .digest-header .digest-subtitle { font-size: .85rem; color: #80b3e6; margin-top: .25rem; }
      .digest-content { padding: 2rem 0 3rem; }
      .digest-section-title { font-size: 1.3rem; font-weight: 700; color: #003366; border-bottom: 3px solid #003366; padding-bottom: .5rem; margin: 2rem 0 1.25rem; }
      .digest-section-title:first-child { margin-top: 0; }
      [data-theme="dark"] .digest-section-title { color: #66aadd; border-bottom-color: #66aadd; }
      .paper-card { background: #fff; border: 1px solid #e2e6ea; border-left: 5px solid #003366; border-radius: .4rem; padding: 1.25rem 1.5rem; margin-bottom: 1.25rem; box-shadow: 0 1px 4px rgba(0,0,0,.06); transition: box-shadow .2s; }
      .paper-card:hover { box-shadow: 0 3px 12px rgba(0,0,0,.1); }
      [data-theme="dark"] .paper-card { background: var(--card-bg, #1e2a38); border-color: #2a3a4a; border-left-color: #66aadd; }
      .paper-rank { display: inline-block; background: #003366; color: #fff; font-size: .75rem; font-weight: 700; padding: 2px 10px; border-radius: 3px; margin-bottom: .5rem; }
      .paper-title { font-size: 1.05rem; font-weight: 700; margin-bottom: .35rem; }
      .paper-title a { color: #003366; text-decoration: none; }
      .paper-title a:hover { text-decoration: underline; }
      [data-theme="dark"] .paper-title a { color: #88ccff; }
      .paper-meta { font-size: .8rem; color: #666; margin-bottom: .6rem; }
      .paper-meta b { color: #444; }
      [data-theme="dark"] .paper-meta { color: #aaa; }
      [data-theme="dark"] .paper-meta b { color: #ccc; }
      .score-badge { display: inline-block; background: #007A33; color: #fff; font-size: .75rem; font-weight: 700; padding: 2px 10px; border-radius: 3px; }
      .score-rationale { font-size: .78rem; color: #555; font-style: italic; margin-left: .4rem; }
      [data-theme="dark"] .score-rationale { color: #aaa; }
      .score-line { margin-bottom: .75rem; }
      .paper-summary { font-size: .9rem; margin-bottom: .85rem; }
      .post-angle { background: #EBF5FF; border-left: 3px solid #0052CC; padding: .6rem .85rem; border-radius: 0 5px 5px 0; font-size: .78rem; color: #0052CC; font-style: italic; }
      .post-angle b { font-style: normal; }
      [data-theme="dark"] .post-angle { background: #1a2a3d; color: #88bbee; border-left-color: #4488cc; }
      .additional-list { list-style: none; padding: 0; }
      .additional-list li { padding: .75rem 0; border-bottom: 1px solid #eee; font-size: .9rem; }
      .additional-list li:last-child { border-bottom: none; }
      [data-theme="dark"] .additional-list li { border-bottom-color: #2a3a4a; }
      .add-title a { color: #0052CC; font-weight: 600; text-decoration: none; }
      .add-title a:hover { text-decoration: underline; }
      [data-theme="dark"] .add-title a { color: #88bbee; }
      .add-source { font-size: .8rem; color: #666; margin-top: .15rem; }
      [data-theme="dark"] .add-source { color: #999; }
      .digest-back { display: inline-block; margin: 1.5rem 0 0; font-size: .85rem; }
    </style>
"""
    page += '  </head>\n  <body id="page-top">\n\n'
    page += NAVBAR + '\n\n'

    # Header
    page += '    <section class="digest-header">\n'
    page += '      <div class="container">\n'
    page += '        <h1>GI Oncology Daily Digest</h1>\n'
    page += '        <div class="digest-date">' + html_mod.escape(date_line) + '</div>\n'
    page += '        <div class="digest-subtitle">Curated by Dr. Allan Pereira — Moffitt Cancer Center</div>\n'
    page += '      </div>\n    </section>\n\n'

    # Content
    page += '    <section class="digest-content">\n'
    page += '      <div class="container" style="max-width:800px;">\n'
    page += '        <h2 class="digest-section-title" style="margin-top:0;">Top 5 Papers</h2>\n'
    page += cards_html
    page += '\n        <h2 class="digest-section-title">Additional Papers of Interest</h2>\n'
    page += '        <ol class="additional-list">\n'
    page += add_html
    page += '        </ol>\n\n'
    page += '        <a href="index_digest.html" class="digest-back"><i class="fas fa-arrow-left mr-1"></i> Back to all digests</a>\n'
    page += '      </div>\n    </section>\n\n'

    page += FOOTER_FULL + '\n\n'
    page += BOTTOM_SCRIPTS + '\n'
    page += THEME_TOGGLE_JS + '\n'
    page += '  </body>\n</html>'

    return page


# ===================================================================
#  2. X THREAD HTML (polished card layout)
# ===================================================================
def build_x_thread_html(data):
    """Generate the polished X/Twitter thread draft HTML."""
    date_str = data["date"]
    date_nice = data["date_display"]
    subtitle = data.get("subtitle", "")
    posts = data["x_thread"]  # list of dicts: {label, text, url (optional)}

    subtitle_line = "GI Oncology Digest — " + date_nice
    if subtitle:
        subtitle_line += " — " + subtitle

    digest_url = "https://allanatal.github.io/my-website/digests/digest-" + date_str + ".html"

    page = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    page += '  <meta charset="utf-8">\n'
    page += '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    page += '  <title>X Thread Draft — ' + date_nice + ' | GI Oncology Digest</title>\n'
    page += """  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f7fa; color: #1a1a2e; padding: 0; }
    .header { background: linear-gradient(135deg, #003366 0%, #00528A 100%); color: #fff; padding: 2rem 1.5rem; text-align: center; }
    .header h1 { font-size: 1.5rem; font-weight: 700; margin-bottom: .25rem; }
    .header .subtitle { font-size: .9rem; color: #99ccff; }
    .header .instructions { font-size: .8rem; color: #80b3e6; margin-top: .75rem; line-height: 1.4; }
    .container { max-width: 680px; margin: 0 auto; padding: 1.5rem 1rem; }
    .thread-card { background: #fff; border: 1px solid #e1e4e8; border-radius: 12px; padding: 1.25rem; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,.06); }
    .thread-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: .75rem; padding-bottom: .5rem; border-bottom: 1px solid #f0f0f0; }
    .post-label { font-weight: 700; font-size: .85rem; color: #003366; background: #e8f0fe; padding: 3px 10px; border-radius: 4px; }
    .char-count { font-size: .75rem; color: #888; font-style: italic; }
    .post-text { font-size: .95rem; line-height: 1.55; white-space: pre-wrap; word-wrap: break-word; }
    .post-text a { color: #1da1f2; text-decoration: none; }
    .post-text a:hover { text-decoration: underline; }
    .footer-note { text-align: center; font-size: .8rem; color: #888; margin-top: 1rem; padding: 1rem; }
    @media (prefers-color-scheme: dark) {
      body { background: #0d1117; color: #c9d1d9; }
      .thread-card { background: #161b22; border-color: #30363d; }
      .thread-card-header { border-bottom-color: #21262d; }
      .post-label { background: #1a2a3d; color: #66aadd; }
    }
  </style>
"""
    page += '</head>\n<body>\n'
    page += '  <div class="header">\n'
    page += '    <h1>X Thread Draft</h1>\n'
    page += '    <div class="subtitle">' + html_mod.escape(subtitle_line) + '</div>\n'
    page += '    <div class="instructions">Review each post below, then copy and paste into X as a thread.<br>Post 1 first, then reply to it with Posts 2-' + str(len(posts)) + ' in order.</div>\n'
    page += '  </div>\n'
    page += '  <div class="container">\n'

    for post in posts:
        text = post["text"]
        label = post["label"]
        url = post.get("url", "")

        # Character count: text only (URLs don't count on X)
        char_count = len(text)

        # Build display text with clickable link appended
        display_text = html_mod.escape(text)
        if url:
            display_text += '\n\n<a href="' + html_mod.escape(url) + '" target="_blank" style="color:#1da1f2;word-break:break-all;">' + html_mod.escape(url) + '</a>'

        page += '\n    <div class="thread-card">\n'
        page += '      <div class="thread-card-header">\n'
        page += '        <span class="post-label">' + html_mod.escape(label) + '</span>\n'
        page += '        <span class="char-count">' + str(char_count) + ' characters</span>\n'
        page += '      </div>\n'
        page += '      <div class="post-text">' + display_text + '</div>\n'
        page += '    </div>\n'

    page += '\n    <div class="footer-note">\n'
    page += '      Generated by Dr. Allan Pereira\'s GI Oncology Digest system<br>\n'
    page += '      Full digest: <a href="' + digest_url + '" style="color:#1da1f2;">' + digest_url + '</a>\n'
    page += '    </div>\n'
    page += '  </div>\n</body>\n</html>'

    return page


# ===================================================================
#  3. FEED UPDATE
# ===================================================================
def update_feed(data):
    """Add today's entry to digest-feed.json (or update if date exists)."""
    date_str = data["date"]
    date_nice = data["date_display"]
    subtitle = data.get("subtitle", "")

    # Use explicit feed_desc if provided, otherwise auto-generate
    if "feed_desc" in data and data["feed_desc"]:
        desc = data["feed_desc"]
    else:
        desc_parts = []
        for p in data["papers"][:5]:
            short = p["title"].split(":")[0] if ":" in p["title"] else p["title"][:60]
            src = p["source"].split("/")[0].strip() if "/" in p["source"] else p["source"]
            desc_parts.append(short + " (" + src + ")")
        desc = ", ".join(desc_parts)

    title = "GI Oncology Digest \u2013 " + date_nice

    entry = {
        "date": date_str,
        "title": title,
        "url": "digests/digest-" + date_str + ".html",
        "desc": desc
    }

    # Load existing feed
    feed = []
    if os.path.exists(FEED_PATH):
        with open(FEED_PATH, "r", encoding="utf-8") as f:
            feed = json.load(f)

    # Remove existing entry for same date if present
    feed = [e for e in feed if e["date"] != date_str]

    # Insert at top
    feed.insert(0, entry)

    with open(FEED_PATH, "w", encoding="utf-8") as f:
        json.dump(feed, f, indent=2)

    return len(feed)


# ===================================================================
#  4. REBUILD INDEX PAGE
# ===================================================================
def rebuild_index():
    """Rebuild index_digest.html from digest-feed.json."""
    with open(FEED_PATH, "r", encoding="utf-8") as f:
        feed = json.load(f)

    entries_html = ""
    for e in feed:
        entries_html += '      <a class="digest-entry" href="' + html_mod.escape(e["url"].replace("digests/", "")) + '">\n'
        entries_html += '        <h3>' + html_mod.escape(e["title"]) + '</h3>\n'
        entries_html += '        <div class="de-date">' + html_mod.escape(e["date"]) + '</div>\n'
        entries_html += '        <div class="de-desc">' + html_mod.escape(e["desc"]) + '</div>\n'
        entries_html += '      </a>\n'

    page = '<!DOCTYPE html>\n<html lang="en">\n  <head>\n'
    page += '    <meta charset="utf-8">\n'
    page += '    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'
    page += '    <meta name="description" content="GI Oncology Daily Digest Archive — Dr. Allan Pereira" />\n'
    page += '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">\n'
    page += '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">\n'
    page += '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    page += '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    page += '    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
    page += '    <link rel="stylesheet" href="../site.css?v=3">\n'
    page += '    <title>GI Oncology Digest Archive | Dr. Allan Pereira</title>\n'
    page += IIFE_OPEN + '\n'
    page += """    <style>
      .archive-header { background: linear-gradient(135deg, #003366 0%, #00528A 100%); color: #fff; padding: 3rem 0 2.5rem; text-align: center; }
      .archive-header h1 { font-size: 2rem; font-weight: 700; }
      .archive-header p { color: #99ccff; }
      .digest-list { max-width: 800px; margin: 2rem auto 3rem; }
      .digest-entry { display: block; background: #fff; border: 1px solid #e2e6ea; border-left: 5px solid #003366; border-radius: .4rem; padding: 1rem 1.25rem; margin-bottom: 1rem; text-decoration: none; color: inherit; transition: box-shadow .2s; }
      .digest-entry:hover { box-shadow: 0 3px 12px rgba(0,0,0,.1); text-decoration: none; color: inherit; }
      [data-theme="dark"] .digest-entry { background: var(--card-bg, #1e2a38); border-color: #2a3a4a; border-left-color: #66aadd; }
      .digest-entry h3 { font-size: 1.05rem; font-weight: 700; color: #003366; margin-bottom: .25rem; }
      [data-theme="dark"] .digest-entry h3 { color: #88ccff; }
      .digest-entry .de-date { font-size: .8rem; color: #666; }
      [data-theme="dark"] .digest-entry .de-date { color: #aaa; }
      .digest-entry .de-desc { font-size: .85rem; color: #555; margin-top: .35rem; }
      [data-theme="dark"] .digest-entry .de-desc { color: #999; }
    </style>
"""
    page += '  </head>\n  <body id="page-top">\n'
    page += NAVBAR + '\n'
    page += '    <section class="archive-header">\n'
    page += '      <div class="container">\n'
    page += '        <h1>GI Oncology Digest Archive</h1>\n'
    page += '        <p>Daily curated research by Dr. Allan Pereira</p>\n'
    page += '      </div>\n    </section>\n'
    page += '    <div class="container digest-list">\n'
    page += entries_html
    page += '    </div>\n'
    page += FOOTER_MINIMAL + '\n'
    page += BOTTOM_SCRIPTS + '\n'
    page += THEME_TOGGLE_JS + '\n'
    page += '  </body>\n</html>'

    index_path = os.path.join(DIGESTS_DIR, "index_digest.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(page)

    return len(feed)


# ===================================================================
#  MAIN
# ===================================================================
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 digest_engine.py <path/to/data.json>")
        sys.exit(1)

    json_path = sys.argv[1]
    # Resolve relative to script dir if not absolute
    if not os.path.isabs(json_path):
        json_path = os.path.join(SCRIPT_DIR, json_path)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    date_str = data["date"]

    # 1. Digest HTML
    digest_html = build_digest_html(data)
    digest_path = os.path.join(DIGESTS_DIR, "digest-" + date_str + ".html")
    with open(digest_path, "w", encoding="utf-8") as f:
        f.write(digest_html)
    print("HTML saved: " + digest_path)

    # 2. X Thread HTML
    thread_html = build_x_thread_html(data)
    thread_path = os.path.join(DIGESTS_DIR, "x-thread-" + date_str + ".html")
    with open(thread_path, "w", encoding="utf-8") as f:
        f.write(thread_html)
    print("X thread saved: " + thread_path)

    # 3. Print character counts
    print("\nCharacter counts per post:")
    for post in data["x_thread"]:
        chars = len(post["text"])
        print("  " + post["label"] + ": " + str(chars) + " chars")

    # 4. Update feed
    feed_count = update_feed(data)
    print("\nFeed updated: " + str(feed_count) + " entries")

    # 5. Rebuild index
    index_count = rebuild_index()
    print("Index rebuilt: " + str(index_count) + " total entries")

    print("\nDone.")


if __name__ == "__main__":
    main()
