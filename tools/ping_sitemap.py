#!/usr/bin/env python3
"""사이트맵 핑(보조 수단).

주의: 구글(2023)·빙(2024) 모두 sitemap ping 엔드포인트를 폐지했습니다.
따라서 현재 가장 빠른 통보 경로는:
  1) IndexNow  → 빙·네이버·얀덱스 (python tools/indexnow.py)
  2) Google Indexing API → 구글 (python tools/google_indexing.py)
  3) Search Console / 네이버 서치어드바이저에 sitemap.xml 1회 제출(자동 재크롤링)

이 스크립트는 호환을 위해 남아 있는 핑 엔드포인트가 있으면 best-effort 로 시도하고
결과를 보고합니다. 실패(404 등)는 정상이며, 위 1~3 경로를 사용하세요.
"""
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

SITEMAP = BASE_URL.rstrip("/") + "/sitemap.xml"
ENC = urllib.parse.quote(SITEMAP, safe="")

# 폐지된 엔드포인트 포함(호환용 best-effort)
PING = [
    ("Google(폐지됨)", f"https://www.google.com/ping?sitemap={ENC}"),
    ("Bing(폐지됨)", f"https://www.bing.com/ping?sitemap={ENC}"),
]


def main() -> None:
    print(f"sitemap: {SITEMAP}\n")
    for name, url in PING:
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                print(f"[{name}] HTTP {r.status}")
        except Exception as e:  # noqa: BLE001
            print(f"[{name}] 실패(정상일 수 있음): {e}")
    print("\n권장: `python tools/indexnow.py` (빙·네이버) + Search Console sitemap 제출(구글).")


if __name__ == "__main__":
    main()
