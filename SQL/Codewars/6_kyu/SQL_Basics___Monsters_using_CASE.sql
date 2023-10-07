SELECT t.id AS id, t.heads AS heads, t.arms AS arms,
       b.legs AS legs, b.tails AS tails,
  CASE
  WHEN heads > arms
    OR tails > legs THEN 'BEAST'
  ELSE 'WEIRDO'
   END AS species
  FROM top_half AS t, bottom_half AS b
 WHERE t.id = b.id
 ORDER BY species;