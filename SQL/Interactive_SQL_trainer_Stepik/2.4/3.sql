SELECT city.name_city, COUNT(buy.buy_id) AS Количество
  FROM buy
       JOIN client USING(client_id)
       JOIN city   USING(city_id)
 GROUP BY city.name_city
 ORDER BY Количество DESC, name_city;