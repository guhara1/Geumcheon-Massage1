# 전체 페이지 목록 집계
from . import main, areas, stations, districts, sinansan, info, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + districts.PAGES
    + [sinansan.PAGE]
    + info.PAGES
    + [about.PAGE]
)
