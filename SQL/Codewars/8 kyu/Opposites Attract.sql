SELECT
  flower1,
  flower2,
  CASE
    WHEN
      (flower1 + flower2) % 2 = 1
    THEN
      True
    ELSE
      False
  END
  AS res
FROM love;
