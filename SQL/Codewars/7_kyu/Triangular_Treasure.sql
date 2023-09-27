SELECT
  n,
  CASE
    WHEN
      n < 0
    THEN
      0
    ELSE
      n * (n + 1) / 2
  END
    AS res
FROM triangular;
