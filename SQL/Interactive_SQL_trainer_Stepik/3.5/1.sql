SELECT CONCAT(LEFT(CONCAT(module_id, ' ', module_name), 16), '...') AS Модуль,
       CONCAT(LEFT(CONCAT(module_id, '.', lesson_position, ' ', lesson_name), 16), '...') AS Урок,
       CONCAT(module_id, '.', lesson_position, '.', step_position, ' ', step_name) AS Шаг
  FROM step
       JOIN lesson USING(lesson_id)
       JOIN module USING(module_id)
 WHERE step_name LIKE '%ложенн% запрос%'
 ORDER BY module_id, lesson_id, step_position;