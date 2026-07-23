# -*- coding: utf-8 -*-
"""Generate privacy + terms pages for SK / CZ / DE / EN."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root { --primary: #1A56DB; --text: #111827; --text-sec: #6B7280; --border: #E5E7EB; --card: #F9FAFB; }
    body { font-family: 'Inter', sans-serif; color: var(--text); background: #fff; line-height: 1.7; }
    nav { border-bottom: 1px solid var(--border); padding: 0 24px; }
    .nav-inner { max-width: 800px; margin: 0 auto; display: flex; align-items: center; height: 60px; justify-content: space-between; gap: 16px; flex-wrap: wrap; }
    .nav-logo { font-size: 18px; font-weight: 800; color: var(--primary); text-decoration: none; }
    .nav-back { font-size: 14px; color: var(--text-sec); text-decoration: none; }
    .nav-back:hover { color: var(--primary); }
    .lang-mini { display: flex; gap: 8px; font-size: 13px; }
    .lang-mini a { color: var(--text-sec); text-decoration: none; }
    .lang-mini a.active { color: var(--primary); font-weight: 700; }
    .container { max-width: 800px; margin: 0 auto; padding: 60px 24px 80px; }
    h1 { font-size: 36px; font-weight: 800; margin-bottom: 8px; }
    .updated { font-size: 14px; color: var(--text-sec); margin-bottom: 40px; }
    h2 { font-size: 20px; font-weight: 700; margin: 36px 0 12px; color: var(--text); }
    p { font-size: 15px; color: #374151; margin-bottom: 16px; }
    ul { margin: 0 0 16px 20px; }
    ul li { font-size: 15px; color: #374151; margin-bottom: 8px; line-height: 1.6; }
    .highlight {
      background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 12px;
      padding: 20px 24px; margin: 24px 0;
    }
    .highlight p { margin: 0; font-weight: 500; color: var(--primary); }
    footer { border-top: 1px solid var(--border); padding: 32px 24px; text-align: center; font-size: 13px; color: var(--text-sec); }
    footer a { color: inherit; }
"""

