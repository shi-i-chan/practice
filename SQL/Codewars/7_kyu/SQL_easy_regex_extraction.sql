SELECT name, greeting, replace(substring(greeting, '#[\d]+'), '#', '') AS user_id
  FROM greetings;