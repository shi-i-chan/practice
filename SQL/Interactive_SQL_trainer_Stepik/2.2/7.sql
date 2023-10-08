SELECT title, name_author, name_genre, price, amount
  FROM author 
       INNER JOIN book
       ON author.author_id = book.author_id
       INNER JOIN genre
       ON  book.genre_id = genre.genre_id
 WHERE genre.genre_id IN
       (SELECT query_in_1.genre_id
          FROM (SELECT genre_id, SUM(amount) AS sum_amount
                  FROM book
                 GROUP BY genre_id ) AS query_in_1
               INNER JOIN (SELECT genre_id, SUM(amount) AS sum_amount
                             FROM book
                            GROUP BY genre_id
                            ORDER BY sum_amount DESC
                            LIMIT 1) AS query_in_2
               ON query_in_1.sum_amount= query_in_2.sum_amount)
 ORDER BY title ASC;