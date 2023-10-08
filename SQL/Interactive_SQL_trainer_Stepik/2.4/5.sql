SELECT buy.buy_id, client.name_client,
       SUM(buy_book.amount * book.price) AS Стоимость
  FROM buy
       JOIN client   USING(client_id)
       JOIN buy_book USING(buy_id)
       JOIN book     USING(book_id)
 GROUP BY buy.buy_id;