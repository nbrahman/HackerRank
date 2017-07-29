select N, case 
	when b1.p is null then 'Root' 
	when (select count(*) cnt from bst b2 where b2.p=b1.N)=0 then 'Leaf' else 'Inner' end
from bst b1
order by b1.N
