# -*- coding: utf-8 -*-
"""Generate SK / CZ / DE / EN landing pages for rychleucto.sk"""
from pathlib import Path

from ga import head_snippet as ga_head

ROOT = Path(__file__).resolve().parent

LANGS = {
    "sk": {
        "code": "sk",
        "html_lang": "sk",
        "dir": "",
        "prefix": "",
        "path": "/",
        "app": "RýchleÚčto",
        "shot_dir": "sk",
        "title": "RýchleÚčto — Doklady pre účtovníka za 60 sekúnd",
        "description": "RýchleÚčto je mobilná aplikácia pre živnostníkov a malé firmy. Odfoťte doklady a pošlite ich svojmu účtovníkovi — export do POHODA, Money S3, MRP a OMEGA.",
        "nav_features": "Funkcie",
        "nav_how": "Ako to funguje",
        "nav_pricing": "Cenník",
        "nav_faq": "FAQ",
        "nav_privacy": "Súkromie",
        "nav_screens": "Aplikácia",
        "cta_nav": "Stiahnuť zadarmo",
        "badge": "🇸🇰 Vyvinuté na Slovensku",
        "h1_html": "Doklady pre účtovníka<br/>za <span>60 sekúnd</span>",
        "hero_p": "Odfoťte faktúry a bločky a pošlite ich účtovnej firme, ktorú už máte. Export do POHODA, Money S3, MRP a OMEGA — bez zmeny kancelárie a bez cloudu.",
        "btn_play": "📱 Stiahnuť z Google Play (Android)",
        "btn_ios": "🍎 Stiahnuť z App Store (iPhone)",
        "btn_how": "Ako to funguje?",
        "hero_alt": "RýchleÚčto — náhľad aplikácie",
        "screens_label": "Aplikácia",
        "screens_title": "Pozrite si, ako to vyzerá",
        "screens_sub": "Skutočné obrazovky z aplikácie — od skenovania po mesačný export.",
        "shot_alt": "Náhľad aplikácie {n}",
        "how_label": "Ako to funguje",
        "how_title": "Tri jednoduché kroky",
        "step1_t": "Odfotografujte doklad",
        "step1_p": "Faktúru, bloček alebo paragon. Veľkú faktúru? Spravte viac fotiek po častiach. Alebo naskenujte QR kód z eKasy.",
        "step2_t": "Skontrolujte a potvrďte",
        "step2_p": "Aplikácia automaticky rozpozná dodávateľa, sumu a dátum. Vy len rýchlo skontrolujete a potvrdíte.",
        "step3_t": "Odošlite účtovnej firme",
        "step3_p": "Koncom mesiaca jedným kliknutím odošlete všetky doklady. Email sa otvorí automaticky s prílohou.",
        "feat_label": "Funkcie",
        "feat_title": "Všetko čo potrebujete",
        "feat_sub": "RýchleÚčto robí nudnú administratívu za vás — aby ste sa mohli sústrediť na biznis.",
        "f1_t": "Inteligentné skenovanie",
        "f1_p": "Odfotografujte doklad v jednej alebo viacerých fotkách. OCR rozpozná dodávateľa, sumu a dátum.",
        "f2_t": "eKasa integrácia",
        "f2_p": "Naskenujte QR kód z bločku a aplikácia dotiahne údaje z Finančnej správy SR.",
        "f3_t": "Prehľad nákladov a príjmov",
        "f3_p": "Automatické rozlišovanie nákladov a príjmov. Prehľad po mesiacoch, filtre a vyhľadávanie.",
        "f4_t": "Export pre účtovníka",
        "f4_p": "Mesačný ZIP: PDF tabuľka, CSV, XML, ISDOC, OMEGA a originálne fotografie.",
        "f5_t": "Pohoda, Money S3, MRP, OMEGA",
        "f5_p": "Exportujte doklady do formátov pre bežné účtovné softvéry.",
        "f6_t": "100% offline & súkromné",
        "f6_p": "Dáta ostávajú v telefóne. Žiadny cloud, žiadna registrácia, žiadne zdieľanie s tretími stranami.",
        "price_label": "Cenník",
        "price_title": "Jednoduché ceny",
        "price_sub": "Začnite zadarmo, plaťte až keď ste spokojní.",
        "trial_name": "Trial",
        "trial_price": "0€",
        "trial_period": "/ 30 dní",
        "trial_desc": "Plný prístup ku všetkým funkciám po dobu 30 dní.",
        "trial_f1": "Neobmedzené skenovanie dokladov",
        "trial_f2": "OCR + eKasa integrácia",
        "trial_f3": "Export pre účtovníka",
        "trial_f4": "XML / ISDOC / MRP / OMEGA export",
        "trial_cta": "Vyskúšať zadarmo",
        "year_name": "Ročné Premium",
        "year_price": "9,99€",
        "year_period": "/ rok",
        "year_desc": "Pre živnostníkov s paušálnymi výdavkami — až 50 dokladov ročne.",
        "year_f1": "50 skenovaných a uložených dokladov / rok",
        "year_f2": "OCR + eKasa + PDF",
        "year_f3": "Export pre účtovníka (POHODA, Money S3, MRP…)",
        "year_f4": "Po limite upgrade na mesačné neobmedzené",
        "year_cta": "Vybrať ročné",
        "prem_badge": "Najpopulárnejší",
        "prem_name": "Premium mesačné",
        "prem_price": "4,99€",
        "prem_period": "/ mesiac",
        "prem_desc": "Neobmedzené skenovanie. Zrušiť môžete kedykoľvek.",
        "prem_f1": "Všetko z Trial",
        "prem_f2": "Neobmedzené doklady",
        "prem_f3": "Budúce aktualizácie zadarmo",
        "prem_f4": "Platba cez Google Play",
        "prem_f5": "Platba cez App Store",
        "prem_cta": "Začať — 30 dní zadarmo",
        "faq_label": "FAQ",
        "faq_title": "Časté otázky",
        "faq": [
            ("Pre koho je RýchleÚčto určené?", "Pre živnostníkov, malé s.r.o. a každého, kto chce ušetriť čas s mesačnou administratívou pre účtovníka."),
            ("Sú moje dáta v bezpečí?", "Áno. Všetky dáta ostávajú výlučne v telefóne. Aplikácia neposiela osobné údaje na server a nevyžaduje registráciu."),
            ("Funguje aplikácia bez internetu?", "Áno, takmer všetko funguje offline. Internet je potrebný len pre eKasa overenie QR kódov."),
            ("Aké sú predplatné?", "Po 30-dňovom trial môžete zvoliť ročné Premium za 9,99€ (50 dokladov / rok) alebo mesačné neobmedzené za 4,99€. Platba cez Google Play alebo App Store, zrušenie kedykoľvek."),
            ("V akých jazykoch je aplikácia?", "Slovenčina, čeština, nemčina a angličtina."),
        ],
        "cta_title": "Začnite používať RýchleÚčto dnes",
        "cta_p": "30 dní zadarmo. Žiadna registrácia. Žiadna kreditná karta.",
        "footer_p": "Mobilná aplikácia pre živnostníkov a malé firmy. Účtovníctvo za 60 sekúnd mesačne.",
        "footer_app": "Aplikácia",
        "footer_legal": "Právne",
        "footer_privacy": "Zásady ochrany súkromia",
        "footer_terms": "Obchodné podmienky",
        "footer_contact": "Kontakt",
        "footer_copy": "© 2026 RýchleÚčto — Joy IT Solution s.r.o. Všetky práva vyhradené.",
        "footer_country": "🇸🇰 Slovenská republika",
        "developed": "Vyvinuté s ❤️ od",
        "compat_label": "Kompatibilita",
        "compat_title": "Export pre účtovné softvéry",
        "compat_sub": "Mesačný balík obsahuje importné súbory pripravené pre bežné účtovné systémy.",
        "compat_items": [
            "Export do MRP XML 2.0",
            "Export do POHODA XML",
            "Export do Money S3 XML",
            "Export do OMEGA (TXT)",
        ],
        "trademark_disclaimer": "Názvy MRP, POHODA, Money S3 a OMEGA sú ochrannými známkami ich príslušných vlastníkov. Táto aplikácia nie je s uvedenými spoločnosťami pridružená ani nimi schválená.",
    },
    "cs": {
        "code": "cs",
        "html_lang": "cs",
        "dir": "cz",
        "prefix": "../",
        "path": "/cz/",
        "app": "ÚčtoSkenExport",
        "shot_dir": "cs",
        "title": "ÚčtoSkenExport — Doklady pro účetní za 60 sekund",
        "description": "ÚčtoSkenExport je mobilní aplikace pro OSVČ a malé firmy. Vyfoťte doklady a pošlete je své účetní — export do POHODA, Money S3, MRP a OMEGA.",
        "nav_features": "Funkce",
        "nav_how": "Jak to funguje",
        "nav_pricing": "Ceník",
        "nav_faq": "FAQ",
        "nav_privacy": "Soukromí",
        "nav_screens": "Aplikace",
        "cta_nav": "Stáhnout zdarma",
        "badge": "🇨🇿 Dostupné pro Česko",
        "h1_html": "Doklady pro účetní<br/>za <span>60 sekund</span>",
        "hero_p": "Vyfoťte faktury a účtenky a pošlete je účetní firmě, kterou už máte. Export do POHODA, Money S3, MRP a OMEGA — bez změny kanceláře a bez cloudu.",
        "btn_play": "📱 Stáhnout z Google Play (Android)",
        "btn_ios": "🍎 Stáhnout z App Store (iPhone)",
        "btn_how": "Jak to funguje?",
        "hero_alt": "ÚčtoSkenExport — náhled aplikace",
        "screens_label": "Aplikace",
        "screens_title": "Podívejte se, jak to vypadá",
        "screens_sub": "Skutečné obrazovky z aplikace — od skenování po měsíční export.",
        "shot_alt": "Náhled aplikace {n}",
        "how_label": "Jak to funguje",
        "how_title": "Tři jednoduché kroky",
        "step1_t": "Vyfoťte doklad",
        "step1_p": "Fakturu, účtenku nebo paragon. Velkou fakturu? Pořiďte více fotek po částech. Nebo naskenujte QR kód z eKasy.",
        "step2_t": "Zkontrolujte a potvrďte",
        "step2_p": "Aplikace automaticky rozpozná dodavatele, částku a datum. Vy jen rychle zkontrolujete a potvrdíte.",
        "step3_t": "Odešlete účetní firmě",
        "step3_p": "Koncem měsíce jedním klepnutím odešlete všechny doklady. E-mail se otevře automaticky s přílohou.",
        "feat_label": "Funkce",
        "feat_title": "Vše, co potřebujete",
        "feat_sub": "ÚčtoSkenExport dělá nudnou administrativu za vás — abyste se mohli soustředit na byznys.",
        "f1_t": "Inteligentní skenování",
        "f1_p": "Vyfoťte doklad v jedné nebo více fotkách. OCR rozpozná dodavatele, částku a datum.",
        "f2_t": "eKasa integrace",
        "f2_p": "Naskenujte QR kód z účtenky a aplikace načte údaje ze systému finanční správy.",
        "f3_t": "Přehled nákladů a příjmů",
        "f3_p": "Automatické rozlišování nákladů a příjmů. Přehled po měsících, filtry a vyhledávání.",
        "f4_t": "Export pro účetní",
        "f4_p": "Měsíční ZIP: PDF tabulka, CSV, XML, ISDOC, OMEGA a originální fotografie.",
        "f5_t": "Pohoda, Money S3, MRP, OMEGA",
        "f5_p": "Exportujte doklady do formátů pro běžné účetní softwary.",
        "f6_t": "100% offline & soukromé",
        "f6_p": "Data zůstávají v telefonu. Žádný cloud, žádná registrace, žádné sdílení s třetími stranami.",
        "price_label": "Ceník",
        "price_title": "Jednoduché ceny",
        "price_sub": "Začněte zdarma, plaťte až když jste spokojeni.",
        "trial_name": "Trial",
        "trial_price": "0€",
        "trial_period": "/ 30 dní",
        "trial_desc": "Plný přístup ke všem funkcím po dobu 30 dní.",
        "trial_f1": "Neomezené skenování dokladů",
        "trial_f2": "OCR + eKasa integrace",
        "trial_f3": "Export pro účetní",
        "trial_f4": "XML / ISDOC / MRP / OMEGA export",
        "trial_cta": "Vyzkoušet zdarma",
        "year_name": "Roční Premium",
        "year_price": "9,99€",
        "year_period": "/ rok",
        "year_desc": "Pro OSVČ s paušálními výdaji — až 50 dokladů ročně.",
        "year_f1": "50 naskenovaných a uložených dokladů / rok",
        "year_f2": "OCR + eKasa + PDF",
        "year_f3": "Export pro účetní (POHODA, Money S3, MRP…)",
        "year_f4": "Po limitu upgrade na měsíční neomezené",
        "year_cta": "Vybrat roční",
        "prem_badge": "Nejpopulárnější",
        "prem_name": "Premium měsíční",
        "prem_price": "4,99€",
        "prem_period": "/ měsíc",
        "prem_desc": "Neomezené skenování. Zrušit můžete kdykoli.",
        "prem_f1": "Vše z Trial",
        "prem_f2": "Neomezené doklady",
        "prem_f3": "Budoucí aktualizace zdarma",
        "prem_f4": "Platba přes Google Play",
        "prem_f5": "Platba přes App Store",
        "prem_cta": "Začít — 30 dní zdarma",
        "faq_label": "FAQ",
        "faq_title": "Časté otázky",
        "faq": [
            ("Pro koho je ÚčtoSkenExport určen?", "Pro OSVČ, malá s.r.o. a každého, kdo chce ušetřit čas s měsíční administrativou pro účetní."),
            ("Jsou moje data v bezpečí?", "Ano. Všechna data zůstávají výhradně v telefonu. Aplikace neposílá osobní údaje na server a nevyžaduje registraci."),
            ("Funguje aplikace bez internetu?", "Ano, téměř vše funguje offline. Internet je potřeba jen pro ověření QR kódů eKasa."),
            ("Jaká jsou předplatná?", "Po 30denním trialu můžete zvolit roční Premium za 9,99€ (50 dokladů / rok) nebo měsíční neomezené za 4,99€. Platba přes Google Play nebo App Store, zrušení kdykoli."),
            ("V jakých jazycích je aplikace?", "Slovenština, čeština, němčina a angličtina."),
        ],
        "cta_title": "Začněte používat ÚčtoSkenExport dnes",
        "cta_p": "30 dní zdarma. Žádná registrace. Žádná kreditní karta.",
        "footer_p": "Mobilní aplikace pro OSVČ a malé firmy. Účetnictví za 60 sekund měsíčně.",
        "footer_app": "Aplikace",
        "footer_legal": "Právní",
        "footer_privacy": "Zásady ochrany soukromí",
        "footer_terms": "Obchodní podmínky",
        "footer_contact": "Kontakt",
        "footer_copy": "© 2026 ÚčtoSkenExport — Joy IT Solution s.r.o. Všechna práva vyhrazena.",
        "footer_country": "🇨🇿 Česká republika",
        "developed": "Vyvinuto s ❤️ od",
        "compat_label": "Kompatibilita",
        "compat_title": "Export pro účetní softwary",
        "compat_sub": "Měsíční balíček obsahuje importní soubory připravené pro běžné účetní systémy.",
        "compat_items": [
            "Export do MRP XML 2.0",
            "Export do POHODA XML",
            "Export do Money S3 XML",
            "Export do OMEGA (TXT)",
        ],
        "trademark_disclaimer": "Názvy MRP, POHODA, Money S3 a OMEGA jsou ochrannými známkami jejich příslušných vlastníků. Tato aplikace není s uvedenými společnostmi přidružená ani jimi schválená.",
    },
    "de": {
        "code": "de",
        "html_lang": "de",
        "dir": "de",
        "prefix": "../",
        "path": "/de/",
        "app": "SchnellBelegio",
        "shot_dir": "de",
        "title": "SchnellBelegio — Belege für die Buchhaltung in 60 Sekunden",
        "description": "SchnellBelegio ist die App für Einzelunternehmer und kleine Firmen. Belege fotografieren und an Ihre Buchhaltung senden — exportfähig für gängige Formate.",
        "nav_features": "Funktionen",
        "nav_how": "So funktioniert's",
        "nav_pricing": "Preise",
        "nav_faq": "FAQ",
        "nav_privacy": "Datenschutz",
        "nav_screens": "App",
        "cta_nav": "Kostenlos laden",
        "badge": "🇩🇪 Für Deutschland & Österreich",
        "h1_html": "Belege für die Buchhaltung<br/>in <span>60 Sekunden</span>",
        "hero_p": "Fotografieren Sie Rechnungen und Belege und senden Sie sie an Ihre bestehende Buchhaltung. Export für gängige Formate — ohne Kanzleiwechsel und ohne Cloud-Zwang.",
        "btn_play": "📱 Bei Google Play laden (Android)",
        "btn_ios": "🍎 Im App Store laden (iPhone)",
        "btn_how": "So funktioniert's",
        "hero_alt": "SchnellBelegio — App-Vorschau",
        "screens_label": "App",
        "screens_title": "So sieht die App aus",
        "screens_sub": "Echte Screenshots — vom Scan bis zum Monatsexport.",
        "shot_alt": "App-Screenshot {n}",
        "how_label": "So funktioniert's",
        "how_title": "Drei einfache Schritte",
        "step1_t": "Beleg fotografieren",
        "step1_p": "Rechnung oder Beleg. Lange Dokumente in mehreren Fotos. Oder QR-Code scannen.",
        "step2_t": "Prüfen und bestätigen",
        "step2_p": "Die App erkennt Lieferant, Betrag und Datum. Sie prüfen kurz und bestätigen.",
        "step3_t": "An die Buchhaltung senden",
        "step3_p": "Am Monatsende senden Sie alle Belege mit einem Tippen. Die E-Mail öffnet sich mit Anhang.",
        "feat_label": "Funktionen",
        "feat_title": "Alles, was Sie brauchen",
        "feat_sub": "SchnellBelegio übernimmt die Bürokratie — damit Sie sich aufs Business konzentrieren.",
        "f1_t": "Intelligentes Scannen",
        "f1_p": "Fotografieren Sie Belege in einem oder mehreren Fotos. OCR erkennt Lieferant, Betrag und Datum.",
        "f2_t": "QR-Code Erkennung",
        "f2_p": "Scannen Sie den QR-Code auf dem Beleg — Daten werden automatisch ausgelesen.",
        "f3_t": "Ausgaben & Einnahmen",
        "f3_p": "Automatische Trennung von Ausgaben und Einnahmen. Monatsübersicht, Filter und Suche.",
        "f4_t": "Export für die Buchhaltung",
        "f4_p": "Monatliches ZIP: PDF-Tabelle, CSV, XML, ISDOC und Originalfotos.",
        "f5_t": "XML, ISDOC, CSV, PDF",
        "f5_p": "Exportformate für Ihre Buchhaltung — typische DE-Formate folgen später.",
        "f6_t": "100% offline & privat",
        "f6_p": "Daten bleiben auf dem Telefon. Keine Cloud, keine Registrierung, kein Teilen mit Dritten.",
        "price_label": "Preise",
        "price_title": "Einfache Preise",
        "price_sub": "Kostenlos starten, zahlen wenn Sie zufrieden sind.",
        "trial_name": "Testphase",
        "trial_price": "0€",
        "trial_period": "/ 30 Tage",
        "trial_desc": "Voller Zugang zu allen Funktionen für 30 Tage.",
        "trial_f1": "Unbegrenztes Scannen",
        "trial_f2": "OCR + QR-Erkennung",
        "trial_f3": "Export für die Buchhaltung",
        "trial_f4": "XML / ISDOC / CSV / PDF",
        "trial_cta": "Kostenlos testen",
        "year_name": "Jahres-Premium",
        "year_price": "9,99€",
        "year_period": "/ Jahr",
        "year_desc": "Für Freiberufler mit wenigen Belegen — bis zu 50 Dokumente pro Jahr.",
        "year_f1": "50 gescannte und gespeicherte Belege / Jahr",
        "year_f2": "OCR + QR + PDF",
        "year_f3": "Export für die Buchhaltung",
        "year_f4": "Nach Limit Upgrade auf unbegrenztes Monatsabo",
        "year_cta": "Jahresabo wählen",
        "prem_badge": "Beliebteste",
        "prem_name": "Premium monatlich",
        "prem_price": "4,99€",
        "prem_period": "/ Monat",
        "prem_desc": "Unbegrenztes Scannen. Jederzeit kündbar.",
        "prem_f1": "Alles aus der Testphase",
        "prem_f2": "Unbegrenzte Belege",
        "prem_f3": "Zukünftige Updates inklusive",
        "prem_f4": "Zahlung über Google Play",
        "prem_f5": "Zahlung über App Store",
        "prem_cta": "Starten — 30 Tage gratis",
        "faq_label": "FAQ",
        "faq_title": "Häufige Fragen",
        "faq": [
            ("Für wen ist SchnellBelegio?", "Für Einzelunternehmer, kleine Firmen und alle, die Zeit bei der monatlichen Belegverwaltung sparen wollen."),
            ("Sind meine Daten sicher?", "Ja. Alle Daten bleiben ausschließlich auf dem Telefon. Keine Server-Registrierung, kein Cloud-Zwang."),
            ("Funktioniert die App offline?", "Ja, fast alles funktioniert offline. Internet wird nur für manche Online-Prüfungen benötigt."),
            ("Welche Abos gibt es?", "Nach 30 Tagen Testphase: Jahres-Premium für 9,99€ (50 Belege / Jahr) oder unbegrenztes Monatsabo für 4,99€. Zahlung über Google Play oder App Store, jederzeit kündbar."),
            ("In welchen Sprachen gibt es die App?", "Slowakisch, Tschechisch, Deutsch und Englisch."),
        ],
        "cta_title": "Starten Sie heute mit SchnellBelegio",
        "cta_p": "30 Tage kostenlos. Keine Registrierung. Keine Kreditkarte nötig.",
        "footer_p": "Die App für Einzelunternehmer und kleine Firmen. Buchhaltung in 60 Sekunden monatlich.",
        "footer_app": "App",
        "footer_legal": "Rechtliches",
        "footer_privacy": "Datenschutzerklärung",
        "footer_terms": "Nutzungsbedingungen",
        "footer_contact": "Kontakt",
        "footer_copy": "© 2026 SchnellBelegio — Joy IT Solution s.r.o. Alle Rechte vorbehalten.",
        "footer_country": "🇩🇪 Deutschland / 🇦🇹 Österreich",
        "developed": "Entwickelt mit ❤️ von",
        "compat_label": "Kompatibilität",
        "compat_title": "Export für Buchhaltungssoftware",
        "compat_sub": "Das Monatspaket enthält Importdateien für gängige Buchhaltungssysteme.",
        "compat_items": [
            "Export nach MRP XML 2.0",
            "Export nach POHODA XML",
            "Export nach Money S3 XML",
            "Export nach OMEGA (TXT)",
        ],
        "trademark_disclaimer": "Die Namen MRP, POHODA, Money S3 und OMEGA sind Marken ihrer jeweiligen Inhaber. Diese App ist mit den genannten Unternehmen weder verbunden noch von ihnen genehmigt.",
    },
    "en": {
        "code": "en",
        "html_lang": "en",
        "dir": "en",
        "prefix": "../",
        "path": "/en/",
        "app": "Scan2Accountant",
        "shot_dir": "en",
        "title": "Scan2Accountant — Documents for your accountant in 60 seconds",
        "description": "Scan2Accountant is a mobile app for freelancers and small businesses. Photograph documents and send them to your accountant — export-ready for common formats.",
        "nav_features": "Features",
        "nav_how": "How it works",
        "nav_pricing": "Pricing",
        "nav_faq": "FAQ",
        "nav_privacy": "Privacy",
        "nav_screens": "App",
        "cta_nav": "Download free",
        "badge": "🌍 Available in 4 languages",
        "h1_html": "Documents for your accountant<br/>in <span>60 seconds</span>",
        "hero_p": "Photograph invoices and receipts and send them to the accountant you already have. Export-ready formats — no firm lock-in and no forced cloud.",
        "btn_play": "📱 Get it on Google Play (Android)",
        "btn_ios": "🍎 Download on the App Store (iPhone)",
        "btn_how": "How it works",
        "hero_alt": "Scan2Accountant — app preview",
        "screens_label": "App",
        "screens_title": "See how it looks",
        "screens_sub": "Real screenshots — from scanning to the monthly export.",
        "shot_alt": "App screenshot {n}",
        "how_label": "How it works",
        "how_title": "Three simple steps",
        "step1_t": "Photograph the document",
        "step1_p": "Invoice or receipt. Long documents in multiple photos. Or scan a QR code.",
        "step2_t": "Review and confirm",
        "step2_p": "The app detects supplier, amount and date. You quickly review and confirm.",
        "step3_t": "Send to your accountant",
        "step3_p": "At month end, send all documents in one tap. Email opens with the attachment ready.",
        "feat_label": "Features",
        "feat_title": "Everything you need",
        "feat_sub": "Scan2Accountant handles the busywork — so you can focus on your business.",
        "f1_t": "Smart scanning",
        "f1_p": "Photograph documents in one or more shots. OCR reads supplier, amount and date.",
        "f2_t": "QR code recognition",
        "f2_p": "Scan the QR code on a receipt — data is loaded automatically.",
        "f3_t": "Expenses & income",
        "f3_p": "Automatic expense/income split. Monthly overview, filters and search.",
        "f4_t": "Export for accounting",
        "f4_p": "Monthly ZIP: PDF table, CSV, XML, ISDOC and original photos.",
        "f5_t": "XML, ISDOC, CSV, PDF",
        "f5_p": "Formats ready for your accountant — more local formats coming later.",
        "f6_t": "100% offline & private",
        "f6_p": "Data stays on your phone. No cloud, no sign-up, no sharing with third parties.",
        "price_label": "Pricing",
        "price_title": "Simple pricing",
        "price_sub": "Start free, pay when you're happy.",
        "trial_name": "Trial",
        "trial_price": "€0",
        "trial_period": "/ 30 days",
        "trial_desc": "Full access to all features for 30 days.",
        "trial_f1": "Unlimited document scanning",
        "trial_f2": "OCR + QR recognition",
        "trial_f3": "Export for your accountant",
        "trial_f4": "XML / ISDOC / CSV / PDF",
        "trial_cta": "Try for free",
        "year_name": "Yearly Premium",
        "year_price": "€9.99",
        "year_period": "/ year",
        "year_desc": "For freelancers with light paperwork — up to 50 documents per year.",
        "year_f1": "50 scanned & saved documents / year",
        "year_f2": "OCR + QR + PDF",
        "year_f3": "Export for your accountant",
        "year_f4": "After the limit, upgrade to unlimited monthly",
        "year_cta": "Choose yearly",
        "prem_badge": "Most popular",
        "prem_name": "Premium monthly",
        "prem_price": "€4.99",
        "prem_period": "/ month",
        "prem_desc": "Unlimited scanning. Cancel anytime.",
        "prem_f1": "Everything in Trial",
        "prem_f2": "Unlimited documents",
        "prem_f3": "Future updates included",
        "prem_f4": "Pay via Google Play",
        "prem_f5": "Pay via App Store",
        "prem_cta": "Start — 30 days free",
        "faq_label": "FAQ",
        "faq_title": "Frequently asked questions",
        "faq": [
            ("Who is Scan2Accountant for?", "Freelancers, small companies and anyone who wants to save time on monthly paperwork for their accountant."),
            ("Is my data safe?", "Yes. All data stays on your phone. No server registration and no forced cloud account."),
            ("Does it work offline?", "Yes, almost everything works offline. Internet is only needed for some online checks."),
            ("What subscriptions are available?", "After a 30-day trial: Yearly Premium for €9.99 (50 documents / year) or unlimited monthly for €4.99. Pay via Google Play or the App Store; cancel anytime."),
            ("Which languages are supported?", "Slovak, Czech, German and English."),
        ],
        "cta_title": "Start using Scan2Accountant today",
        "cta_p": "30 days free. No registration. No credit card required.",
        "footer_p": "A mobile app for freelancers and small businesses. Bookkeeping in 60 seconds monthly.",
        "footer_app": "App",
        "footer_legal": "Legal",
        "footer_privacy": "Privacy policy",
        "footer_terms": "Terms of service",
        "footer_contact": "Contact",
        "footer_copy": "© 2026 Scan2Accountant — Joy IT Solution s.r.o. All rights reserved.",
        "footer_country": "🌍 Europe",
        "developed": "Built with ❤️ by",
        "compat_label": "Compatibility",
        "compat_title": "Export for accounting software",
        "compat_sub": "The monthly bundle includes import files prepared for common accounting systems.",
        "compat_items": [
            "Export to MRP XML 2.0",
            "Export to POHODA XML",
            "Export to Money S3 XML",
            "Export to OMEGA (TXT)",
        ],
        "trademark_disclaimer": "MRP, POHODA, Money S3 and OMEGA are trademarks of their respective owners. This app is not affiliated with or endorsed by those companies.",
    },
}

