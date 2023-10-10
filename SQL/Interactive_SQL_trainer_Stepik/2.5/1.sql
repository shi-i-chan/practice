INSERT INTO client(name_client, email, city_id)
SELECT 'Попов Илья', 'popov@test', city_id
  FROM city
 WHERE name_city = 'Москва';

-- OR

INSERT INTO client(name_client, email, city_id)
VALUES ('Попов Илья', 'popov@test', (SELECT city_id
                                       FROM city
                                      WHERE name_city = 'Москва'));