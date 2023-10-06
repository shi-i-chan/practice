SELECT author,
       ROUND(SUM(price * amount), 2) AS Стоимость
  FROM book
 WHERE title <> 'Идиот'
   AND title <> 'Белая гвардия'
 GROUP BY author
HAVING Стоимость > 5000
 ORDER BY Стоимость DESC;