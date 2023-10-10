INSERT INTO buy_book(buy_id, book_id, amount)
SELECT 5, book_id, 2
  FROM book
       JOIN author USING(author_id)
 WHERE title = 'Лирика'
   AND name_author LIKE 'Пастернак%'
UNION
SELECT 5, book_id, 1
  FROM book
       JOIN author USING(author_id)
 WHERE title = 'Белая гвардия'
   AND name_author LIKE 'Булгаков%';