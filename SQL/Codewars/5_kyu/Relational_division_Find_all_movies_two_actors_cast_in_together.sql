SELECT title 
  FROM film
       JOIN film_actor AS a USING(film_id)
       JOIN film_actor AS b USING(film_id)
 WHERE a.actor_id = 105 AND b.actor_id = 122
 ORDER BY title;