UPDATE fine AS f, (
    SELECT name, number_plate, violation
      FROM fine
     GROUP BY name, number_plate, violation
    HAVING count(*) >= 2
    ) AS dv
   SET f.sum_fine = f.sum_fine * 2
 WHERE f.date_payment IS NULL
   AND (f.name = dv.name
		   AND f.violation = dv.violation);