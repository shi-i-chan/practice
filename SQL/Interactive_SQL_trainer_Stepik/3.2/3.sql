UPDATE attempt
   SET result = 
       (SELECT SUM(is_correct) / 3 * 100
         FROM testing
              JOIN answer USING(answer_id)
        WHERE attempt_id = 8)
 WHERE attempt_id = 8;