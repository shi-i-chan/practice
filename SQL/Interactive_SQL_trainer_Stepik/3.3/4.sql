SELECT name_program
  FROM program
       JOIN program_subject USING(program_id)
 GROUP BY 1
HAVING MIN(min_result) >= 40
 ORDER BY name_program;