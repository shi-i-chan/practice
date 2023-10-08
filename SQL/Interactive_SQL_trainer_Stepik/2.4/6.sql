SELECT buy.buy_id, step.name_step
  FROM buy
       JOIN buy_step USING(buy_id)
       JOIN step     USING(step_id)
 WHERE buy_step.date_step_beg IS NOT NULL
       AND buy_step.date_step_end IS NULL;