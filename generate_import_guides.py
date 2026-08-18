# -*- coding: utf-8 -*-
"""Generate SK import-guide hub + software pages for rychleucto.sk."""
from __future__ import annotations

from pathlib import Path

from ga import head_snippet as ga_head

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "navod-importu"
# Absolute paths so pages keep the main site stylesheet even under /navod-importu/
ASSET = "/assets/import-guides"
CSS = "/styles.css"
JS = "/site.js"

APP = "RýchleÚčto"
TRADEMARK = (
    "Názvy MRP, POHODA, Money S3 a OMEGA sú ochrannými známkami ich príslušných "
    "vlastníkov. Sú uvedené výlučne na označenie kompatibility aplikácie s "
    "podporovanými formátmi importu."
)

GUIDES = [
    {
        "slug": "money-s3",
        "name": "Money S3",
        "title": "Import do Money S3 — RýchleÚčto",
        "description": "Návod na import dokladov z RýchleÚčto do Money S3: faktúry prijaté, faktúry vystavené a pokladničné doklady.",
        "card_p": "Faktúry prijaté, faktúry vystavené a pokladničné doklady — krok za krokom so screenshotmi.",
        "file": "money-s3.html",
        "zip_hint": "V mesačnom ZIP nájdete súbory v priečinku <code>money_s3/</code>.",
    },
    {
        "slug": "mrp",
        "name": "MRP",
        "title": "Import do MRP — RýchleÚčto",
        "description": "Návod na import faktúr z RýchleÚčto do MRP XML 2.0.",
        "card_p": "Import faktúr prijatých a vydaných cez MRP XML 2.0.",
        "file": "mrp.html",
        "zip_hint": "V mesačnom ZIP nájdete súbory v priečinku <code>mrp/</code> "
        "(<code>faktury_prijate.xml</code>, <code>faktury_vydane.xml</code>).",
    },
    {
        "slug": "omega",
        "name": "OMEGA",
        "title": "Import do OMEGA — RýchleÚčto",
        "description": "Návod na import dokladov z RýchleÚčto do OMEGA (TXT).",
        "card_p": "Import cez TXT súbor — 5 krokov so screenshotmi.",
        "file": "omega.html",
        "zip_hint": "V mesačnom ZIP nájdete súbor <code>omega_import.txt</code>.",
    },
    {
        "slug": "pohoda",
        "name": "POHODA",
        "title": "Import do POHODA — RýchleÚčto",
        "description": "Návod na XML import dokladov z RýchleÚčto do programu POHODA.",
        "card_p": "XML spracovanie (dataPack) — zahájenie importu a kontrola výsledku.",
        "file": "pohoda.html",
        "zip_hint": "V mesačnom ZIP nájdete súbor <code>pohoda_import.xml</code>.",
    },
]


def images_html(folder: str, count: int, alt_prefix: str) -> str:
    figs = []
    for n in range(1, count + 1):
        src = f"{ASSET}/{folder}/{n:02d}.png"
        alt = f"{alt_prefix} — krok {n}"
        figs.append(
            f"""      <figure class="guide-shot">
        <a href="{src}" class="shot-link" data-lightbox aria-label="{alt}">
          <img src="{src}" alt="{alt}" loading="lazy" />
        </a>
        <figcaption>Krok {n}</figcaption>
      </figure>"""
        )
    return '<div class="guide-shots">\n' + "\n".join(figs) + "\n    </div>"


def money_s3_sections() -> str:
    sections = [
        ("faktury-prijate", "1. Faktúry prijaté", "Faktúry prijaté"),
        ("faktury-vystavene", "2. Faktúry vystavené", "Faktúry vystavené"),
        ("pokladnicne-doklady", "3. Pokladničné doklady", "Pokladničné doklady"),
    ]
    blocks = []
    for folder, heading, alt in sections:
        blocks.append(
            f"""  <section class="guide-section" id="{folder}">
    <h2>{heading}</h2>
    {images_html(f"money-s3/{folder}", 6, alt)}
  </section>"""
        )
    return "\n".join(blocks)


