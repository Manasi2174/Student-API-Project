from django.shortcuts import render # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404 # type: ignore

# Create your views here.

# Create Student View
class CreateStudent(APIView):
    def post(self,request):
        is_many = isinstance(request.data, list)
        serializer = StudentSerializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# List all students view
class ListStudents(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
# Get student by id
class GetStudentById(APIView):
    def get(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
# Update student
class UpdateStudent(APIView):
    def put(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
# Delete Student
class DeleteStudent(APIView):
    def delete(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        student.delete()
        return Response({"message":"Deleted Successfully"},status=204)
    
# Get student by name
class GetStudentByName(APIView):
    def get(self,request,name):
        students = Student.objects.filter(name=name)
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
# Get students by roll range
class GetByRollRange(APIView):
    def get(self,request,min_roll,max_roll):
        students = Student.objects.filter(roll__gte=min_roll,roll__lte=max_roll)
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
# Get count of total students
class GetTotalCount(APIView):
    def get(self,request):
        count = Student.objects.count()
        return Response({"Total Students": count})
    
# Get student by first letter
class GetByPartial(APIView):
    def get(self,request,query):
        students = Student.objects.filter(name__icontains=query)
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
# Get toppers among all students
class GetToppers(APIView):
    def get(self,request):
        topper = Student.objects.order_by('-marks').first()
        if topper:
            serializer = StudentSerializer(topper)
            return Response(serializer.data)
        return Response({"Message":"No students found"},status=404)