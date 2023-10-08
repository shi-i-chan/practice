INSERT INTO author (name_author)
SELECT author AS name_author
  FROM autho 
       RIGHT JOIN supply
       ON author.name_author = supply.author
 WHERE name_author IS NULL;