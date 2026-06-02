-- Write your PostgreSQL query statement below
with tmp1 as (
select *, lag(id, 1) over () as lag1 , lag(id, 2) over () as lag2, lag(people, 1) over () as p1, lag(people, 2) over () as p2 from Stadium),
tmp2 as (
select id, visit_date, people
from tmp1 where id = lag1 +1 and id=lag2 +2
and p1 >= 100 and p2 >= 100
and people >= 100)
select s.* from Stadium s
where exists (
    select 1 from tmp2 t where s.id = t.id or s.id = t.id-1 or s.id = t.id-2
)

order by visit_date

