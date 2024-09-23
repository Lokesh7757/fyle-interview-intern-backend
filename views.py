from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Assignment, Teacher
from .serializers import AssignmentSerializer, TeacherSerializer

@api_view(['GET'])
def list_principal_assignments(request):
    """List all submitted and graded assignments for the principal"""
    if request.headers.get('X-Principal') and request.headers['X-Principal'].get('principal_id'):
        assignments = Assignment.objects.filter(state__in=['SUBMITTED', 'GRADED'])
        serializer = AssignmentSerializer(assignments, many=True)
        return Response({"data": serializer.data})
    return Response({"error": "Unauthorized"}, status=403)

@api_view(['GET'])
def list_teachers(request):
    """List all teachers for the principal"""
    if request.headers.get('X-Principal') and request.headers['X-Principal'].get('principal_id'):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response({"data": serializer.data})
    return Response({"error": "Unauthorized"}, status=403)

@api_view(['POST'])
def regrade_assignment(request):
    """Principal can re-grade any assignment"""
    if request.headers.get('X-Principal') and request.headers['X-Principal'].get('principal_id'):
        assignment_id = request.data.get('id')
        grade = request.data.get('grade')
        assignment = Assignment.objects.get(id=assignment_id)
        
        if assignment.state == 'GRADED':
            assignment.grade = grade
            assignment.save()
            serializer = AssignmentSerializer(assignment)
            return Response({"data": serializer.data})
        else:
            return Response({"error": "Assignment not graded yet"}, status=400)
    return Response({"error": "Unauthorized"}, status=403)
