SELECT
  n,
  CASE
    WHEN n > 0
      THEN
        6 * n * n + 2
    ELSE
      1
  END
  AS res
FROM squares;