def mrp_body() -> str:
    return f"""  <section class="guide-section">
    <h2>Postup importu</h2>
    {images_html("mrp", 3, "MRP import")}
    <div class="guide-note">
      <p>Importované faktúry si môžete následne pozrieť ako ste zvyknutí v sekcii <strong>Fakturácia</strong>:</p>
      <ul>
        <li><strong>A)</strong> Vydané</li>
        <li><strong>B)</strong> Prijaté</li>
      </ul>
    </div>
  </section>"""


def omega_body() -> str:
    return f"""  <section class="guide-section">
    <h2>Postup importu</h2>
    {images_html("omega", 5, "OMEGA import")}
    <div class="guide-note">
      <p>Importované faktúry si môžete následne pozrieť ako ste zvyknutí v:</p>
      <ul>
        <li><strong>Fakturácia → Odoslané faktúry</strong></li>
        <li><strong>Fakturácia → Došlé faktúry</strong></li>
      </ul>
    </div>
  </section>"""


def pohoda_body() -> str:
    return f"""  <section class="guide-section">
    <h2>Postup importu</h2>
    {images_html("pohoda", 5, "POHODA XML spracovanie")}
    <h2>Zahájenie XML spracovania</h2>
    <p>Na prvej strane sprievodcu najskôr vyberte typ XML spracovania, ktorým je definované, či bude vykonaný XML import/export jedného konkrétneho súboru alebo viacerých súborov. V prípade exportu konkrétneho XML súboru zaškrtnite voľbu <strong>Súbor</strong>. Výberom voľby <strong>Zložka</strong> určíte, že chcete vykonať import alebo export viacerých XML súborov naraz.</p>
    <p>V poli <strong>Vstupný priečinok alebo súbor (request)</strong> zvoľte cestu k XML súborom. V prípade, že ste vybrali možnosť Zložka, skontroluje POHODA všetky XML súbory v tejto zložke, a ak obsahujú platný dataPack, budú spracované.</p>
    <p>XML komunikácia programu POHODA umožňuje aktualizovať i zmazať záznam v programe POHODA.</p>
    <p>V poli <strong>Výstupný priečinok alebo súbor (response)</strong> vyberte cestu k priečinku alebo súboru, kde bude dochádzať k ukladaniu už spracovaných XML súborov. V tomto priečinku môžete nájsť výsledky s exportovanými alebo importovanými dokladmi. Ak cesta pre výstupný priečinok alebo súbor nebude vyplnená, dôjde k vyplneniu tohto údaja automaticky na základe údajov uvedených v poli Vstupný priečinok alebo súbor. V tomto umiestnení sa vytvorí podpriečinok <strong>Response</strong>, v ktorom bude možné nájsť výsledky XML spracovania súborov.</p>
    <p>Ak chcete používať nepovinnú voľbu <strong>Kontrola duplicity dávok</strong>, zaškrtnite ju. POHODA bude kontrolovať, či už zadaný doklad nebol importovaný. Ak áno, import neprebehne a vo výstupnom priečinku alebo súbore dôjde k zobrazeniu hlásenia o duplicite tohto dokladu. Kontrola prebieha na základe atribútu id, elementu dataPack a atribútu id, elementu dataPackItem.</p>
    <h2>Výsledok XML spracovania</h2>
    <p>Na poslednej strane sprievodcu môžete zistiť výsledok XML spracovania a pomocou tlačidla <strong>Otvoriť cieľový priečinok</strong> otvoríte výstupný priečinok (Response), v ktorom sú k dispozícii výsledky XML spracovania.</p>
    <p>Po dokončení sprievodcu importom, resp. exportom XML, je možné zistiť výsledok XML spracovania v agende <strong>XML log</strong>. Tu je možné otvoriť ako cieľový (Response), tak i zdrojový súbor (Request) cez miestnu ponuku.</p>
  </section>"""


