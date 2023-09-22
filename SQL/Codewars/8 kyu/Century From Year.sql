SELECT
  yr,
  (yr - 1) / 100 + 1 as century
FROM years;
