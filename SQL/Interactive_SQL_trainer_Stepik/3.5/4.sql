SELECT CASE WHEN rate <= 10 THEN 'I'
            WHEN rate <= 15 THEN 'II'
            WHEN rate <= 27 THEN 'III'
            ELSE 'IV'
        END AS Группа,
       CASE WHEN rate <= 10 THEN 'от 0 до 10'
            WHEN rate <= 15 THEN 'от 11 до 15'
            WHEN rate <= 27 THEN 'от 16 до 27'
            ELSE 'больше 27'
        END AS Интервал,
        COUNT(student_name) AS Количество
  FROM (SELECT student_name, COUNT(step_id) AS rate
          FROM student
               JOIN step_student USING(student_id)
         WHERE result = 'correct'
         GROUP BY student_name) AS sub_table
 GROUP BY Группа, Интервал
 ORDER BY Группа;