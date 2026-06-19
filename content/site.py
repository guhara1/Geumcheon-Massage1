# 사이트 공통 설정 — 금천구 출장마사지·홈타이 안내
BASE_URL = "https://geumcheon-massage1.pages.dev"

# IndexNow 키 — 루트에 {INDEXNOW_KEY}.txt 파일로 노출되며 빙·네이버·얀덱스에 즉시 색인 통보에 사용.
INDEXNOW_KEY = "3397165d01a7c228c01852a3837b2c1a"

# RSS 피드 메타
FEED_TITLE = "바로GO 금천구 출장마사지·홈타이 안내"
FEED_DESC = "금천구 출장마사지·홈타이 방문 가능 지역, 역세권·생활권 안내와 예약 정보를 제공합니다."

BRAND = "바로GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"
REGION = "서울특별시 금천구"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명·기능명만 표시한다.
NAV = [
    ("금천 홈", "/", []),
    ("지역별 안내", "/seoul/geumcheon/areas/", [
        ("대표동 전체", "/seoul/geumcheon/areas/"),
        ("가산동", "/seoul/geumcheon/gasan-dong-chuljangmassage/"),
        ("독산동", "/seoul/geumcheon/doksan-dong-chuljangmassage/"),
        ("시흥동", "/seoul/geumcheon/siheung-dong-chuljangmassage/"),
    ]),
    ("역세권 안내", "/seoul/geumcheon/stations/", [
        ("역세권 전체", "/seoul/geumcheon/stations/"),
        ("가산디지털단지역", "/seoul/geumcheon/gasan-digital-complex-station-chuljangmassage/"),
        ("독산역", "/seoul/geumcheon/doksan-station-chuljangmassage/"),
        ("금천구청역", "/seoul/geumcheon/geumcheon-gu-office-station-chuljangmassage/"),
        ("석수역 인접 생활권", "/seoul/geumcheon/seoksu-nearby-area-chuljangmassage/"),
        ("구로디지털단지역 인접 생활권", "/seoul/geumcheon/guro-digital-complex-nearby-area-chuljangmassage/"),
    ]),
    ("생활권 안내", "/seoul/geumcheon/districts/", [
        ("생활권 전체", "/seoul/geumcheon/districts/"),
        ("가산디지털단지 생활권", "/seoul/geumcheon/gasan-digital-complex-area-chuljangmassage/"),
        ("독산역 생활권", "/seoul/geumcheon/doksan-station-area-chuljangmassage/"),
        ("금천구청 인근", "/seoul/geumcheon/geumcheon-office-area-chuljangmassage/"),
        ("시흥사거리 생활권", "/seoul/geumcheon/siheung-sageori-area-chuljangmassage/"),
        ("금천패션아울렛 생활권", "/seoul/geumcheon/fashion-outlet-area-chuljangmassage/"),
        ("독산동 주거지 생활권", "/seoul/geumcheon/doksan-residential-area-chuljangmassage/"),
        ("시흥동 주거지 생활권", "/seoul/geumcheon/siheung-residential-area-chuljangmassage/"),
        ("안양천 인접 생활권", "/seoul/geumcheon/anyangcheon-area-chuljangmassage/"),
        ("신안산선 예정 생활권", "/seoul/geumcheon/sinansan-line-guide/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#area"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 가능 주소 확인", "/precautions/#address"),
        ("자택 이용 전 확인사항", "/precautions/#home"),
        ("숙소 이용 전 확인사항", "/precautions/#lodging"),
        ("사무실 인근 이용 전 확인사항", "/precautions/#office"),
        ("개인정보 처리 기준", "/precautions/#privacy"),
        ("고객 안전 안내", "/precautions/#safety"),
        ("불법·선정적 서비스 불가 안내", "/precautions/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/hometai-guide/", [
        ("홈타이란?", "/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/hometai-guide/#diff"),
        ("금천구 홈타이 이용 전 기준", "/hometai-guide/#standard"),
        ("지역별 이동 기준", "/hometai-guide/#move"),
        ("추가 비용 확인 기준", "/hometai-guide/#cost"),
        ("처음 이용하는 고객 안내", "/hometai-guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
