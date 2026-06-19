#!/usr/bin/env python3
"""Google Indexing API 통보 — 구글에 URL 색인/갱신 즉시 통보.

구글은 IndexNow 에 참여하지 않으므로, 즉시 통보가 필요하면 이 스크립트를 씁니다.
※ Indexing API 는 공식적으로 JobPosting/BroadcastEvent 용이지만 URL_UPDATED 통보에
   널리 사용됩니다. 일반 페이지는 Search Console 의 sitemap 제출이 정석 경로이며,
   이 API 는 보조 수단으로 보세요.

사전 준비(1회):
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python tools/google_indexing.py                 # sitemap.xml 전체
  python tools/google_indexing.py <url> [<url>..] # 특정 URL
  python tools/google_indexing.py --delete <url>  # URL_DELETED 통보
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        print("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main() -> None:
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        print("의존성이 없습니다. 먼저 실행: pip install google-auth requests")
        sys.exit(1)
    import requests

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        print("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 설정하세요.")
        sys.exit(1)

    args = sys.argv[1:]
    delete = "--delete" in args
    args = [a for a in args if a != "--delete"]
    urls = args if args else sitemap_urls()
    notif_type = "URL_DELETED" if delete else "URL_UPDATED"

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    headers = {"Authorization": f"Bearer {creds.token}",
               "Content-Type": "application/json"}

    ok = 0
    for url in urls:
        if not url.startswith(BASE):
            continue
        r = requests.post(ENDPOINT, headers=headers,
                          json={"url": url, "type": notif_type}, timeout=30)
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        print(f"[{status}] {notif_type} {url}")
        if r.status_code == 200:
            ok += 1
    print(f"\n완료: {ok}/{len(urls)} 건 접수")


if __name__ == "__main__":
    main()
