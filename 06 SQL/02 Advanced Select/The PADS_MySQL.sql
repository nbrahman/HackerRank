select n 
from
(
    select concat(name, '(', substring(occupation,1,1), ')') n, 1 flg
    from occupations
    union all
    select concat('There are a total of ', count(name), ' ', lower(occupation), 's.') n, 2 flg
    from occupations
    group by occupation
) t2
order by flg, n