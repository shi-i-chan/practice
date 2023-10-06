UPDATE fine AS f, traffic_violation AS tv
   SET f.sum_fine = tv.sum_fine
 WHERE tv.violation = f.violation
   AND f.sum_fine IS NULL;