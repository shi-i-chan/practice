INSERT INTO buy_step (buy_id, step_id, date_step_beg, date_step_end)
SELECT buy_id, step_id, Null, Null
  FROM buy
       CROSS JOIN step
 WHERE buy_id = 5;