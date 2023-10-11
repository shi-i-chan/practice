SELECT name_student, date_attempt, result
  FROM student
       JOIN attempt USING(student_id)
       JOIN subject USING(subject_id)
 WHERE name_subject = 'Основы баз данных'
 ORDER BY result DESC;