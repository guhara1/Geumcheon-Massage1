# 메인 페이지 — 금천구 허브. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY, REGION
from .components import INFO_BLOCK, CTA

_JSONLD = f"""<meta name="naver-site-verification" content="1754e535be5d16cd60a43b37a2a21d36ac4ccab2" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "금천구 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "금천구 출장마사지·홈타이 예약 전 가산동, 독산동, 시흥동 생활권 안내",
  "inLanguage": "ko-KR",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "{BRAND}",
    "url": "{BASE_URL}/"
  }},
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "{REGION} 전지역 방문형 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "{REGION}"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "areaServed": "KR",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "금천구 어느 지역까지 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가산동, 독산동, 시흥동을 중심으로 금천구 전지역을 안내합니다. 예약 가능 여부는 정확한 주소와 예약 시간을 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "독산1동, 시흥1동 같은 번호 동 페이지는 왜 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "독산1~4동은 독산동 대표 페이지, 시흥1~5동은 시흥동 대표 페이지에서 세부 생활권으로 통합 안내해 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "둘 다 방문형 관리 서비스를 가리키는 표현입니다. 차이와 이용 기준은 홈타이 이용 가이드에서 정리해 안내합니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Visiting Care · 금천구 전지역</p>
    <h1>금천구 출장마사지 · 금천구 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">가산동·독산동·시흥동 생활권을 기준으로 방문 가능 지역과 예약 전 확인사항을 안내합니다.<br>자택·숙소·사무실 인근까지 전화 한 통으로 확인하세요.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/geumcheon/areas/">대표동 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>3개</strong><span>대표동</span></li>
      <li><strong>5개</strong><span>역세권 안내</span></li>
      <li><strong>8개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>금천구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>금천구 출장마사지를 찾는 분들은 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 금천구는 서울 서남부 자치구로, 가산디지털단지역 중심의 업무지구, 독산역·독산동 주거 생활권, 금천구청역·시흥동 생활권이 함께 있습니다. 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 자세한 절차는 <a href="/reservation/">금천구 출장마사지 예약 안내</a>에서 단계별로 정리해 두었습니다.</p>
</section>

<section id="difference">
<h2>가산동·독산동·시흥동 생활권 차이</h2>
<p>같은 금천구라도 세 대표동은 생활 리듬이 다릅니다. 가산동은 가산디지털단지역을 끼고 업무·쇼핑·주거가 섞여 있어 사무실·숙소 인근 문의가 많습니다. 독산동은 독산역, 독산사거리, 말미사거리, 시흥대로를 따라 이어지는 주거 생활권이 중심입니다. 시흥동은 금천구청역과 시흥사거리, 안양천 인접 생활권을 포함하는 금천구 남부의 넓은 주거권입니다. 동마다 이동 시간과 방문 준비가 달라, 각 페이지에서 지역별 이동 기준을 따로 설명합니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표동은 가산동, 독산동, 시흥동 세 곳입니다. 독산1~4동, 시흥1~5동처럼 번호로 나뉜 행정동은 개별 페이지로 만들지 않고, 독산동·시흥동 대표 페이지 안에서 세부 생활권으로 설명합니다. 거주하시거나 머무시는 동을 아래에서 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/geumcheon/gasan-dong-chuljangmassage/">가산동 출장마사지</a></li>
<li><a href="/seoul/geumcheon/doksan-dong-chuljangmassage/">독산동 출장마사지</a></li>
<li><a href="/seoul/geumcheon/siheung-dong-chuljangmassage/">시흥동 출장마사지</a></li>
</ul>
<p>금천구 전체 대표동 구조는 <a href="/seoul/geumcheon/areas/">금천구 대표동별 출장마사지 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>가산디지털단지역·독산역·금천구청역 역세권 안내</h2>
<p>역세권 페이지는 실제 검색 의도와 가까운 제목으로 운영합니다. 가산디지털단지역은 업무지구와 이동 기준을, 독산역은 독산동 주거 생활권을, 금천구청역은 시흥동·금천구청 인근을 담당합니다. 환승역이나 인접역을 노선별로 쪼개지 않고, 가산디지털단지역은 1개 URL만 두며, 구로디지털단지역·석수역은 단독 역 페이지 대신 인접 생활권으로 설명합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/geumcheon/gasan-digital-complex-station-chuljangmassage/">가산디지털단지역 출장마사지</a></li>
<li><a href="/seoul/geumcheon/doksan-station-chuljangmassage/">독산역 출장마사지 방문 안내</a></li>
<li><a href="/seoul/geumcheon/geumcheon-gu-office-station-chuljangmassage/">금천구청역 출장마사지</a></li>
</ul>
<p>역 전체 목록과 인접 생활권 처리 기준은 <a href="/seoul/geumcheon/stations/">금천구 역세권 출장마사지 안내</a>에서 확인하세요.</p>
</section>

<section id="check">
<h2>금천구 홈타이 예약 전 확인사항</h2>
<p>금천구 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 업무지구가 많은 가산동은 평일 저녁 이동 시간이, 시흥동 남부나 석수역 인접권은 차량 이동 기준이 달라질 수 있습니다. 예약 전 정확한 주소, 공동현관 출입 방법, 조용한 공간 여부를 확인해 주시면 방문이 매끄럽습니다. 홈타이와 출장마사지의 차이는 <a href="/hometai-guide/">금천구 홈타이 이용 가이드</a>에, 방문 형태별 준비사항은 <a href="/precautions/">출장마사지 이용 전 확인사항</a>에 정리되어 있습니다.</p>
</section>

<section id="dedup">
<h2>금천구 페이지 중복 방지 운영 기준</h2>
<p>금천구 홈타이 사이트에서 가장 중요한 부분은 행정동을 무리하게 쪼개지 않는 것입니다. 독산1~4동, 시흥1~5동을 각각 개별 페이지로 만들면 본문이 비슷해질 위험이 큽니다. 그래서 독산동·시흥동 대표 페이지로 통합하고, 가산동은 단독 대표 페이지로 운영합니다. 신안산선 예정역인 시흥사거리역·신독산역은 개통 전까지 단독 색인 페이지를 만들지 않고 <a href="/seoul/geumcheon/sinansan-line-guide/">신안산선 예정 생활권 안내</a>에서 보조 설명으로만 다룹니다. 같은 본문에서 지역명만 바꾸는 방식은 사용하지 않습니다.</p>
</section>

<section id="howto">
<h2>금천구 출장마사지 사이트 이용 방법</h2>
<p>메인페이지는 금천구 전체 안내를, 대표동 페이지는 가산동·독산동·시흥동 검색을, 역세권 페이지는 가산디지털단지역·독산역·금천구청역을, 생활권 페이지는 더 좁은 거점을 담당합니다. 본인에게 익숙한 기준으로 페이지를 골라 방문 가능 여부를 확인하신 뒤, 예약 전화에서 정확한 위치와 희망 시간을 알려주시면 됩니다. 모든 안내는 정보형 톤을 유지하고 허위 후기는 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>금천구 어느 지역까지 방문이 가능한가요?</h3>
<p>가산동, 독산동, 시흥동을 중심으로 금천구 전지역을 안내합니다. 예약 가능 여부는 정확한 주소와 예약 시간을 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>독산1동, 시흥1동 같은 번호 동 페이지는 왜 없나요?</h3>
<p>독산1~4동은 독산동 대표 페이지, 시흥1~5동은 시흥동 대표 페이지에서 세부 생활권으로 통합 안내해 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>출장마사지와 홈타이는 어떻게 다른가요?</h3>
<p>둘 다 방문형 관리 서비스를 가리키는 표현입니다. 차이와 이용 기준은 <a href="/hometai-guide/">금천구 홈타이 이용 가이드</a>에서 정리해 안내합니다.</p>
</div>
</section>

{INFO_BLOCK}
{CTA}
"""

PAGE = {
    "path": "",
    "title": "금천구 출장마사지｜가산·독산·시흥 홈타이 지역 안내",
    "desc": "금천구 출장마사지·홈타이 예약 전 가산동, 독산동, 시흥동 생활권을 확인하세요.",
    "h1": "금천구 출장마사지 · 금천구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
