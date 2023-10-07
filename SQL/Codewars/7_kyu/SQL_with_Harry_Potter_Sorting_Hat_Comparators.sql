SELECT s.id, s.name, s.quality1, s.quality2
  FROM students AS s
 WHERE (s.quality1 = 'evil' AND s.quality2 = 'cunning')
    OR (s.quality1 = 'brave' AND s.quality2 != 'evil')
    OR (s.quality1 = 'studious' OR s.quality2 = 'intelligent')
    OR (s.quality1 = 'hufflepuff' OR s.quality2 = 'hufflepuff')
 ORDER BY s.id ASC;