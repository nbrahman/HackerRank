select round(max(s.long_W), 4)
from station s, (select max(lat_n) lat_n from station where lat_n < 137.2345) t
where s.lat_n = t.lat_n