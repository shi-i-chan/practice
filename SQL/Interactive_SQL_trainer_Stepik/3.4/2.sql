DELETE FROM applicant
 USING applicant
       JOIN (SELECT program_enrollee.program_id, program_enrollee.enrollee_id 
               FROM program
                    JOIN program_subject  USING(program_id)
                    JOIN program_enrollee USING(program_id)
                    JOIN enrollee_subject
                      ON enrollee_subject.enrollee_id = program_enrollee.enrollee_id
                         AND enrollee_subject.subject_id = program_subject.subject_id
              WHERE result < min_result) AS t
         ON applicant.program_id = t.program_id
            AND applicant.enrollee_id = t.enrollee_id;