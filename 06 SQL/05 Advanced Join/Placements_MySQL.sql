select s.name
from students s, friends f, packages p1, packages p2
where f.id = p1.id and f.friend_id = p2.id and f.id = s.id and p1.salary < p2.salary
order by p2.salary asc