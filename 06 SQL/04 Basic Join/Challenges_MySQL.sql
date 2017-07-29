/*
Enter your query here.
*/
select distinct h.hacker_id, h.name, t.cnt
from hackers h,
			(
				select hacker_id, count(challenge_id) cnt
				from challenges c
                group by hacker_id
			) t,
			(
				select max(cnt) max_cnt
                from
                (
                    select hacker_id, count(challenge_id) cnt
                    from challenges c
                    group by hacker_id
                ) t
			) t2,
			(
				select cnt, count(cnt) cnt_cnt
                from
                (
                    select hacker_id, count(challenge_id) cnt
                    from challenges c
                    group by hacker_id
                ) t
                group by cnt
                having count(cnt) = 1
			) t3
where t.hacker_id = h.hacker_id and ((t3.cnt_cnt = 1 and t3.cnt = t.cnt) or t.cnt = t2.max_cnt)
order by t.cnt desc, h.hacker_id