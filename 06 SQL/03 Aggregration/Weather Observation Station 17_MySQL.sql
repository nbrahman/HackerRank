select round(max(s.long_W), 4)
from station s, (select min(lat_n) lat_n from station where lat_n > 38.7780) t
where s.lat_n = t.lat_n