SELECT genre.name_genre,
       SUM(buy_book.amount) AS Количество
  FROM buy_book
  JOIN book  USING(book_id)
  JOIN genre USING(genre_id)
GROUP BY genre.name_genre
HAVING SUM(buy_book.amount) =
          (SELECT SUM(buy_book.amount)
             FROM buy_book
             JOIN book USING(book_id)
             JOIN genre USING(genre_id)
            GROUP BY genre.name_genre
            LIMIT 1);