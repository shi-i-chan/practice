SELECT
  month,
  CASE
    WHEN
      month >= 1
      AND month <= 3
      THEN 1
    WHEN
      month >= 4
      AND month <= 6
      THEN 2
    WHEN
      month >= 7
      AND month <= 9
      THEN 3
    WHEN
      month >= 9
      AND month <= 12
      THEN 4
  END
  AS res
FROM quarterof;
