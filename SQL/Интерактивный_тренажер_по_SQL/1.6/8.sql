SELECT MONTHNAME(date_first) AS Месяц,
       COUNT(MONTHNAME(date_first)) AS Количество
  FROM trip
 GROUP BY Месяц
 ORDER BY Количество DESC, Месяц;