UPDATE book
   SET genre_id = 
       CASE
       WHEN book_id = 10
       THEN (SELECT genre_id
               FROM genre
              WHERE name_genre = 'Поэзия')
       WHEN book_id = 11
       THEN (SELECT genre_id
               FROM genre
              WHERE name_genre = 'Приключения')
       ELSE book.genre_id
       END;