PLAY = "https://play.google.com/store/apps/details?id=sk.rychleucto.rychleucto"
IOS = "https://apps.apple.com/sk/app/scan2accountant/id6788722506"


def lang_switch(active: str, prefix: str) -> str:
    items = [
        ("sk", "/", "SK"),
        ("cs", "/cz/", "CZ"),
        ("de", "/de/", "DE"),
        ("en", "/en/", "EN"),
    ]
    links = []
    for code, href, label in items:
        cls = ' class="active"' if code == active else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<div class="lang-switch" aria-label="Language">' + "".join(links) + "</div>"


def screenshots_html(t: dict) -> str:
    p = t["prefix"]
    shots = []
    for n in range(1, 6):
        src = f'{p}assets/screenshots/{t["shot_dir"]}/{n:02d}.png'
        alt = t["shot_alt"].format(n=n)
        shots.append(
            f'<figure class="shot">'
            f'<a href="{src}" class="shot-link" data-lightbox aria-label="{alt}">'
            f'<img src="{src}" alt="{alt}" loading="lazy" width="1080" height="1920" />'
            f'</a></figure>'
        )
    return "\n          ".join(shots)


def faq_html(t: dict) -> str:
    blocks = []
    for q, a in t["faq"]:
        blocks.append(
            f"""      <div class="faq-item">
        <div class="faq-q">{q} <span>+</span></div>
        <div class="faq-a">{a}</div>
      </div>"""
        )
    return "\n".join(blocks)


