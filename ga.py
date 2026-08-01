# -*- coding: utf-8 -*-
"""Google Analytics 4 snippet for rychleucto.sk."""

GA_MEASUREMENT_ID = "G-F0DHNS74KT"


def head_snippet() -> str:
    mid = GA_MEASUREMENT_ID
    return f"""  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={mid}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{mid}');
  </script>
"""
