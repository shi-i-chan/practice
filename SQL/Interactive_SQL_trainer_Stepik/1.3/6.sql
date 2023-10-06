SELECT ROUND(AVG(price), 2) AS Средняя_цена,
       ROUND(SUM(price * amount), 2) AS Стоимость
  FROM book
 WHERE amount >= 5
   AND amount <= 14;