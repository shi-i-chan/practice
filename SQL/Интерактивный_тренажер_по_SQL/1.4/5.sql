SELECT title, author, amount,
       (SELECT ABS(amount -
               (SELECT MAX(amount)
                  FROM book))
       ) AS Заказ
  FROM book
 WHERE amount <
       (SELECT MAX(amount)
          FROM book);