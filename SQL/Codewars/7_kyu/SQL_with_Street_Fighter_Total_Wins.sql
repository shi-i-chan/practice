SELECT name, SUM(won) AS won, SUM(lost) AS lost
  FROM fighters
       INNER JOIN winning_moves
       ON fighters.move_id = winning_moves.id
 WHERE winning_moves.move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
 GROUP BY name
 ORDER BY won DESC
 LIMIT 6;