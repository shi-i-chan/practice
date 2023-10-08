SELECT join_table.title, SUM(Количество) AS Количество, SUM(Сумма) AS Сумма
  FROM
(
SELECT book.title, 
        SUM(buy_archive.amount) AS Количество,
        SUM(buy_archive.price * buy_archive.amount) AS Сумма
   FROM buy_archive
        JOIN book USING(book_id)
  GROUP BY title

UNION ALL

SELECT title,
        SUM(buy_book.amount) AS Количество,
        SUM(book.price * buy_book.amount) AS Сумма
   FROM book
        JOIN buy_book USING(book_id)
        JOIN buy_step USING(buy_id)
        JOIN step     USING(step_id)
  WHERE buy_step.date_step_end IS NOT NULL
        AND step.name_step = 'Оплата'
  GROUP BY title
) AS join_table
GROUP BY title
ORDER BY Сумма DESC;