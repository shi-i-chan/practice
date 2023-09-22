SELECT
  str,
  CASE
    WHEN
      LOWER(str) = LOWER(REVERSE(str))
    THEN
      True
    ELSE
      False
  END
  AS res
FROM ispalindrome;
