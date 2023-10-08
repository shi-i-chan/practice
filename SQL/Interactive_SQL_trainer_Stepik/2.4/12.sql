(SELECT YEAR(date_payment) AS Год,
        MONTHNAME(date_payment) AS Месяц,
        SUM(price * amount) AS Сумма
   FROM buy_archive
  GROUP BY Год, Месяц)
UNION
(SELECT YEAR(date_step_beg) AS Год,
        MONTHNAME(date_step_beg) AS Месяц,
        SUM(book.price * buy_book.amount) AS Сумма
   FROM book
        JOIN buy_book USING(book_id)
        JOIN buy_step USING(buy_id)
        JOIN step     USING(step_id)
  WHERE buy_step.date_step_end IS NOT NULL
        AND step.name_step = 'Оплата'
  GROUP BY Год, Месяц)
  ORDER BY Месяц ASC, Год ASC;