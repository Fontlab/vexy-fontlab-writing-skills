#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "properdocs==1.6.7",
#   "mkdocs==1.6.1",
#   "mkdocs-materialx==10.1.8",
#   "mkdocs-glightbox==0.5.2",
#   "pymdown-extensions==11.0.1",
#   "Markdown==3.10.2",
#   "mkdocs-material-extensions==1.3.1",
# ]
# ///
# this_file: build.py
"""Build the FontLab writing skills site into docs/.

The site is published at https://fontlab.dev/vexy-fontlab-writing-skills/
by GitHub Pages (main branch, /docs). The configuration mirrors
vexy-fontlab-writing-styleguide/src_docs (ProperDocs + MaterialX + fltheme26),
but every file it needs is embedded here so the build runs from a bare clone.

Markdown is staged in a temporary directory, never inside the repository: a
renamed SKILL.md copy inside the tree would look like a duplicate skill to
`npx skills add`. README.md becomes the home page and each SKILL.md becomes its
folder's index.md, so the skills' relative `references/...` links keep working.

Usage:
    ./build.py           # build docs/
    ./build.py --serve   # live preview on http://127.0.0.1:8000/
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE_URL = "https://fontlab.dev/vexy-fontlab-writing-skills/"
# The site first lived under fl1992mk/; keep that address working.
OLD_PATH = "fl1992mk"

# Skills that are not per-language localization skills, in reading order.
VOICE_SKILLS = [
    "fontlab-neutral",
    "fontlab-marketing",
    "fontlab-technical",
    "fontlab-write",
    "fontlab-rewrite",
    "fontlab-tldr",
    "fontlab-simplify",
    "fontlab-terminology",
    "fontlab-partners",
]
LOCALIZATION_CORE = "fontlab-localization"

REDIRECT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vexy FontLab Writing Skills</title>
    <link rel="canonical" href="{url}">
    <meta http-equiv="refresh" content="0; url=../">
</head>
<body>
    <p><a href="../">Vexy FontLab Writing Skills</a></p>
</body>
</html>
"""

MKDOCS_YML = """\
site_name: Vexy FontLab Writing Skills
site_description: "Agent skills that write in the FontLab house voice."
site_url: {site_url}
site_author: Fontlab Ltd.
repo_url: https://github.com/Fontlab/vexy-fontlab-writing-skills

docs_dir: md
site_dir: {site_dir}

use_directory_urls: true

theme:
  name: materialx
  custom_dir: mk-fontlab
  font: false
  code:
    fold:
      enabled: true
  features:
    - navigation.tabs
    - navigation.top
    - toc.follow
    - content.code.annotate
    - content.code.copy
    - content.code.select
    - content.tabs.link
    - content.footnote.tooltips
    - content.tooltips
  palette:
    - scheme: default
      primary: black
      accent: red

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - meta
  - tables
  - toc:
      permalink: true
      title: Contents
      toc_depth: 3
  - pymdownx.betterem
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.magiclink
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
      clickable_checkbox: false
  - pymdownx.tilde

plugins:
  - search:
      enabled: true
  - glightbox

extra_css:
  - https://i.fontlab.com/fltheme26/1.0.0/components.css
  - https://i.fontlab.com/fltheme26/1.0.0/theme.css

extra_javascript:
  - https://i.fontlab.com/fltheme26/1.0.0/basecoat.js
  - https://i.fontlab.com/fltheme26/1.0.0/theme.js

nav:
{nav}
"""

