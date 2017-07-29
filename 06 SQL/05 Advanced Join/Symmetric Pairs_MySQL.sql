select * from
(
    select f1.x, f1.y
    from functions f1, functions f2
    where f1.x = f2.y and f1.y = f2.x and f1.x < f1.y
    union
    select f.x, f.y
    from functions f
    where f.x = f.y
    group by x, y
    having count(*)>1
) t
order by t.x