UPDATE book
   SET buy = IF(amount < buy, amount, buy),
       price = IF(buy = 0, price * 0.9, price);