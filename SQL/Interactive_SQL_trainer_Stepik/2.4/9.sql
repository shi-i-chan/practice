SELECT DISTINCT(client.name_client)
  FROM buy
  JOIN client   USING(client_id)
  JOIN buy_book USING(buy_id)
  JOIN book     USING(book_id)
  JOIN author   USING(author_id)
WHERE author.name_author = 'Достоевский Ф.М.'
ORDER BY name_client;