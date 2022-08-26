select id, name, age
FROM users
where age > 30
order by name, age desc;
--

alter table users add column phone varchar(20);

-- REGEX

select name from users where name similar to '%(ma|am)%' limit 100;

