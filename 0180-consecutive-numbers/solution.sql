-- Write your PostgreSQL query statement below
with lag as (
select distinct num, lag(num, 1) over () as lag1, lag(num, 2) over () as lag2
from Logs
)
select distinct num as ConsecutiveNums from lag 
where num = lag1 and num=lag2
