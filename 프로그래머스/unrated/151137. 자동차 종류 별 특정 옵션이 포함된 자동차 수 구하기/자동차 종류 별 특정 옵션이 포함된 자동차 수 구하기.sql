-- 코드를 입력하세요
SELECT car_type, count(car_id) as CARS
from car_rental_company_car
where options like '%시트%'
group by car_type
order by 1 asc;