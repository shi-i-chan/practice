SELECT name_program
  FROM program
       JOIN program_subject USING(program_id)
       JOIN subject         USING(subject_id)
 WHERE name_subject IN ('Математика', 'Информатика')
 GROUP BY 1
 HAVING COUNT(name_subject) = 2
 ORDER BY name_program;