/*
Enter your query here.
*/
select h.hacker_id, h.name
from hackers h, difficulty d, challenges c, submissions s
where h.hacker_id = s.hacker_id and d.difficulty_level = c.difficulty_level and d.score = s.score and c.challenge_id = s.challenge_id
group by h.hacker_id, h.name
having count(*) > 1
order by count(*) desc, h.hacker_id