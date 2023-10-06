SELECT title, author 
  FROM book 
 WHERE title LIKE "% %"
   AND title NOT LIKE "_"
   AND (author LIKE "_% С.%" or author LIKE "_%.С.")
 ORDER BY title;