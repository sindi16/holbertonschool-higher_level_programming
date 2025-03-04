-- script to list the number of records
SELECT score, COUNT(name) AS number FROM second_table
GROUP BY score
ORDER BY COUNT(name) DESC;