-- Write query to get number of graded assignments for each student:
SELECT Student_id, COUNT(*) AS Number_of_Graded_Assignment
FROM Assignment
GROUP BY Student_id;
