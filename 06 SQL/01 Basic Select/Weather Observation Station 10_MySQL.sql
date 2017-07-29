select distinct CITY
from STATION
where substring(CITY,length(CITY),1) not in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')