def page_shell(
    *,
    title: str,
    description: str,
    canonical: str,
    body: str,
    active_slug: str | None = None,
) -> str:
    return f"""<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{CSS}" />
{ga_head()}
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">{APP}</a>
    <div class="nav-links">
      <a href="/#screenshots">Aplikácia</a>
      <a href="/#funkcie">Funkcie</a>
      <a href="/#ako-to-funguje">Ako to funguje</a>
      <a href="/#kompatibilita">Kompatibilita</a>
      <a href="/navod-importu/" class="active">Návod importu</a>
      <a href="/#cennik">Cenník</a>
      <a href="/#faq">FAQ</a>
      <a href="/privacy.html">Súkromie</a>
    </div>
    <div class="nav-actions">
      <a href="/navod-importu/" class="nav-guides-link">Návod importu</a>
      <a href="/#download" class="btn btn-primary nav-cta-btn">Stiahnuť zadarmo</a>
    </div>
  </div>
</nav>

{body}

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="font-size:20px;font-weight:800;color:white;">{APP}</div>
        <p>Mobilná aplikácia pre živnostníkov a malé firmy. Účtovníctvo za 60 sekúnd mesačne.</p>
      </div>
      <div class="footer-col">
        <h4>Aplikácia</h4>
        <a href="/">Domov</a>
        <a href="/#kompatibilita">Kompatibilita</a>
        <a href="/navod-importu/">Návod importu</a>
      </div>
      <div class="footer-col">
        <h4>Právne</h4>
        <a href="/privacy.html">Zásady ochrany súkromia</a>
        <a href="/terms.html">Obchodné podmienky</a>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 {APP} — Joy IT Solution s.r.o.</div>
      <div>🇸🇰 Slovenská republika</div>
    </div>
    <p class="footer-disclaimer">{TRADEMARK}</p>
  </div>
</footer>

<script src="{JS}" defer></script>
</body>
</html>
"""


def render_hub() -> str:
    cards = []
    for g in GUIDES:
        cards.append(
            f"""      <a class="guide-card" href="{g['file']}">
        <h3>{g['name']}</h3>
        <p>{g['card_p']}</p>
        <span class="guide-card-cta">Otvoriť návod →</span>
      </a>"""
        )
    body = f"""
<div class="guide-hero">
  <div class="section-inner">
    <div class="section-label">Pre účtovníkov</div>
    <h1 class="section-title">Návod importu pre účtovníkov</h1>
    <p class="section-sub">Vyberte účtovný softvér — ukážeme vám, ako naimportovať mesačný balík z aplikácie {APP}.</p>
  </div>
</div>

<div class="section-inner guide-hub">
  <div class="guide-grid">
{chr(10).join(cards)}
  </div>
  <p class="trademark-disclaimer" style="margin-top:40px;">{TRADEMARK}</p>
</div>
"""
    return page_shell(
        title="Návod importu pre účtovníkov — RýchleÚčto",
        description="Návody na import mesačného balíka z RýchleÚčto do Money S3, MRP, OMEGA a POHODA.",
        canonical="https://www.rychleucto.sk/navod-importu/",
        body=body,
        active_slug=None,
    )


def render_guide(g: dict, content: str) -> str:
    pills = []
    for o in GUIDES:
        cls = "guide-pill active" if o["slug"] == g["slug"] else "guide-pill"
        pills.append(f'<a href="{o["file"]}" class="{cls}">{o["name"]}</a>')
    others = "".join(pills)
    body = f"""
<div class="guide-hero">
  <div class="section-inner">
    <div class="section-label">Návod importu</div>
    <h1 class="section-title">Import do {g['name']}</h1>
    <p class="section-sub">{g['zip_hint']}</p>
    <div class="guide-pills">
      <a href="/navod-importu/" class="guide-pill">← Všetky softvéry</a>
      {others}
    </div>
  </div>
</div>

<div class="section-inner guide-content">
{content}
</div>
"""
    return page_shell(
        title=g["title"],
        description=g["description"],
        canonical=f"https://www.rychleucto.sk/navod-importu/{g['file']}",
        body=body,
        active_slug=g["slug"],
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(render_hub(), encoding="utf-8")
    print("wrote navod-importu/index.html")

    bodies = {
        "money-s3": money_s3_sections(),
        "mrp": mrp_body(),
        "omega": omega_body(),
        "pohoda": pohoda_body(),
    }
    for g in GUIDES:
        out = OUT / g["file"]
        out.write_text(render_guide(g, bodies[g["slug"]]), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
