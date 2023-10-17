SELECT CONCAT(module_id, '.', lesson_position,
              IF(step_position < 10, ".0", "."),
              step_position, ' ', step_name) AS Шаг
  FROM step
       JOIN step_keyword USING(step_id)
       JOIN keyword USING(keyword_id)
       JOIN lesson USING(lesson_id)
       JOIN module USING(module_id)
 WHERE keyword_name IN ('MAX', 'AVG')
 GROUP BY Шаг
 HAVING COUNT(*) = 2
 ORDER BY Шаг;