SELECT SUM(price)
  FROM book
 WHERE price IN
       (SELECT MIN(price)
          FROM book
         GROUP BY author);