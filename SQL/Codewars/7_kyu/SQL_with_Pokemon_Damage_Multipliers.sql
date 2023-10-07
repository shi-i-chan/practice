SELECT p.pokemon_name, p.str * m.multiplier AS modifiedstrength, m.element 
  FROM pokemon AS p 
       JOIN multipliers AS m 
       ON p.element_id = m.id
 WHERE p.str * m.multiplier >= 40 
 ORDER BY modifiedstrength DESC;