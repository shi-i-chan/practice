SELECT DISTINCT buy.buy_id, buy_step.date_step_end
  FROM buy
       LEFT JOIN buy_step USING(buy_id)
       JOIN step
       ON buy_step.step_id = 
          (SELECT step.step_id
             FROM step
            WHERE name_step = 'Оплата')
 WHERE buy_step.date_step_end IS NOT NULL;