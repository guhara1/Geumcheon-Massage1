#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스·Seznam 동시 통보.

IndexNow는 하나의 엔드포인트에 통보하면 참여 검색엔진 전체에 공유됩니다.
(네이버·빙·얀덱스·Seznam 참여. 구글은 IndexNow 미참여 → google_indexing.py 사용.)

사용법:
  # 1) 전체 일괄 통보 (sitemap.xml 의 모든 URL)
  python tools/indexnow.py

  # 2) 글 올릴 때마다 특정 URL만 즉시 통보
  python tools/indexnow.py https://geumcheon-massage1.pages.dev/seoul/geumcheon/gasan-dong-chuljangmassage/

  # 3) 실제 전송 없이 확인만
  python tools/indexnow.py --dry-run

키 파일은 build.py 가 사이트 루트에 {INDEXNOW_KEY}.txt 로 생성합니다.
배포 후 https://<도메인>/{INDEXNOW_KEY}.txt 가 열려야 통보가 승인됩니다.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = urllib.parse.urlparse(BASE).netloc
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# IndexNow 엔드포인트(아무 곳에나 통보해도 참여 엔진 전체에 공유됨)
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        print("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls: list, dry_run: bool = False) -> None:
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        print("통보할 URL 이 없습니다. (도메인이 BASE_URL 과 일치해야 합니다)")
        return

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    print(f"호스트   : {HOST}")
    print(f"키 위치  : {KEY_LOCATION}")
    print(f"URL 수   : {len(urls)}")
    for u in urls:
        print(f"  - {u}")

    if dry_run:
        print("\n[--dry-run] 실제 전송하지 않았습니다.")
        return

    data = json.dumps(payload).encode("utf-8")
    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint,
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"\n[{endpoint}] → HTTP {resp.status} {resp.reason}")
        except urllib.error.HTTPError as e:
            # 200/202 가 정상. 일부 엔드포인트는 키 검증 후 처리됩니다.
            print(f"\n[{endpoint}] → HTTP {e.code} {e.reason}")
        except Exception as e:  # noqa: BLE001
            print(f"\n[{endpoint}] → 오류: {e}")
    print("\n완료. (HTTP 200/202 면 정상 접수)")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv[1:]
    urls = args if args else sitemap_urls()
    submit(urls, dry_run=dry)


if __name__ == "__main__":
    main()
