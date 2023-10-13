SELECT name_department, name_program, plan,
       COUNT(*)        AS Количество,
       ROUND(COUNT(*) / plan, 2) AS Конкурс
  FROM program_enrollee
       JOIN program    USING(program_id)
       JOIN department USING(department_id)
 GROUP BY 1, 2, 3
 ORDER BY Конкурс DESC;