# Copied from vexy-fontlab-writing-styleguide/src_docs/mk-fontlab/main.html;
# only the site label, site URL and the styleguide-only language CSS differ.
MAIN_HTML = """\
{# this_file: build.py (generated mk-fontlab/main.html) #}
{% extends "base.html" %}

{% block extrahead %}
  <link rel="stylesheet" href="https://use.typekit.net/gav0zux.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Funnel+Display:wght@300..800&family=Funnel+Sans:ital,wght@0,300..800;1,300..800&family=Outfit:wght@100..900&family=REM:ital,wght@0,100..900;1,100..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://i.fontlab.com/fltheme26/1.0.0/editorial/styleguide-vendor.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vexy-hrefc@1.0.7/dist/hrefc.css">
  <link rel="stylesheet" href="https://i.fontlab.com/fltheme26/1.0.0/editorial/fontlab-theme.css">
  <link rel="stylesheet" href="https://i.fontlab.com/fltheme26/1.0.0/editorial/fontlab-materialx.css">
  <link rel="stylesheet" href="https://i.fontlab.com/fltheme26/1.0.0/editorial/fontlab-layout.css">
  <link rel="stylesheet" href="https://i.fontlab.com/fltheme26/1.0.0/editorial/styleguide.css">

  <!-- Restore persisted subtheme + collapsed TOC before paint (avoids flash). -->
  <script>
  (function () {
    var map = { "material-light":"light","material-dark":"dark","miller":"light","retro":"retro","lines":"light" };
    var d = document.documentElement;
    try {
      var t = localStorage.getItem("fontlab-docs-subtheme");
      if (t && map[t]) { d.dataset.theme = map[t]; d.dataset.flSubtheme = t; }
      else { d.dataset.theme = "light"; d.dataset.flSubtheme = "material-light"; t = "material-light"; }
      var menuMap = { "material-light":"dark","material-dark":"flat-dark","miller":"light","retro":"light","lines":"light" };
      d.dataset.flMenu = menuMap[t] || "dark";
      if (localStorage.getItem("fontlab-docs-toc") !== "open") d.classList.add("fl-toc-collapsed");
    } catch (e) { d.dataset.theme = "light"; d.dataset.flSubtheme = "material-light"; d.classList.add("fl-toc-collapsed"); }
  })();
  </script>

  <!-- FontLab menu/footer loader -->
  <script src="https://i.fontlab.com/menu/fontlab.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/vexy-hrefc@1.0.7/dist/hrefc.global.min.js" defer></script>
  <script src="https://i.fontlab.com/fltheme26/1.0.0/editorial/fontlab-theme.js" defer></script>

  <!-- Configure <fontlab-menu>: empty localMenu, search source is 'marketing'. -->
  <script>
  (function () {
    function apply() {
      var el = document.querySelector('fontlab-menu');
      if (!el) return;
      el.config = {
        localMenu: [],
        search: { from: 'marketing' }
      };
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', apply);
    } else { apply(); }
  })();
  </script>
{% endblock %}

{% block header %}
  {# MaterialX's bundle expects a [data-md-component=header] and initializes
     search inside it. Keep a hidden header that carries the search markup;
     fontlab-theme.js then relocates the live .md-search into the left rail. #}
  <header class="md-header" data-md-component="header" aria-hidden="true">
    {% include "partials/search.html" %}
  </header>
  <fontlab-menu
    mode="dark"
    site-label="Writing skills"
    site-url="{{ config.site_url }}"></fontlab-menu>
{% endblock %}

{% block site_nav %}
  {% if nav %}
    {% if page.meta and page.meta.hide %}
      {% set hidden = "hidden" if "navigation" in page.meta.hide %}
    {% endif %}
    <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation" {{ hidden }}>
      <div class="md-sidebar__scrollwrap">
        <div class="md-sidebar__inner">
          {% include "partials/nav.html" %}
        </div>
      </div>
    </div>
  {% endif %}
  {% if "toc.integrate" not in features %}
    {% if page.meta and page.meta.hide %}
      {% set hidden = "hidden" if "toc" in page.meta.hide %}
    {% endif %}
    <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" {{ hidden }}>
      <div class="md-sidebar__scrollwrap">
        <div class="md-sidebar__inner">
          {% include "partials/toc.html" %}
        </div>
      </div>
    </div>
  {% endif %}

  <!-- Subtheme switcher: injected into the tabs nav (div[4]/nav) by fontlab-theme.js -->
  <template id="fl-theme-menu-template">
    <div class="fl-theme" data-fl-theme>
      <button class="fl-theme__btn" type="button" aria-expanded="false" aria-controls="fl-theme-options" aria-label="Change subtheme" title="Subtheme">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 0 0 18c1.66 0 1.5-2 2.5-2.5s2.5.5 2.5-1.5c0-2-2-2-2-3.5s2-1.5 2-3S16 3 12 3z"/>
        </svg>
      </button>
      <div class="fl-theme__pop" id="fl-theme-options" aria-label="Subtheme choices" hidden>
        <button class="fl-theme__opt" type="button" aria-pressed="false" data-theme="material-light">Light</button>
        <button class="fl-theme__opt" type="button" aria-pressed="false" data-theme="material-dark">Dark</button>
        <button class="fl-theme__opt" type="button" aria-pressed="false" data-theme="miller">Miller · newspaper</button>
        <button class="fl-theme__opt" type="button" aria-pressed="false" data-theme="retro">Retro · warm</button>
        <button class="fl-theme__opt" type="button" aria-pressed="false" data-theme="lines">Vexy Lines · vivid</button>
      </div>
    </div>
  </template>

  <!-- Right TOC expand/collapse handle: injected into the secondary sidebar by fontlab-theme.js -->
  <template id="fl-toc-toggle-template">
    <button class="fl-toc-toggle" type="button" aria-expanded="false" aria-label="Toggle on-page contents" data-fl-toc-toggle>
      <span class="fl-toc-toggle__icon" aria-hidden="true"></span>
    </button>
  </template>
{% endblock %}

{% block footer %}
  <fontlab-footer mode="dark"></fontlab-footer>
{% endblock %}
"""