def compat_html(t: dict) -> str:
    items = "\n".join(f"        <li>{item}</li>" for item in t["compat_items"])
    return f"""      <ul class="compat-list">
{items}
      </ul>"""


def _json_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
    )


def seo_head(t: dict) -> str:
    """Canonical, Open Graph, Twitter + JSON-LD for search engines."""
    canonical = f"https://www.rychleucto.sk{t['path']}"
    og_locale = {
        "sk": "sk_SK",
        "cs": "cs_CZ",
        "de": "de_DE",
        "en": "en_US",
    }.get(t["code"], "sk_SK")
    image = "https://www.rychleucto.sk/hero.png"
    play = "https://play.google.com/store/apps/details?id=sk.rychleucto.rychleucto"
    ios = "https://apps.apple.com/sk/app/scan2accountant/id6788722506"

    faq_entities = []
    for q, a in t["faq"]:
        faq_entities.append(
            "{\n"
            '        "@type": "Question",\n'
            f'        "name": "{_json_escape(q)}",\n'
            '        "acceptedAnswer": {\n'
            '          "@type": "Answer",\n'
            f'          "text": "{_json_escape(a)}"\n'
            "        }\n"
            "      }"
        )
    faq_json = ",\n      ".join(faq_entities)

    return f"""  <link rel="canonical" href="{canonical}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#1A56DB" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{t['app']}" />
  <meta property="og:locale" content="{og_locale}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{t['title']}" />
  <meta property="og:description" content="{t['description']}" />
  <meta property="og:image" content="{image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t['title']}" />
  <meta name="twitter:description" content="{t['description']}" />
  <meta name="twitter:image" content="{image}" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{_json_escape(t['app'])}",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Android, iOS",
    "description": "{_json_escape(t['description'])}",
    "url": "{canonical}",
    "image": "{image}",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "EUR"
    }},
    "downloadUrl": [
      "{play}",
      "{ios}"
    ],
    "publisher": {{
      "@type": "Organization",
      "name": "Joy IT Solution s.r.o.",
      "url": "https://www.rychleucto.sk/"
    }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_json}
    ]
  }}
  </script>
"""


