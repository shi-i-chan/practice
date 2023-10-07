SELECT bool,
  CASE
  WHEN bool = True
  THEN 'Yes'
  ELSE 'No'
   END
    AS res
  FROM booltoword;