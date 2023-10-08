SELECT name_author
  FROM book
       INNER JOIN author
       ON book.author_id = author.author_id
 GROUP BY name_author
HAVING COUNT(DISTINCT(genre_id)) = 1
 ORDER BY name_author;