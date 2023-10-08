DELETE
  FROM author
 USING book
       INNER JOIN author
       ON book.author_id = author.author_id
       INNER JOIN genre
       ON book.genre_id = genre.genre_id
 WHERE genre.name_genre = 'Поэзия';