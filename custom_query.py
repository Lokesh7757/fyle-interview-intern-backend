from django.db import connection

# For counting assignments with grade 'A' per teacher
def count_grade_A_assignments_by_teacher_with_max_grading():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT teacher_id, COUNT(*) AS A_count
            FROM assignment
            WHERE grade = 'A'
            GROUP BY teacher_id
            ORDER BY A_count DESC
            LIMIT 1;
        """)
        result = cursor.fetchone()
    return result


# For counting graded assignments per student
def number_of_graded_assignments_for_each_student():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT student_id, COUNT(*) AS graded_assignments
            FROM assignment
            WHERE state = 'GRADED'
            GROUP BY student_id;
        """)
        result = cursor.fetchall()
    return result
