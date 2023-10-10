UPDATE book, buy_book
   SET book.amount = book.amount - buy_book.amount
 WHERE buy_book.buy_id = 5
   AND buy_book.book_id = book.book_id;