def render(t: dict) -> str:
    p = t["prefix"]
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']}</title>
  <meta name="description" content="{t['description']}" />
  <link rel="alternate" hreflang="sk" href="https://www.rychleucto.sk/" />
  <link rel="alternate" hreflang="cs" href="https://www.rychleucto.sk/cz/" />
  <link rel="alternate" hreflang="de" href="https://www.rychleucto.sk/de/" />
  <link rel="alternate" hreflang="en" href="https://www.rychleucto.sk/en/" />
  <link rel="alternate" hreflang="x-default" href="https://www.rychleucto.sk/" />
{seo_head(t)}  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}styles.css" />
{ga_head()}
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="{t['path']}" class="nav-logo">{t['app']}</a>
    <div class="nav-links">
      <a href="#screenshots">{t['nav_screens']}</a>
      <a href="#funkcie">{t['nav_features']}</a>
      <a href="#ako-to-funguje">{t['nav_how']}</a>
      <a href="#kompatibilita">{t['compat_label']}</a>
      <a href="#cennik">{t['nav_pricing']}</a>
      <a href="#faq">{t['nav_faq']}</a>
      <a href="privacy.html">{t['nav_privacy']}</a>
    </div>
    <div class="nav-actions">
      {lang_switch(t['code'] if t['code'] != 'cs' else 'cs', p)}
      <a href="#download" class="btn btn-primary">{t['cta_nav']}</a>
    </div>
  </div>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-badge">{t['badge']}</div>
      <h1>{t['h1_html']}</h1>
      <p>{t['hero_p']}</p>
      <div class="hero-cta">
        <a href="{PLAY}" class="btn btn-primary btn-lg">{t['btn_play']}</a>
        <a href="{IOS}" class="btn btn-app-store btn-lg">{t['btn_ios']}</a>
        <a href="#ako-to-funguje" class="btn btn-outline btn-lg">{t['btn_how']}</a>
      </div>
    </div>
    <div class="hero-image">
      <img src="{p}hero.png" alt="{t['hero_alt']}" loading="eager" />
    </div>
  </div>
