UPDATE book
   SET price = price * 0.9
 WHERE amount >= 5
   AND amount <= 10;