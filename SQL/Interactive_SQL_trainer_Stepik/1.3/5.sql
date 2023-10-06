SELECT ROUND(MIN(price), 2) AS Минимальная_цена,
       ROUND(MAX(price), 2) AS Максимальная_цена,
       ROUND(AVG(price), 2) AS Средняя_цена
  FROM book;