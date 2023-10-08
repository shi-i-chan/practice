SELECT author.name_author, SUM(book.amount) AS Количество
  FROM author
       LEFT JOIN book
       ON book.author_id = author.author_id
 GROUP BY name_author
HAVING Количество < 10
       OR Количество IS NULL 
 ORDER BY Количество ASC;