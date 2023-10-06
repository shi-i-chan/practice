INSERT INTO book(title, author, price, amount)
SELECT title, author, price, amount
  FROM supply
 WHERE author <> 'Булгаков М.А.'
   AND author <> 'Достоевский Ф.М.';