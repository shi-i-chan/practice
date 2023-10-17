INSERT INTO step_keyword (step_id, keyword_id) 
SELECT step_id, keyword_id
  FROM step
       CROSS JOIN keyword
 WHERE step_name REGEXP (CONCAT('\\b', keyword_name, '\\b'));