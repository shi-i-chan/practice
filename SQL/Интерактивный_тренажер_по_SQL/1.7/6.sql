UPDATE fine AS f, payment AS p
   SET f.date_payment = p.date_payment,
       f.sum_fine = IF(DATEDIFF(p.date_payment, p.date_violation) <= 20, f.sum_fine / 2, f.sum_fine)
 WHERE f.name = p.name
   AND f.number_plate = p.number_plate
   AND f.violation = p.violation
   AND f.date_violation = p.date_violation;