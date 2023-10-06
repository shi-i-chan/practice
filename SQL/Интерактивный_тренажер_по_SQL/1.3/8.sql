SELECT author,
       COUNT(title) AS n_titles,
       MIN(price) AS min_price,
       SUM(amount) AS amount
  FROM book
 WHERE price > 500
 GROUP BY author
HAVING n_titles > 1;