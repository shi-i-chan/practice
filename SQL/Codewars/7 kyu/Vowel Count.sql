SELECT
  str,
  LENGTH(str) - LENGTH(TRANSLATE(str, 'aeiou', ''))
    AS res
FROM getcount;
