-- Список курсов, которые посещает студент.
SELECT DISTINCT s.student, d.discipline
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
WHERE g.student = 12;