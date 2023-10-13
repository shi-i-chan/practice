SELECT name_program
  FROM program
       JOIN program_subject USING(program_id)
       JOIN subject         USING(subject_id)
 WHERE name_subject = 'Информатика'
 ORDER BY name_program DESC;