SELECT id, name
  FROM departments as d
 WHERE EXISTS 
       (SELECT s.name
          FROM sales AS s
         WHERE s.department_id = d.id
           AND s.price > 98.00);