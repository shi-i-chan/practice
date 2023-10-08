SELECT book.title AS Название,
       supply.author AS Автор,
       (book.amount + supply.amount) AS Количество
  FROM supply
       INNER JOIN book
       ON supply.title = book.title
	       AND supply.amount = book.amount
       INNER JOIN author
	   ON author.author_id = book.author_id
 WHERE book.title = supply.title
   AND book.price = supply.price;