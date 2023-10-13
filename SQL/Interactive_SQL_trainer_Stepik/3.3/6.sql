SELECT name_enrollee, COALESCE(SUM(bonus), 0) AS Бонус
  FROM enrollee
       LEFT JOIN enrollee_achievement USING(enrollee_id)
       LEFT JOIN achievement USING(achievement_id)
 GROUP BY 1
 ORDER BY 1;