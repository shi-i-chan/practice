SELECT name_program,
       name_enrollee,
       SUM(result) AS itog
  FROM enrollee
       JOIN program_enrollee USING(enrollee_id)
       JOIN program          USING(program_id)
       JOIN program_subject  USING(program_id)
       JOIN subject          USING(subject_id)
       JOIN enrollee_subject
         ON subject.subject_id = enrollee_subject.subject_id
            AND enrollee_subject.enrollee_id = enrollee.enrollee_id
 GROUP BY name_program, name_enrollee
 ORDER BY name_program, itog DESC;