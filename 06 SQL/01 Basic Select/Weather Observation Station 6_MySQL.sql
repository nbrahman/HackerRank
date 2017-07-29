select CITY
from STATION
where substring(CITY,1,1) in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')