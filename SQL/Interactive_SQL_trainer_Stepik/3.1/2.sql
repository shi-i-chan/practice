SELECT name_subject,
       COUNT(result) AS Количество,
       ROUND(SUM(result) / COUNT(result), 2) AS Среднее
  FROM subject
       LEFT JOIN attempt USING(subject_id)
 GROUP BY name_subject;