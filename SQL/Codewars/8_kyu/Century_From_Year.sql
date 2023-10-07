SELECT yr, (yr - 1) / 100 + 1 AS century
  FROM years;