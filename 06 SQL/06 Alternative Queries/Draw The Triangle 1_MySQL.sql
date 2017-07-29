/*
Enter your query here.
*/
select repeat('* ', @count := @count - 1) from information_schema.tables, (select @count := 21) t limit 20