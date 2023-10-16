UPDATE applicant
       JOIN (SELECT enrollee_id, COALESCE(SUM(bonus), 0) AS bonus
               FROM enrollee
                    LEFT JOIN enrollee_achievement USING(enrollee_id)
                    LEFT JOIN achievement USING(achievement_id)
              GROUP BY 1) AS b USING(enrollee_id)
  SET itog = itog + bonus;