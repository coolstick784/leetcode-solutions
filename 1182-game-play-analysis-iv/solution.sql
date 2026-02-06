-- Write your PostgreSQL query statement below


with tmp2 as (
select cast(count(*) as numeric) as n from Activity a
join (
select player_id, min(event_date) as md
from Activity
group by player_id
) b
on a.player_id = b.player_id
where event_date - 1 = md
),
tmp3 as (
    select cast(count(*) as numeric) as total from (select distinct player_id from Activity)
),
tmp4 as (
select n/total as fraction
from tmp2 cross join tmp3
)
select round(fraction, 2) as fraction
from tmp4

