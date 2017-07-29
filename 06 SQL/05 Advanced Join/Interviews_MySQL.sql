select co.contest_id, co.hacker_id, co.name, sum(ss.sts), sum(ss.stas), sum(vs.stv), sum(vs.stuv)
from contests co, colleges cl, challenges ch, 
    (select ch2.challenge_id, sum(vs2.total_views) stv, sum(vs2.total_unique_views) stuv
     from challenges ch2 left join  view_stats vs2 on ch2.challenge_id = vs2.challenge_id group by ch2.challenge_id) vs, 
    (select ch2.challenge_id, sum(ss2.total_submissions) sts, sum(ss2.total_accepted_submissions) stas
     from challenges ch2 left join  submission_stats ss2 on ch2.challenge_id = ss2.challenge_id group by ch2.challenge_id) ss 
where co.contest_id = cl.contest_id and cl.college_id = ch.college_id and vs.challenge_id = ch.challenge_id and ss.challenge_id = ch.challenge_id
group by co.contest_id, co.hacker_id, co.name
having sum(ss.sts) + sum(ss.stas) + sum(vs.stv) + sum(vs.stuv) != 0
order by co.contest_id