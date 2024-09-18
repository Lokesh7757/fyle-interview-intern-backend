-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS No_of_A_Grades
FROM Assignment
WHERE Teacher = (
    SELECT Teacher
    FROM Assignment
    GROUP BY Teacher
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
AND grade = 'A';
