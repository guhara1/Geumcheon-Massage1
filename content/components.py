# 공용 컴포넌트 — 예약/결제/이동비 안내 블록과 예약 CTA.
# 가격을 임의로 만들지 않고, 실제 비용은 전화 상담에서 확인하도록 안내한다.
# 안내 블록은 class="pricing" 으로 두어 페이지 고유 본문 글자수 측정에서 제외한다.
from .site import PHONE, PHONE_DISPLAY

# 예약·결제·이동비 신뢰 안내 블록(공용). 페이지마다 동일하게 들어가며
# 본문 고유 글자수 계산에서는 빠진다.
INFO_BLOCK = f"""
<section class="pricing" id="reserve-info">
<h2>예약·결제·이동비 안내</h2>
<p class="pricing-lead">금천구 방문형 관리 서비스는 아래 기준으로 안내됩니다. 정확한 비용과 가능 시간은 예약 전화에서 위치를 기준으로 확인해 드립니다.</p>
<div class="price-grid">
  <div class="price-card">
    <p class="price-name">방문 가능 지역</p>
    <p class="price-value">금천구<span>전지역</span></p>
    <p class="price-time">가산·독산·시흥</p>
    <p class="price-desc">정확한 주소 기준 확인</p>
    <a class="price-btn" href="tel:{PHONE}">지역 확인</a>
  </div>
  <div class="price-card featured">
    <p class="price-badge">전화 확인</p>
    <p class="price-name">예약 상담</p>
    <p class="price-value">24<span>시간</span></p>
    <p class="price-time">연중무휴</p>
    <p class="price-desc">위치·시간·코스 안내</p>
    <a class="price-btn primary" href="tel:{PHONE}">예약 문의</a>
  </div>
  <div class="price-card">
    <p class="price-name">추가 이동비</p>
    <p class="price-value">사전<span>안내</span></p>
    <p class="price-time">거리 기준</p>
    <p class="price-desc">예약 시 미리 확인</p>
    <a class="price-btn" href="tel:{PHONE}">이동비 확인</a>
  </div>
</div>
<p class="price-note">결제 방식, 추가 이동비, 취소 기준은 예약 단계에서 명확히 안내합니다. <a href="/reservation/">예약 안내 자세히 보기 →</a></p>
</section>
"""


def cta(text="방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다."):
    return f"""
<section class="cta" id="contact">
<h2>예약문의</h2>
<p>{text}</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""


CTA = cta()
