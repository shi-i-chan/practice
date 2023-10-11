SELECT name_student, result
  FROM student
       JOIN attempt USING(student_id)
 WHERE result = 
       (SELECT MAX(result)
          FROM attempt)
 ORDER BY name_student;