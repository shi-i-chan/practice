SELECT n,
  CASE
  WHEN n = 0 THEN n
  ELSE CAST(CEIL((1 + SQRT(8 * n + 1)) / 2) AS int)
   END
    AS res
  FROM participants;