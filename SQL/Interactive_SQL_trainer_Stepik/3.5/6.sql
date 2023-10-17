SELECT Студент, Прогресс,
       CASE WHEN Прогресс = 100 THEN 'Сертификат с отличием'
            WHEN Прогресс >= 80 THEN 'Сертификат'
            ELSE ''
        END AS Результат
  FROM (SELECT student_name AS Студент,
               ROUND(COUNT(DISTINCT(step_id)) /
                    (SELECT COUNT(DISTINCT(step_id)) FROM step_student) * 100) AS Прогресс
          FROM student
               JOIN step_student USING(student_id)
         WHERE result = 'correct'
         GROUP BY Студент) AS sub_table
 ORDER BY Прогресс DESC, Студент;