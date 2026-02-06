-- Write your PostgreSQL query statement below
select distinct num as ConsecutiveNums from (
select id, num, lag(num, 1) over () as lag1, lag(num, 2) over () as lag2  from Logs
)
where num = lag1 and num = lag2

