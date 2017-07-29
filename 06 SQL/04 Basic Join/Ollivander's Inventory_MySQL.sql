/*
Enter your query here.
*/
select w.id, wp.age, w.coins_needed, w.power
from wands w, wands_property wp, 
	(
		select wp.age, w.power, min(w.coins_needed) minCoins
		from wands w, wands_property wp
		where wp.is_evil = 0 and w.code = wp.code
		group by w.power, wp.age
	) as wp_min
where w.code = wp.code and wp.is_evil = 0 and w.power = wp_min.power and w.coins_needed = wp_min.minCoins and wp.age = wp_min.age
order by w.power desc, wp.age desc