# Write your MySQL query statement below

select emp_id, event_day as day, sum(time) as total_time
from(
select emp_id, event_day, out_time-in_time as time
from Employees) a
group by emp_id, event_day;
