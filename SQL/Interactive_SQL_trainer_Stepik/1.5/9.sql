CREATE TABLE ordering AS
SELECT author, title,
       (SELECT ROUND(AVG(amount))
          FROM book) AS amount
  FROM book
 WHERE book.amount <
       (SELECT ROUND(AVG(amount))
          FROM book);