</section>

<section id="screenshots" class="screenshots-bg">
  <div class="section-inner">
    <div class="section-label">{t['screens_label']}</div>
    <h2 class="section-title">{t['screens_title']}</h2>
    <p class="section-sub">{t['screens_sub']}</p>
    <div class="screenshots-scroll">
          {screenshots_html(t)}
    </div>
  </div>
</section>

<section id="ako-to-funguje" class="how-bg">
  <div class="section-inner">
    <div class="section-label">{t['how_label']}</div>
    <h2 class="section-title">{t['how_title']}</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <h3>{t['step1_t']}</h3>
        <p>{t['step1_p']}</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h3>{t['step2_t']}</h3>
        <p>{t['step2_p']}</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h3>{t['step3_t']}</h3>
        <p>{t['step3_p']}</p>
      </div>
    </div>
  </div>
</section>

<section id="funkcie">
  <div class="section-inner">
    <div class="section-label">{t['feat_label']}</div>
    <h2 class="section-title">{t['feat_title']}</h2>
    <p class="section-sub">{t['feat_sub']}</p>
    <div class="features-grid">
      <div class="feature-card"><div class="feature-icon">📸</div><h3>{t['f1_t']}</h3><p>{t['f1_p']}</p></div>
      <div class="feature-card"><div class="feature-icon">🔲</div><h3>{t['f2_t']}</h3><p>{t['f2_p']}</p></div>
      <div class="feature-card"><div class="feature-icon">📊</div><h3>{t['f3_t']}</h3><p>{t['f3_p']}</p></div>
      <div class="feature-card"><div class="feature-icon">📤</div><h3>{t['f4_t']}</h3><p>{t['f4_p']}</p></div>
      <div class="feature-card"><div class="feature-icon">🗂️</div><h3>{t['f5_t']}</h3><p>{t['f5_p']}</p></div>
      <div class="feature-card"><div class="feature-icon">🔒</div><h3>{t['f6_t']}</h3><p>{t['f6_p']}</p></div>
    </div>
  </div>
