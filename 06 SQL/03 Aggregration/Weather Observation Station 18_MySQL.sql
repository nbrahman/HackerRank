select round(abs(x1-x2)+abs(y1-y2), 4)
from
(
    select max(lat_n) x1, max(long_w) y1, min(lat_n) x2, min(long_w) y2
    from station
) t