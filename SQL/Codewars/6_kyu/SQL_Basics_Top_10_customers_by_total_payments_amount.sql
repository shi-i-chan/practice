SELECT c.customer_id, c.email,
       COUNT(p.customer_id)::INT AS payments_count,
       SUM(p.amount)::FLOAT AS total_amount
  FROM customer AS c, payment AS p
 WHERE p.customer_id = c.customer_id
 GROUP BY c.customer_id
 ORDER BY total_amount DESC
 LIMIT 10;