</section>

<section id="kompatibilita" class="compat-bg">
  <div class="section-inner">
    <div class="section-label">{t['compat_label']}</div>
    <h2 class="section-title">{t['compat_title']}</h2>
    <p class="section-sub">{t['compat_sub']}</p>
{compat_html(t)}
    <p class="trademark-disclaimer">{t['trademark_disclaimer']}</p>
  </div>
</section>

<section id="cennik">
  <div class="section-inner">
    <div class="section-label">{t['price_label']}</div>
    <h2 class="section-title">{t['price_title']}</h2>
    <p class="section-sub">{t['price_sub']}</p>
    <div class="pricing-grid">
      <div class="pricing-card">
        <div class="pricing-name">{t['trial_name']}</div>
        <div class="pricing-price">{t['trial_price']} <span>{t['trial_period']}</span></div>
        <div class="pricing-desc">{t['trial_desc']}</div>
        <ul class="pricing-features">
          <li>{t['trial_f1']}</li>
          <li>{t['trial_f2']}</li>
          <li>{t['trial_f3']}</li>
          <li>{t['trial_f4']}</li>
        </ul>
        <a href="#download" class="btn btn-outline" style="width:100%;justify-content:center;">{t['trial_cta']}</a>
      </div>
      <div class="pricing-card">
        <div class="pricing-name">{t['year_name']}</div>
        <div class="pricing-price">{t['year_price']} <span>{t['year_period']}</span></div>
        <div class="pricing-desc">{t['year_desc']}</div>
        <ul class="pricing-features">
          <li>{t['year_f1']}</li>
          <li>{t['year_f2']}</li>
          <li>{t['year_f3']}</li>
          <li>{t['year_f4']}</li>
        </ul>
        <a href="#download" class="btn btn-outline" style="width:100%;justify-content:center;">{t['year_cta']}</a>
      </div>
      <div class="pricing-card featured">
        <div class="pricing-badge">{t['prem_badge']}</div>
        <div class="pricing-name">{t['prem_name']}</div>
        <div class="pricing-price">{t['prem_price']} <span>{t['prem_period']}</span></div>
        <div class="pricing-desc">{t['prem_desc']}</div>
        <ul class="pricing-features">
          <li>{t['prem_f1']}</li>
          <li>{t['prem_f2']}</li>
          <li>{t['prem_f3']}</li>
          <li>{t['prem_f4']}</li>
          <li>{t['prem_f5']}</li>
        </ul>
        <a href="#download" class="btn btn-primary" style="width:100%;justify-content:center;">{t['prem_cta']}</a>
      </div>
    </div>
  </div>
