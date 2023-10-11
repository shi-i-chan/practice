SELECT name_question, name_answer,
       IF(is_correct, 'Верно', 'Неверно') AS Результат
  FROM question
       JOIN testing USING(question_id)
       JOIN answer  USING(answer_id)
 WHERE attempt_id = 7;