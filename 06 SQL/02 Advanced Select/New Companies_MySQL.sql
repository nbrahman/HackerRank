select c.company_Code, c.founder, lmcnt, smcnt, mcnt, ecnt
from company c, (select company_code, count(distinct lead_manager_code) lmcnt from lead_manager group by company_code) lm, (select company_code, count(distinct senior_manager_code) smcnt from senior_manager group by company_code) sm, (select company_code, count(distinct manager_code) mcnt from manager group by company_code) m, (select company_code, count(distinct employee_code) ecnt from employee group by company_code) e
where c.company_code = lm.company_code and c.company_code = sm.company_Code and c.company_code = m.company_code and c.company_code=e.company_code
group by c.company_Code, c.founder
order by c.company_code