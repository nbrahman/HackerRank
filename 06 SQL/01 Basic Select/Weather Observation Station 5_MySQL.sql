select * 
from 
(
    select CITY, length(CITY)
    from STATION
    order by length(CITY) asc, city asc
    limit 1
) temp
union
select * 
from 
(
    select CITY, length(CITY)
    from STATION
    order by length(CITY) desc, city asc
    limit 1
) temp