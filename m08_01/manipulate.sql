SELECT id, name as fullname 
FROM contacts
WHERE favorite <> TRUE 
ORDER BY fullname ASC
LIMIT 100;

SELECT name, email
FROM users
WHERE age IN(20, 30, 40)
ORDER BY name;

SELECT name, email
FROM users
WHERE age BETWEEN 20 AND 32
ORDER BY name;


SELECT name, email
FROM contacts
WHERE name LIKE '% L%'
ORDER BY name;

SELECT name, email, age
FROM users
WHERE age NOT BETWEEN 30 AND 40
ORDER BY name;

SELECT COUNT(user_id) as total_contacts, user_id
FROM contacts
GROUP BY user_id;


SELECT id, name
FROM users
WHERE age < 35;

SELECT *
FROM contacts
WHERE user_id IN (SELECT id
    FROM users
    WHERE age < 35);
    
   
SELECT c.id, c.name, c.email, u.name owner
FROM contacts c
INNER JOIN users u ON u.id = c.user_id;

SELECT c.id, c.name, c.email, u.name owner
FROM contacts c
LEFT JOIN users u ON u.id = c.user_id;

UPDATE contacts SET user_id = 3 WHERE id = 5;

SELECT c.id, c.name, c.email, u.name owner
FROM users u
LEFT JOIN contacts c ON u.id = c.user_id;


CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name VARCHAR(255) UNIQUE NOT NULL
);