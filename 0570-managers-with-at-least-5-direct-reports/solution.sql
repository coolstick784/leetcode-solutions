-- Write your PostgreSQL query statement below
with tmp1 as (
    select managerId, count(*) as ct
    from Employee
    group by managerId
    having count(*)  >= 5
)
select e.name as name
from Employee e
join tmp1 t
on e.id = t.managerId
