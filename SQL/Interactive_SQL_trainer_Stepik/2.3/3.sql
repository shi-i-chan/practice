INSERT INTO book(title, author_id, price, amount)
SELECT title, author.author_id, price, amount
  FROM author
       INNER JOIN supply
       ON supply.author = author.name_author
 WHERE amount <> 0;