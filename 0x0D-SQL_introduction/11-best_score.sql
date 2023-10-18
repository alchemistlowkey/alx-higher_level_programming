-- A script that lists all records with highest score of the table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