# Copied verbatim from vexy-fontlab-writing-styleguide/src_docs/mk-fontlab/partials/nav-item.html.
NAV_ITEM_HTML = """\
{#-
  this_file: build.py (generated mk-fontlab/partials/nav-item.html)
  Based on mkdocs-materialx 10.1.8 material/templates/partials/nav-item.html.
  The active-page label reuses base.html's single __toc state control.
-#}
{% macro render_status(nav_item, type) %}
  {% set class = "md-status md-status--" ~ type %}
  {% if config.extra.status and config.extra.status[type] %}
    <span class="{{ class }}" title="{{ config.extra.status[type] }}">
    </span>
  {% else %}
    <span class="{{ class }}"></span>
  {% endif %}
{% endmacro %}
{% macro render_title(nav_item) %}
  {% if nav_item.typeset %}
    <span class="md-typeset">
      {{ nav_item.typeset.title }}
    </span>
  {% else %}
    {{ nav_item.title }}
  {% endif %}
{% endmacro %}
{% macro render_content(nav_item, ref) %}
  {% set ref = ref or nav_item %}
  {% if nav_item.meta and nav_item.meta.icon %}
    {% include ".icons/" ~ nav_item.meta.icon ~ ".svg" %}
  {% endif %}
  <span class="md-ellipsis">
    {{ render_title(ref) }}
    {% if nav_item.meta and nav_item.meta.subtitle %}
      <br>
      <small>{{ nav_item.meta.subtitle }}</small>
    {% endif %}
  </span>
  {% if nav_item.meta and nav_item.encrypted %}
    {{ render_status(nav_item, "encrypted") }}
  {% endif %}
  {% if nav_item.meta and nav_item.meta.status %}
    {{ render_status(nav_item, nav_item.meta.status) }}
  {% endif %}
{% endmacro %}
{% macro render_pruned(nav_item, ref) %}
  {% set ref = ref or nav_item %}
  {% set first = nav_item.children | first %}
  {% if first and first.children %}
    {{ render_pruned(first, ref) }}
  {% else %}
    <a href="{{ first.url | url }}" class="md-nav__link">
      {{ render_content(ref) }}
      {% if nav_item.children | length > 0 %}
        <span class="md-nav__icon md-icon"></span>
      {% endif %}
    </a>
  {% endif %}
{% endmacro %}
{% macro render(nav_item, path, level, parent) %}
  {% set class = "md-nav__item" %}
  {% if nav_item.active %}
    {% set class = class ~ " md-nav__item--active" %}
  {% endif %}
  {% if nav_item.pages %}
    {% if page in nav_item.pages %}
      {% set nav_item = page %}
    {% endif %}
  {% endif %}
  {% if nav_item.children %}
    {% set _ = namespace(index = none) %}
    {% if "navigation.indexes" in features %}
      {% for item in nav_item.children %}
        {% if item.is_index and _.index is none %}
          {% set _.index = item %}
        {% endif %}
      {% endfor %}
    {% endif %}
    {% set index = _.index %}
    {% if "navigation.tabs" in features %}
      {% if level == 1 and nav_item.active %}
        {% set class = class ~ " md-nav__item--section" %}
        {% set is_section = true %}
      {% endif %}
      {% if "navigation.sections" in features %}
        {% if level == 2 and parent.active %}
          {% set class = class ~ " md-nav__item--section" %}
          {% set is_section = true %}
        {% endif %}
      {% endif %}
    {% elif "navigation.sections" in features %}
      {% if level == 1 %}
        {% set class = class ~ " md-nav__item--section" %}
        {% set is_section = true %}
      {% endif %}
    {% endif %}
    {% if "navigation.prune" in features %}
      {% if not is_section and not nav_item.active %}
        {% set class = class ~ " md-nav__item--pruned" %}
        {% set is_pruned = true %}
      {% endif %}
    {% endif %}
    <li class="{{ class }} md-nav__item--nested">
      {% if not is_pruned %}
        {% set checked = "checked" if nav_item.active %}
        {% if "navigation.expand" in features and not checked %}
          {% set indeterminate = "md-toggle--indeterminate" %}
        {% endif %}
        <input class="md-nav__toggle md-toggle {{ indeterminate }}" type="checkbox" id="{{ path }}" {{ checked }}>
        {% if not index %}
          {% set tabindex = "0" if not is_section %}
          <label class="md-nav__link" for="{{ path }}" id="{{ path }}_label" tabindex="{{ tabindex }}">
            {{ render_content(nav_item) }}
            <span class="md-nav__icon md-icon"></span>
          </label>
        {% else %}
          {% set class = "md-nav__link--active" if index == page %}
          <div class="md-nav__link md-nav__container">
            <a href="{{ index.url | url }}" class="md-nav__link {{ class }}">
              {{ render_content(index, nav_item) }}
            </a>
            {% if nav_item.children | length > 1 %}
              {% set tabindex = "0" if not is_section %}
              <label class="md-nav__link {{ class }}" for="{{ path }}" id="{{ path }}_label" tabindex="{{ tabindex }}">
                <span class="md-nav__icon md-icon"></span>
              </label>
            {% endif %}
          </div>
        {% endif %}
        <nav class="md-nav" data-md-level="{{ level }}" aria-labelledby="{{ path }}_label" aria-expanded="{{ nav_item.active | tojson }}">
          <label class="md-nav__title" for="{{ path }}">
            <span class="md-nav__icon md-icon"></span>
            {{ render_title(nav_item) }}
          </label>
          <ul class="md-nav__list">
            {% for item in nav_item.children %}
              {% if not index or item != index %}
                {{ render(item, path ~ "_" ~ loop.index, level + 1, nav_item) }}
              {% endif %}
            {% endfor %}
          </ul>
        </nav>
      {% else %}
        {{ render_pruned(nav_item) }}
      {% endif %}
    </li>
  {% elif nav_item == page %}
    <li class="{{ class }}">
      {% set toc = page.toc %}
      {% set first = toc | first %}
      {% if first and first.level == 1 %}
        {% set toc = first.children %}
      {% endif %}
      {% if toc %}
        <label class="md-nav__link md-nav__link--active" for="__toc">
          {{ render_content(nav_item) }}
          <span class="md-nav__icon md-icon"></span>
        </label>
      {% endif %}
      <a href="{{ nav_item.url | url }}" class="md-nav__link md-nav__link--active">
        {{ render_content(nav_item) }}
      </a>
      {% if toc %}
        {% include "partials/toc.html" %}
      {% endif %}
    </li>
  {% else %}
    <li class="{{ class }}">
      <a href="{{ nav_item.url | url }}" class="md-nav__link">
        {{ render_content(nav_item) }}
      </a>
    </li>
  {% endif %}
{% endmacro %}
"""

