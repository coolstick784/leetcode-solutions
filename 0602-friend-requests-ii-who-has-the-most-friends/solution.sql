-- Write your PostgreSQL query statement below
with requests as  
(
    select distinct requester_id as id, count(distinct accepter_id) as r_ct
    from RequestAccepted
    group by requester_id
),
accepts as (
        select distinct accepter_id as id, count(distinct requester_id) as a_ct
    from RequestAccepted
    group by accepter_id
),
totals as (
select coalesce(a.id, r.id) as id, coalesce(r.r_ct, 0) +coalesce( a.a_ct, 0) as num
from requests r
full join accepts a
on r.id = a.id
order by num desc
)
select * from totals where num = (select max(num) from totals)
