# Write your MySQL query statement below
SELECT a.id FROM Weather a
WHERE a.temperature > (SELECT temperature FROM Weather WHERE (a.recordDate-INTERVAL 1 DAY) = recordDate);