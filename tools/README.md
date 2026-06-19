# 색인 통보 도구 (tools/)

검색엔진에 새 페이지를 **가장 빠르게** 알리기 위한 스크립트 모음입니다.

## 한눈에 보기

| 대상 | 방법 | 명령 |
| --- | --- | --- |
| 빙·네이버·얀덱스 | IndexNow (즉시) | `python tools/indexnow.py` |
| 구글 | Indexing API (즉시, 인증 필요) | `python tools/google_indexing.py` |
| 구글·네이버 | Search Console / 서치어드바이저에 `sitemap.xml` 1회 제출 | (웹 콘솔) |

> 구글은 IndexNow에 참여하지 않습니다. 구글 즉시 통보는 Indexing API를 쓰고,
> 일반적인 경로는 Search Console에 `sitemap.xml`을 제출하는 것입니다.

## 1) IndexNow — 빙·네이버 즉시 통보 (의존성 없음)

먼저 빌드하면 루트에 키 파일과 sitemap이 생성됩니다.

```bash
python build.py
```

배포 후 `https://<도메인>/<INDEXNOW_KEY>.txt` 가 열리는지 확인하세요. 그다음:

```bash
# 전체 일괄 통보 (sitemap.xml 의 모든 URL)
python tools/indexnow.py

# 글 올릴 때마다 특정 URL만 즉시 통보
python tools/indexnow.py https://geumcheon-massage1.pages.dev/seoul/geumcheon/gasan-dong-chuljangmassage/

# 전송 없이 미리보기
python tools/indexnow.py --dry-run
```

키는 `content/site.py` 의 `INDEXNOW_KEY` 에 있으며, 빌드 시 `<KEY>.txt` 로 루트에 노출됩니다.

## 2) Google Indexing API — 구글 즉시 통보

1회 준비: Google Cloud에서 Indexing API 사용 설정 → 서비스 계정 JSON 발급 →
Search Console 속성에 서비스 계정 이메일을 **소유자**로 추가 →
`pip install google-auth requests`.

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python tools/google_indexing.py                 # sitemap 전체
python tools/google_indexing.py <url> [<url>..]  # 특정 URL
```

## 3) sitemap ping (참고)

구글·빙 모두 ping 엔드포인트를 폐지했습니다. `tools/ping_sitemap.py` 는 호환용이며,
실제 통보는 위 1·2번과 Search Console / 네이버 서치어드바이저 sitemap 제출을 사용하세요.

## 권장 운영 루틴

1. 페이지 추가/수정 → `python build.py`
2. 배포(푸시)
3. `python tools/indexnow.py <새 URL>` (빙·네이버 즉시)
4. 필요 시 `python tools/google_indexing.py <새 URL>` (구글 즉시)
5. 최초 1회: Search Console·네이버 서치어드바이저에 `sitemap.xml` 제출
