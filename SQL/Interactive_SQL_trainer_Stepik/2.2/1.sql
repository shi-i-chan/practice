SELECT b.title, g.name_genre, b.price
  FROM book AS b
       INNER JOIN genre AS g
       ON b.amount > 8
          AND b.genre_id = g.genre_id
 ORDER BY price DESC;