# dir "" = root (SK). Others under cz/ de/ en/
PAGES = {
    "sk": {
        "dir": "",
        "home": "/",
        "html_lang": "sk",
        "app": "RýchleÚčto",
        "back": "← Späť na hlavnú stránku",
        "home_label": "Hlavná stránka",
        "privacy_label": "Zásady ochrany súkromia",
        "terms_label": "Obchodné podmienky",
        "updated": "Posledná aktualizácia: 20. júla 2026",
        "privacy_title": "Zásady ochrany súkromia — RýchleÚčto",
        "terms_title": "Obchodné podmienky — RýchleÚčto",
        "privacy_highlight": "RýchleÚčto ukladá všetky vaše dáta výlučne lokálne v telefóne. Neposielajú sa žiadne osobné údaje na naše servery ani tretím stranám.",
        "privacy_body": """
  <h2>1. Prevádzkovateľ</h2>
  <p>Prevádzkovateľom aplikácie RýchleÚčto je:</p>
  <p><strong>Joy IT Solution s.r.o.</strong><br/>
  Slovenská republika<br/>
  Email: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>

  <h2>2. Aké dáta aplikácia používa</h2>
  <p>Aplikácia RýchleÚčto pracuje s nasledovnými typmi dát:</p>
  <ul>
    <li><strong>Fotografie dokladov</strong> — faktúry, bločky a paragóny, ktoré používateľ odfotografuje alebo nahrá</li>
    <li><strong>Rozpoznaný text</strong> — výsledky OCR spracovania fotografií (názov dodávateľa, suma, dátum, IČO)</li>
    <li><strong>Nastavenia aplikácie</strong> — názov firmy alebo živnosti, email účtovnej firmy, jazyk a formát dátumu</li>
    <li><strong>História dokladov</strong> — záznamy spracovaných dokladov uložené v lokálnej databáze</li>
    <li><strong>Stav predplatného</strong> — informácia o skúšobnej dobe a predplatnom spravovaná cez Apple App Store / Google Play</li>
  </ul>

  <h2>3. Kde sú dáta uložené</h2>
  <p><strong>Všetky dáta sú uložené výlučne lokálne v telefóne používateľa.</strong> Aplikácia nepoužíva žiadny cloudový úložný priestor, server ani vzdialenú databázu prevádzkovanú spoločnosťou Joy IT Solution s.r.o.</p>
  <p>Dáta sú uložené v:</p>
  <ul>
    <li>Lokálnej SQLite databáze aplikácie</li>
    <li>Lokálnom úložisku súborov telefónu (fotografie a exporty)</li>
    <li>SharedPreferences / UserDefaults (nastavenia aplikácie)</li>
  </ul>

  <h2>4. Zdieľanie dát s tretími stranami</h2>
  <p>Aplikácia komunikuje s nasledovnými externými službami:</p>
  <ul>
    <li><strong>Finančná správa SR (eKasa API)</strong> — pri skenovaní QR kódu z bločku sa odošle identifikátor dokladu na overenie. Táto komunikácia prebieha priamo so štátnym systémom a neobsahuje osobné údaje používateľa.</li>
    <li><strong>Email klient zariadenia</strong> — pri odoslaní mesačného balíka sa otvorí emailový klient s pripravenou správou. Odoslanie emailu je plne v réžii používateľa.</li>
    <li><strong>Apple App Store / Google Play</strong> — platby a správa predplatného prebiehajú cez obchod s aplikáciami. Joy IT Solution s.r.o. neprijíma ani neukladá údaje o platobnej karte.</li>
  </ul>
  <p>Aplikácia <strong>neposiela žiadne osobné údaje</strong> spoločnosti Joy IT Solution s.r.o. ani analytickým / reklamným tretím stranám.</p>

  <h2>5. Oprávnenia aplikácie</h2>
  <p>Aplikácia požaduje nasledovné oprávnenia:</p>
  <ul>
    <li><strong>Kamera</strong> — na fotografovanie dokladov</li>
    <li><strong>Úložisko / Galéria</strong> — na nahrávanie existujúcich fotografií a PDF súborov</li>
    <li><strong>Internet</strong> — na overenie QR kódov eKasa a na nákup / obnovu predplatného</li>
  </ul>

  <h2>6. Vymazanie dát</h2>
  <p>Všetky dáta môžete kedykoľvek vymazať:</p>
  <ul>
    <li>Priamo v aplikácii (výber a vymazanie dokladov)</li>
    <li>Odinštalovaním aplikácie — všetky lokálne dáta budú trvalo vymazané</li>
  </ul>

  <h2>7. Deti</h2>
  <p>Aplikácia RýchleÚčto je určená výlučne pre osoby staršie ako 18 rokov (podnikateľov). Vedome nezbierame žiadne informácie od detí.</p>

  <h2>8. Zmeny zásad</h2>
  <p>O akýchkoľvek podstatných zmenách týchto zásad budeme informovať prostredníctvom aktualizácie aplikácie alebo na tejto stránke.</p>

  <h2>9. Kontakt</h2>
  <p>Ak máte otázky týkajúce sa ochrany súkromia, kontaktujte nás:</p>
  <p>📧 <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
        "terms_highlight": "Používaním aplikácie RýchleÚčto súhlasíte s týmito obchodnými podmienkami. Predplatné sa spravuje cez App Store alebo Google Play.",
        "terms_body": """
  <h2>1. Prevádzkovateľ</h2>
  <p>Službu RýchleÚčto poskytuje <strong>Joy IT Solution s.r.o.</strong>, Slovenská republika.
  Kontakt: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a>.</p>

  <h2>2. Popis služby</h2>
  <p>RýchleÚčto je mobilná aplikácia na skenovanie dokladov (faktúry, bločky), lokálne OCR spracovanie,
  organizáciu dokladov a export / odoslanie balíka účtovnej firme. Dáta sa spracúvajú lokálne v zariadení používateľa.</p>

  <h2>3. Licencia na používanie</h2>
  <p>Udeľujeme vám osobnú, nevýhradnú, neprenosnú licenciu na používanie aplikácie na kompatibilnom zariadení
  v súlade s týmito podmienkami a pravidlami App Store / Google Play. Aplikáciu nesmiete spätne analyzovať,
  upravovať, ďalej predávať ani používať na nezákonné účely.</p>

  <h2>4. Predplatné a platby</h2>
  <ul>
    <li>Aplikácia môže zahŕňať bezplatnú skúšobnú dobu (napr. 30 dní) a následné predplatné: ročné (napr. 9,99€ / 50 dokladov za rok) alebo mesačné neobmedzené (napr. 4,99€).</li>
    <li>Aktuálna cena a dĺžka skúšobnej doby sú uvedené v App Store / Google Play v čase nákupu.</li>
    <li>Platba sa účtuje cez účet Apple ID alebo Google účet. Joy IT Solution s.r.o. neprijíma údaje o platobnej karte.</li>
    <li>Predplatné sa automaticky obnovuje, pokiaľ ho nezrušíte najmenej 24 hodín pred koncom aktuálneho obdobia.</li>
    <li>Predplatné môžete spravovať a zrušiť v nastaveniach App Store alebo Google Play.</li>
  </ul>

  <h2>5. Zodpovednosť používateľa</h2>
  <p>Zodpovedáte za správnosť nahraných dokladov a za dodržiavanie účtovných a daňových povinností.
  Aplikácia je pomocný nástroj a nenahrádza kvalifikovaného účtovníka ani daňového poradcu.</p>

  <h2>6. Dostupnosť a zmeny</h2>
  <p>Usilujeme sa o spoľahlivú funkčnosť aplikácie, no negarantujeme nepretržitú dostupnosť bez výpadkov.
  Funkcie môžeme aktualizovať, meniť alebo ukončiť s primeraným ohľadom na používateľov.</p>

  <h2>7. Obmedzenie zodpovednosti</h2>
  <p>V maximálnom rozsahu povolenom právom nenesie Joy IT Solution s.r.o. zodpovednosť za nepriame,
  náhodné alebo následné škody, stratu dát alebo ušlý zisk vzniknutý používaním alebo nemožnosťou používať aplikáciu.
  Odporúčame pravidelne zálohovať dôležité doklady mimo aplikácie.</p>

  <h2>8. Ukončenie</h2>
  <p>Môžete prestať aplikáciu používať kedykoľvek (vrátane odinštalovania a zrušenia predplatného).
  Pri porušení týchto podmienok môžeme prístup k plateným funkciám obmedziť v súlade s pravidlami obchodov s aplikáciami.</p>

  <h2>9. Rozhodné právo</h2>
  <p>Tieto podmienky sa riadia právnym poriadkom Slovenskej republiky. Prípadné spory budú riešené príslušnými súdmi SR,
  pokiaľ kogentné právne predpisy nestanovujú inak.</p>

  <h2>10. Kontakt</h2>
  <p>Otázky k podmienkám: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
    },
    "cs": {
        "dir": "cz",
        "home": "/cz/",
        "html_lang": "cs",
        "app": "ÚčtoSkenExport",
        "back": "← Zpět na hlavní stránku",
        "home_label": "Hlavní stránka",
        "privacy_label": "Zásady ochrany soukromí",
        "terms_label": "Obchodní podmínky",
        "updated": "Poslední aktualizace: 20. července 2026",
        "privacy_title": "Zásady ochrany soukromí — ÚčtoSkenExport",
        "terms_title": "Obchodní podmínky — ÚčtoSkenExport",
        "privacy_highlight": "ÚčtoSkenExport ukládá všechna vaše data výhradně lokálně v telefonu. Neodesílají se žádné osobní údaje na naše servery ani třetím stranám.",
        "privacy_body": """
  <h2>1. Provozovatel</h2>
  <p>Provozovatelem aplikace ÚčtoSkenExport je:</p>
  <p><strong>Joy IT Solution s.r.o.</strong><br/>
  Slovenská republika<br/>
  Email: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>

  <h2>2. Jaká data aplikace používá</h2>
  <p>Aplikace ÚčtoSkenExport pracuje s následujícími typy dat:</p>
  <ul>
    <li><strong>Fotografie dokladů</strong> — faktury a účtenky, které uživatel vyfotí nebo nahraje</li>
    <li><strong>Rozpoznaný text</strong> — výsledky OCR zpracování fotografií (název dodavatele, částka, datum, IČO)</li>
    <li><strong>Nastavení aplikace</strong> — název firmy nebo živnosti, e-mail účetní firmy, jazyk a formát data</li>
    <li><strong>Historie dokladů</strong> — záznamy zpracovaných dokladů uložené v lokální databázi</li>
    <li><strong>Stav předplatného</strong> — informace o zkušební době a předplatném spravovaná přes Apple App Store / Google Play</li>
  </ul>

  <h2>3. Kde jsou data uložena</h2>
  <p><strong>Všechna data jsou uložena výhradně lokálně v telefonu uživatele.</strong> Aplikace nepoužívá cloudové úložiště, server ani vzdálenou databázi provozovanou společností Joy IT Solution s.r.o.</p>
  <p>Data jsou uložena v:</p>
  <ul>
    <li>Lokální SQLite databázi aplikace</li>
    <li>Lokálním úložišti souborů telefonu (fotografie a exporty)</li>
    <li>SharedPreferences / UserDefaults (nastavení aplikace)</li>
  </ul>

  <h2>4. Sdílení dat s třetími stranami</h2>
  <p>Aplikace komunikuje s následujícími externími službami:</p>
  <ul>
    <li><strong>Finanční správa SR (eKasa API)</strong> — při skenování QR kódu z účtenky se odešle identifikátor dokladu k ověření. Komunikace probíhá přímo se státním systémem a neobsahuje osobní údaje uživatele.</li>
    <li><strong>E-mailový klient zařízení</strong> — při odeslání měsíčního balíčku se otevře e-mailový klient s připravenou zprávou. Odeslání je plně v režii uživatele.</li>
    <li><strong>Apple App Store / Google Play</strong> — platby a správa předplatného probíhají přes obchod s aplikacemi. Joy IT Solution s.r.o. nepřijímá ani neukládá údaje o platební kartě.</li>
  </ul>
  <p>Aplikace <strong>neodesílá žádné osobní údaje</strong> společnosti Joy IT Solution s.r.o. ani analytickým / reklamním třetím stranám.</p>

  <h2>5. Oprávnění aplikace</h2>
  <ul>
    <li><strong>Kamera</strong> — fotografování dokladů</li>
    <li><strong>Úložiště / Galerie</strong> — nahrávání existujících fotografií a PDF</li>
    <li><strong>Internet</strong> — ověření QR kódů eKasa a nákup / obnova předplatného</li>
  </ul>

  <h2>6. Výmaz dat</h2>
  <ul>
    <li>Přímo v aplikaci (výběr a smazání dokladů)</li>
    <li>Odinstalací aplikace — všechna lokální data budou trvale smazána</li>
  </ul>

  <h2>7. Děti</h2>
  <p>Aplikace je určena výhradně osobám starším 18 let (podnikatelům). Vědomě neshromažďujeme informace od dětí.</p>

  <h2>8. Změny zásad</h2>
  <p>O podstatných změnách budeme informovat aktualizací aplikace nebo na této stránce.</p>

  <h2>9. Kontakt</h2>
  <p>📧 <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
        "terms_highlight": "Používáním aplikace ÚčtoSkenExport souhlasíte s těmito obchodními podmínkami. Předplatné se spravuje přes App Store nebo Google Play.",
        "terms_body": """
  <h2>1. Provozovatel</h2>
  <p>Službu ÚčtoSkenExport poskytuje <strong>Joy IT Solution s.r.o.</strong>, Slovenská republika.
  Kontakt: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a>.</p>

  <h2>2. Popis služby</h2>
  <p>ÚčtoSkenExport je mobilní aplikace pro skenování dokladů, lokální OCR zpracování, organizaci dokladů
  a export / odeslání balíčku účetní firmě. Data se zpracovávají lokálně v zařízení uživatele.</p>

  <h2>3. Licence k užívání</h2>
  <p>Udělujeme vám osobní, nevýhradní, nepřenosnou licenci k používání aplikace na kompatibilním zařízení
  v souladu s těmito podmínkami a pravidly App Store / Google Play.</p>

  <h2>4. Předplatné a platby</h2>
  <ul>
    <li>Aplikace může zahrnovat bezplatnou zkušební dobu (např. 30 dní) a následné předplatné: roční (např. 9,99€ / 50 dokladů za rok) nebo měsíční neomezené (např. 4,99€).</li>
    <li>Aktuální cena a délka zkušební doby jsou uvedeny v App Store / Google Play v okamžiku nákupu.</li>
    <li>Platba probíhá přes účet Apple ID nebo Google. Joy IT Solution s.r.o. nepřijímá údaje o platební kartě.</li>
    <li>Předplatné se automaticky obnovuje, pokud jej nezrušíte nejpozději 24 hodin před koncem aktuálního období.</li>
    <li>Předplatné spravujete a rušíte v nastavení App Store nebo Google Play.</li>
  </ul>

  <h2>5. Odpovědnost uživatele</h2>
  <p>Odpovídáte za správnost nahraných dokladů a za plnění účetních a daňových povinností.
  Aplikace je pomocný nástroj a nenahrazuje kvalifikovaného účetního ani daňového poradce.</p>

  <h2>6. Dostupnost a změny</h2>
  <p>Usilujeme o spolehlivou funkčnost, ale negarantujeme nepřetržitou dostupnost bez výpadků.
  Funkce můžeme aktualizovat, měnit nebo ukončit.</p>

  <h2>7. Omezení odpovědnosti</h2>
  <p>V maximálním rozsahu povoleném právem nenese Joy IT Solution s.r.o. odpovědnost za nepřímé,
  náhodné nebo následné škody, ztrátu dat nebo ušlý zisk vzniklé používáním aplikace.
  Doporučujeme pravidelně zálohovat důležité doklady mimo aplikaci.</p>

  <h2>8. Ukončení</h2>
  <p>Aplikaci můžete přestat používat kdykoli (včetně odinstalace a zrušení předplatného).</p>

  <h2>9. Rozhodné právo</h2>
  <p>Tyto podmínky se řídí právním řádem Slovenské republiky, pokud kogentní předpisy nestanoví jinak.</p>

  <h2>10. Kontakt</h2>
  <p><a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
    },
    "de": {
        "dir": "de",
        "home": "/de/",
        "html_lang": "de",
        "app": "SchnellBelegio",
        "back": "← Zurück zur Startseite",
        "home_label": "Startseite",
        "privacy_label": "Datenschutzerklärung",
        "terms_label": "Nutzungsbedingungen",
        "updated": "Zuletzt aktualisiert: 20. Juli 2026",
        "privacy_title": "Datenschutzerklärung — SchnellBelegio",
        "terms_title": "Nutzungsbedingungen — SchnellBelegio",
        "privacy_highlight": "SchnellBelegio speichert alle Ihre Daten ausschließlich lokal auf dem Telefon. Es werden keine personenbezogenen Daten an unsere Server oder an Dritte gesendet.",
        "privacy_body": """
  <h2>1. Verantwortlicher</h2>
  <p>Verantwortlicher für die App SchnellBelegio ist:</p>
  <p><strong>Joy IT Solution s.r.o.</strong><br/>
  Slowakische Republik<br/>
  E-Mail: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>

  <h2>2. Welche Daten die App nutzt</h2>
  <ul>
    <li><strong>Belegfotos</strong> — Rechnungen und Belege, die Sie fotografieren oder hochladen</li>
    <li><strong>Erkannter Text</strong> — OCR-Ergebnisse (Lieferant, Betrag, Datum, UID/IČO)</li>
    <li><strong>App-Einstellungen</strong> — Firmenname, E-Mail der Buchhaltung, Sprache, Datumsformat</li>
    <li><strong>Beleghistorie</strong> — lokal gespeicherte Datensätze</li>
    <li><strong>Abonnementstatus</strong> — Testzeitraum und Abo über Apple App Store / Google Play</li>
  </ul>

  <h2>3. Speicherung</h2>
  <p><strong>Alle Daten werden ausschließlich lokal auf dem Gerät gespeichert.</strong>
  Joy IT Solution s.r.o. betreibt keinen Cloud-Speicher und keine eigene Nutzerdatenbank für App-Inhalte.</p>
  <ul>
    <li>Lokale SQLite-Datenbank</li>
    <li>Lokaler Dateispeicher (Fotos und Exporte)</li>
    <li>SharedPreferences / UserDefaults (Einstellungen)</li>
  </ul>

  <h2>4. Weitergabe an Dritte</h2>
  <ul>
    <li><strong>Finanzverwaltung SK (eKasa-API)</strong> — beim Scannen eines QR-Codes wird eine Belegkennung zur Prüfung gesendet. Es werden keine personenbezogenen Nutzerdaten übermittelt.</li>
    <li><strong>E-Mail-Client des Geräts</strong> — beim Versand des Monats-Pakets öffnet sich der E-Mail-Client; der Versand liegt beim Nutzer.</li>
    <li><strong>Apple App Store / Google Play</strong> — Zahlungen und Aboverwaltung laufen über den Store. Wir speichern keine Kartendaten.</li>
  </ul>
  <p>Die App sendet <strong>keine personenbezogenen Daten</strong> an Joy IT Solution s.r.o. und keine Analyse-/Werbe-SDKs.</p>

  <h2>5. Berechtigungen</h2>
  <ul>
    <li><strong>Kamera</strong> — zum Fotografieren von Belegen</li>
    <li><strong>Fotos / Dateien</strong> — zum Hochladen vorhandener Bilder und PDFs</li>
    <li><strong>Internet</strong> — eKasa-Prüfung und Abokäufe</li>
  </ul>

  <h2>6. Löschung</h2>
  <ul>
    <li>Direkt in der App (Belege löschen)</li>
    <li>Durch Deinstallation — alle lokalen App-Daten werden entfernt</li>
  </ul>

  <h2>7. Kinder</h2>
  <p>Die App richtet sich an Unternehmer ab 18 Jahren. Wir erheben wissentlich keine Daten von Kindern.</p>

  <h2>8. Änderungen</h2>
  <p>Wesentliche Änderungen dieser Erklärung kommunizieren wir per App-Update oder auf dieser Seite.</p>

  <h2>9. Kontakt</h2>
  <p>📧 <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
        "terms_highlight": "Mit der Nutzung von SchnellBelegio akzeptieren Sie diese Nutzungsbedingungen. Abonnements werden über App Store oder Google Play verwaltet.",
        "terms_body": """
  <h2>1. Anbieter</h2>
  <p>Die App SchnellBelegio wird von <strong>Joy IT Solution s.r.o.</strong>, Slowakische Republik, bereitgestellt.
  Kontakt: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a>.</p>

  <h2>2. Leistungsbeschreibung</h2>
  <p>SchnellBelegio ist eine mobile App zum Scannen von Belegen, lokaler OCR-Verarbeitung, Organisation
  und Export/Versand an die Buchhaltung. Die Verarbeitung erfolgt lokal auf dem Gerät.</p>

  <h2>3. Nutzungsrecht</h2>
  <p>Sie erhalten eine persönliche, nicht-exklusive, nicht übertragbare Lizenz zur Nutzung der App
  auf einem kompatiblen Gerät gemäß diesen Bedingungen und den Store-Regeln.</p>

  <h2>4. Abonnement und Zahlung</h2>
  <ul>
    <li>Es kann eine kostenlose Testphase (z. B. 30 Tage) und danach ein Jahresabo (z. B. 9,99€ / 50 Belege pro Jahr) oder ein unbegrenztes Monatsabo (z. B. 4,99€) geben.</li>
    <li>Preis und Testzeitraum sind im App Store / Google Play zum Kaufzeitpunkt ausgewiesen.</li>
    <li>Die Zahlung erfolgt über Apple-ID oder Google-Konto. Wir speichern keine Kartendaten.</li>
    <li>Das Abo verlängert sich automatisch, sofern es nicht mindestens 24 Stunden vor Periodenende gekündigt wird.</li>
    <li>Verwaltung und Kündigung erfolgen in den Einstellungen von App Store oder Google Play.</li>
  </ul>

  <h2>5. Pflichten des Nutzers</h2>
  <p>Sie sind für die Richtigkeit der Belege sowie für Ihre buchhalterischen und steuerlichen Pflichten verantwortlich.
  Die App ersetzt keinen Steuerberater.</p>

  <h2>6. Verfügbarkeit</h2>
  <p>Wir bemühen uns um zuverlässigen Betrieb, garantieren aber keine unterbrechungsfreie Verfügbarkeit.
  Funktionen können aktualisiert, geändert oder eingestellt werden.</p>

  <h2>7. Haftungsbeschränkung</h2>
  <p>Soweit gesetzlich zulässig haftet Joy IT Solution s.r.o. nicht für indirekte oder Folgeschäden,
  Datenverlust oder entgangenen Gewinn. Bitte sichern Sie wichtige Belege zusätzlich außerhalb der App.</p>

  <h2>8. Beendigung</h2>
  <p>Sie können die Nutzung jederzeit beenden (Deinstallation und Abo-Kündigung).</p>

  <h2>9. Anwendbares Recht</h2>
  <p>Es gilt das Recht der Slowakischen Republik, soweit zwingendes Recht nichts anderes verlangt.</p>

  <h2>10. Kontakt</h2>
  <p><a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
    },
    "en": {
        "dir": "en",
        "home": "/en/",
        "html_lang": "en",
        "app": "Scan2Accountant",
        "back": "← Back to home",
        "home_label": "Home",
        "privacy_label": "Privacy policy",
        "terms_label": "Terms of service",
        "updated": "Last updated: 20 July 2026",
        "privacy_title": "Privacy Policy — Scan2Accountant",
        "terms_title": "Terms of Service — Scan2Accountant",
        "privacy_highlight": "Scan2Accountant stores all your data locally on your phone. No personal data is sent to our servers or to third parties.",
        "privacy_body": """
  <h2>1. Controller</h2>
  <p>The controller of the Scan2Accountant app is:</p>
  <p><strong>Joy IT Solution s.r.o.</strong><br/>
  Slovak Republic<br/>
  Email: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>

  <h2>2. Data the app uses</h2>
  <ul>
    <li><strong>Document photos</strong> — invoices and receipts you capture or upload</li>
    <li><strong>Recognized text</strong> — OCR results (supplier, amount, date, company ID)</li>
    <li><strong>App settings</strong> — business name, accountant email, language, date format</li>
    <li><strong>Document history</strong> — records stored in the local database</li>
    <li><strong>Subscription status</strong> — trial and subscription state managed via Apple App Store / Google Play</li>
  </ul>

  <h2>3. Where data is stored</h2>
  <p><strong>All data is stored exclusively on the user’s device.</strong>
  Joy IT Solution s.r.o. does not operate a cloud storage or remote database for your documents.</p>
  <ul>
    <li>Local SQLite database</li>
    <li>Local file storage (photos and exports)</li>
    <li>SharedPreferences / UserDefaults (settings)</li>
  </ul>

  <h2>4. Sharing with third parties</h2>
  <ul>
    <li><strong>Slovak Financial Administration (eKasa API)</strong> — when scanning a receipt QR code, a document identifier is sent for verification. No personal user data is included.</li>
    <li><strong>Device email client</strong> — when sending a monthly package, your email app opens with a prepared message. Sending is controlled by you.</li>
    <li><strong>Apple App Store / Google Play</strong> — payments and subscription management are handled by the store. We do not receive or store card details.</li>
  </ul>
  <p>The app <strong>does not send personal data</strong> to Joy IT Solution s.r.o. or to analytics / advertising partners.</p>

  <h2>5. Permissions</h2>
  <ul>
    <li><strong>Camera</strong> — to photograph documents</li>
    <li><strong>Photos / Files</strong> — to upload existing images and PDFs</li>
    <li><strong>Internet</strong> — eKasa verification and subscription purchases</li>
  </ul>

  <h2>6. Deletion</h2>
  <ul>
    <li>Inside the app (select and delete documents)</li>
    <li>By uninstalling the app — all local app data is permanently removed</li>
  </ul>

  <h2>7. Children</h2>
  <p>Scan2Accountant is intended for adults (business users) aged 18+. We do not knowingly collect information from children.</p>

  <h2>8. Changes</h2>
  <p>Material changes to this policy will be communicated via an app update or on this page.</p>

  <h2>9. Contact</h2>
  <p>📧 <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
        "terms_highlight": "By using Scan2Accountant you agree to these Terms of Service. Subscriptions are managed via the App Store or Google Play.",
        "terms_body": """
  <h2>1. Provider</h2>
  <p>Scan2Accountant is provided by <strong>Joy IT Solution s.r.o.</strong>, Slovak Republic.
  Contact: <a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a>.</p>

  <h2>2. Service description</h2>
  <p>Scan2Accountant is a mobile app for scanning documents, on-device OCR, organizing receipts,
  and exporting / emailing a monthly package to your accountant. Processing happens locally on your device.</p>

  <h2>3. License</h2>
  <p>We grant you a personal, non-exclusive, non-transferable license to use the app on a compatible device
  in accordance with these terms and the App Store / Google Play rules.</p>

  <h2>4. Subscriptions and payments</h2>
  <ul>
    <li>The app may include a free trial (e.g. 30 days) followed by a yearly plan (e.g. €9.99 / 50 documents per year) or an unlimited monthly subscription (e.g. €4.99).</li>
    <li>Current price and trial length are shown in the App Store / Google Play at purchase time.</li>
    <li>Payment is charged to your Apple ID or Google account. We do not receive card details.</li>
    <li>Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period.</li>
    <li>Manage or cancel in App Store or Google Play settings.</li>
  </ul>

  <h2>5. Your responsibilities</h2>
  <p>You are responsible for the accuracy of uploaded documents and for your accounting and tax obligations.
  The app is a helper tool and does not replace a qualified accountant or tax advisor.</p>

  <h2>6. Availability</h2>
  <p>We aim for reliable operation but do not guarantee uninterrupted availability.
  Features may be updated, changed, or discontinued.</p>

  <h2>7. Limitation of liability</h2>
  <p>To the maximum extent permitted by law, Joy IT Solution s.r.o. is not liable for indirect,
  incidental, or consequential damages, data loss, or lost profits arising from use of the app.
  Please keep important documents backed up outside the app.</p>

  <h2>8. Termination</h2>
  <p>You may stop using the app at any time (including uninstalling and cancelling the subscription).</p>

  <h2>9. Governing law</h2>
  <p>These terms are governed by the laws of the Slovak Republic, unless mandatory local law requires otherwise.</p>

  <h2>10. Contact</h2>
  <p><a href="mailto:joyitsolutionsro@gmail.com">joyitsolutionsro@gmail.com</a></p>
""",
    },
}

LANG_LINKS = [
    ("sk", "/", "SK"),
    ("cs", "/cz/", "CZ"),
    ("de", "/de/", "DE"),
    ("en", "/en/", "EN"),
]


def lang_switch(active: str, page: str) -> str:
    """page is 'privacy' or 'terms'."""
    parts = []
    for code, home, label in LANG_LINKS:
        href = f"{home}{page}.html" if home != "/" else f"/{page}.html"
        # For root SK: /privacy.html; for others /cz/privacy.html
        if home == "/":
            href = f"/{page}.html"
        else:
            href = f"{home}{page}.html"
        cls = ' class="active"' if code == active else ""
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<div class="lang-mini">' + "".join(parts) + "</div>"


def render_page(lang: str, kind: str) -> str:
    t = PAGES[lang]
    title = t["privacy_title"] if kind == "privacy" else t["terms_title"]
    h1 = t["privacy_label"] if kind == "privacy" else t["terms_label"]
    highlight = t["privacy_highlight"] if kind == "privacy" else t["terms_highlight"]
    body = t["privacy_body"] if kind == "privacy" else t["terms_body"]
    other_kind = "terms" if kind == "privacy" else "privacy"
    other_label = t["terms_label"] if kind == "privacy" else t["privacy_label"]
    other_href = f"{other_kind}.html"

    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="alternate" hreflang="sk" href="https://www.rychleucto.sk/{kind}.html" />
  <link rel="alternate" hreflang="cs" href="https://www.rychleucto.sk/cz/{kind}.html" />
  <link rel="alternate" hreflang="de" href="https://www.rychleucto.sk/de/{kind}.html" />
  <link rel="alternate" hreflang="en" href="https://www.rychleucto.sk/en/{kind}.html" />
  <link rel="alternate" hreflang="x-default" href="https://www.rychleucto.sk/{kind}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>{CSS}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="{t['home']}" class="nav-logo">{t['app']}</a>
    {lang_switch(lang, kind)}
    <a href="{t['home']}" class="nav-back">{t['back']}</a>
  </div>
</nav>

<div class="container">
  <h1>{h1}</h1>
  <div class="updated">{t['updated']}</div>

  <div class="highlight">
    <p>{highlight}</p>
  </div>
{body}
</div>

<footer>
  © 2026 {t['app']} — Joy IT Solution s.r.o. &nbsp;|&nbsp;
  <a href="{t['home']}">{t['home_label']}</a> &nbsp;|&nbsp;
  <a href="{other_href}">{other_label}</a>
</footer>

</body>
</html>
"""


def main() -> None:
    for lang, t in PAGES.items():
        out_dir = ROOT / t["dir"] if t["dir"] else ROOT
        out_dir.mkdir(parents=True, exist_ok=True)
        for kind in ("privacy", "terms"):
            path = out_dir / f"{kind}.html"
            path.write_text(render_page(lang, kind), encoding="utf-8")
            print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