</section>

<section id="faq" style="background: var(--card);">
  <div class="section-inner">
    <div class="section-label">{t['faq_label']}</div>
    <h2 class="section-title">{t['faq_title']}</h2>
    <div class="faq-list">
{faq_html(t)}
    </div>
  </div>
</section>

<section class="cta-section" id="download">
  <h2>{t['cta_title']}</h2>
  <p>{t['cta_p']}</p>
  <div class="store-buttons">
    <a href="{PLAY}" class="btn btn-white btn-lg">{t['btn_play']}</a>
    <a href="{IOS}" class="btn btn-white btn-lg" style="color:#111827;">{t['btn_ios']}</a>
  </div>
</section>

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="font-size:20px;font-weight:800;color:white;">{t['app']}</div>
        <p>{t['footer_p']}</p>
        <p style="margin-top:12px;">{t['developed']} <strong style="color:white;">Joy IT Solution s.r.o.</strong></p>
      </div>
      <div class="footer-col">
        <h4>{t['footer_app']}</h4>
        <a href="#screenshots">{t['nav_screens']}</a>
        <a href="#funkcie">{t['nav_features']}</a>
        <a href="#ako-to-funguje">{t['nav_how']}</a>
        <a href="#kompatibilita">{t['compat_label']}</a>
        <a href="#cennik">{t['nav_pricing']}</a>
        <a href="#faq">{t['nav_faq']}</a>
      </div>
      <div class="footer-col">
        <h4>{t['footer_legal']}</h4>
        <a href="privacy.html">{t['footer_privacy']}</a>
        <a href="terms.html">{t['footer_terms']}</a>
        <a href="mailto:joyitsolutionsro@gmail.com">{t['footer_contact']}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <div>{t['footer_copy']}</div>
      <div>{t['footer_country']}</div>
    </div>
    <p class="footer-disclaimer">{t['trademark_disclaimer']}</p>
  </div>
</footer>

<script src="{p}site.js" defer></script>
</body>
</html>
"""


def main() -> None:
    for key, t in LANGS.items():
        html = render(t)
        if t["dir"]:
            out_dir = ROOT / t["dir"]
            out_dir.mkdir(parents=True, exist_ok=True)
            out = out_dir / "index.html"
        else:
            out = ROOT / "index.html"
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
