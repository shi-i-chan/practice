SELECT title, author, amount, ROUND(price * 0.7, 2) AS new_price
  FROM book;