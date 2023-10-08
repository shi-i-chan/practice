SELECT genre.name_genre,
       SUM(buy_book.amount) AS Количество
  FROM buy_book
  JOIN book  USING(book_id)
  JOIN genre USING(genre_id)
GROUP BY genre.name_genre
LIMIT 1;