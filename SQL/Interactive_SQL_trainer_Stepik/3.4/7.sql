SELECT name_program, name_enrollee, itog
  FROM applicant_order
       JOIN program USING(program_id)
       JOIN enrollee USING(enrollee_id)
 WHERE str_id <= plan
 ORDER BY name_program, itog DESC;