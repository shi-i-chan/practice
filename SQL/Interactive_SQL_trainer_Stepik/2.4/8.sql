SELECT buy_step.buy_id,
       DATEDIFF(buy_step.date_step_end, buy_step.date_step_beg) AS Количество_дней,
       IF (DATEDIFF(buy_step.date_step_end, buy_step.date_step_beg) - city.days_delivery < 0,
           0, DATEDIFF(buy_step.date_step_end, buy_step.date_step_beg) - city.days_delivery) AS 'Опоздание'
  FROM buy_step
       JOIN buy    USING(buy_id)
       JOIN client USING(client_id)
       JOIN city   USING(city_id)
 WHERE buy_step.step_id =
       (SELECT step.step_id
          FROM step
         WHERE step.name_step = 'Транспортировка')
       AND buy_step.date_step_end IS NOT NULL;