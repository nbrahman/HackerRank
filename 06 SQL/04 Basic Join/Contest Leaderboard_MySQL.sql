/*
Enter your query here.
*/
select h.hacker_id, h.name, sum(s.score)
from hackers h, (select hacker_id, challenge_id, max(score) score from submissions group by hacker_id, challenge_id) s
where h.hacker_id = s.hacker_id
group by h.hacker_id, h.name
having sum(s.score)>0
order by sum(s.score) desc, hacker_id