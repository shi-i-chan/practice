SELECT author.name_author, book.title,
       COUNT(buy_book.book_id) AS Количество
  FROM book
       JOIN author        USING(author_id)
       LEFT JOIN buy_book USING(book_id)
       LEFT JOIN buy      USING(buy_id)
 GROUP BY author.name_author, book.title
 ORDER BY name_author, title;