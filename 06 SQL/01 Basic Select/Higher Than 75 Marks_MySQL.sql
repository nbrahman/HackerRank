select NAME
from STUDENTS
where MARKS > 75
order by substring(NAME, length(NAME)-2, 3) asc, ID asc