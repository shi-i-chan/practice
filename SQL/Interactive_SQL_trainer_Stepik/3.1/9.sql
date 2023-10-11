SELECT name_subject,
       CONCAT(LEFT(name_question, 30), '...') AS Вопрос,
       COUNT(attempt_id) AS Всего_ответов,
       ROUND(SUM(is_correct) / COUNT(attempt_id) * 100, 2) AS Успешность
  FROM testing
       JOIN question USING(question_id)
       JOIN answer USING(answer_id)
       JOIN subject USING(subject_id)
 GROUP BY 1, 2
 ORDER BY name_subject, Успешность DESC, Вопрос;