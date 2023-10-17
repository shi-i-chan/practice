WITH t1 AS 
(SELECT step_name, 
        SUM(CASE result WHEN 'correct' THEN 1 ELSE 0 END) AS correct,
        SUM(CASE result WHEN 'wrong'   THEN 1 ELSE 0 END) AS wrong
  FROM step 
       INNER JOIN step_student USING (step_id)
 GROUP BY step_name)
SELECT step_name AS Шаг,
       ROUND(correct / (correct + wrong) * 100) AS Успешность
  FROM t1
 ORDER BY Успешность, Шаг;