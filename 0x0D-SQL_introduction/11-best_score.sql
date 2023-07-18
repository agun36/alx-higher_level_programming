--  lists all records with a score >= 10 in the table
USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