SKILL_LINK = re.compile(r"\]\(((?:[^)#\s]*/)?)SKILL\.md")
SKILL_CODE_CELL = re.compile(r"^\| `(fontlab-[a-z-]+)` \|", re.MULTILINE)


def skill_dirs() -> list[str]:
    """Return every top-level skill folder name, sorted."""
    return sorted(p.parent.name for p in ROOT.glob("fontlab-*/SKILL.md"))


def page_title(md: Path) -> str:
    """Return a Markdown file's first H1, or its stem when it has none."""
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md.stem


def stage_markdown(stage: Path, skills: list[str]) -> None:
    """Copy README.md and each skill into `stage`, renaming SKILL.md to index.md."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    # Turn the skill names in the README table into links to their pages.
    readme = SKILL_CODE_CELL.sub(lambda m: f"| [`{m[1]}`]({m[1]}/index.md) |", readme)
    (stage / "index.md").write_text(readme, encoding="utf-8")
    for name in skills:
        for src in sorted((ROOT / name).rglob("*.md")):
            rel = src.relative_to(ROOT)
            dest = stage / (rel.parent / "index.md" if src.name == "SKILL.md" else rel)
            dest.parent.mkdir(parents=True, exist_ok=True)
            text = SKILL_LINK.sub(r"](\1index.md", src.read_text(encoding="utf-8"))
            dest.write_text(text, encoding="utf-8")


def skill_section(name: str, indent: str) -> list[str]:
    """Return nav lines for one skill: its page, then its reference pages.

    Titles are explicit because the nav would otherwise show file stems
    ("Index", "Moves") instead of the pages' H1 headings.
    """
    pages = [("Skill", f"{name}/index.md")]
    pages += [
        (page_title(p), p.relative_to(ROOT).as_posix())
        for p in sorted((ROOT / name / "references").glob("*.md"))
    ]
    title = page_title(ROOT / name / "SKILL.md").removeprefix("FontLab localization: ")
    lines = [f'{indent}- "{title}":']
    lines += [f'{indent}    - "{label}": {path}' for label, path in pages]
    return lines


def nav_yaml(skills: list[str]) -> str:
    """Return the `nav:` body: Home, voice skills, then localization."""
    languages = [s for s in skills if s.startswith(f"{LOCALIZATION_CORE}-")]
    other = [s for s in skills if s not in VOICE_SKILLS + [LOCALIZATION_CORE] + languages]
    languages.sort(key=lambda s: page_title(ROOT / s / "SKILL.md"))
    lines = ["  - Home: index.md", "  - Voice skills:"]
    for name in VOICE_SKILLS + other:
        lines += skill_section(name, "      ")
    lines.append("  - Localization:")
    lines += skill_section(LOCALIZATION_CORE, "      ")
    lines.append("      - Languages:")
    for name in languages:
        lines += skill_section(name, "          ")
    return "\n".join(lines)


def write_config(stage: Path, skills: list[str]) -> Path:
    """Write mkdocs.yml and the theme overrides into `stage`; return the config path."""
    partials = stage / "mk-fontlab" / "partials"
    partials.mkdir(parents=True)
    (stage / "mk-fontlab" / "main.html").write_text(MAIN_HTML, encoding="utf-8")
    (partials / "nav-item.html").write_text(NAV_ITEM_HTML, encoding="utf-8")
    config = stage / "mkdocs.yml"
    config.write_text(
        MKDOCS_YML.format(site_url=SITE_URL, site_dir=DOCS, nav=nav_yaml(skills)),
        encoding="utf-8",
    )
    return config


def source_date_epoch() -> str:
    """Return the last commit time so sitemap dates do not change on every build."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    return out.stdout.strip() or "0"


def main(argv: list[str]) -> int:
    skills = skill_dirs()
    if LOCALIZATION_CORE not in skills:
        sys.exit(f"build.py: {LOCALIZATION_CORE}/SKILL.md not found under {ROOT}")
    serve = "--serve" in argv
    with tempfile.TemporaryDirectory(prefix="skills-site-") as tmp:
        stage = Path(tmp)
        (stage / "md").mkdir()
        stage_markdown(stage / "md", skills)
        config = write_config(stage, skills)
        if not serve:
            # docs/ holds only build output, so start from an empty tree.
            shutil.rmtree(DOCS, ignore_errors=True)
        command = ["serve"] if serve else ["build", "--strict"]
        env = os.environ | {"SOURCE_DATE_EPOCH": source_date_epoch()}
        cmd = [sys.executable, "-m", "properdocs", *command, "-f", str(config)]
        code = subprocess.run(cmd, env=env, check=False).returncode
    if code == 0 and not serve:
        (DOCS / ".nojekyll").write_text("", encoding="utf-8")
        old = DOCS / OLD_PATH
        old.mkdir()
        (old / "index.html").write_text(REDIRECT_HTML.format(url=SITE_URL), encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
