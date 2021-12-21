from rest_framework import permissions, viewsets

from past_questions.models import (Course, Department, Faculty, Level,
                                   PastQuestion, Semester, University, Year)
from past_questions.serializers import (CourseSerializer, DepartmentSerializer,
                                        FacultySerializer, LevelSerializer,
                                        PastQuestionSerializer,
                                        SemesterSerializer,
                                        UniversitySerializer, YearSerializer)

class BaseViewSets(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'delete': [permissions.IsAdminUser],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser]}
    
    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class UniversityViewSets(BaseViewSets):
    queryset = University.objects.all()
    serializer_class  = UniversitySerializer
  
class FacultyViewSets(BaseViewSets):
    queryset = Faculty.objects.all()
    serializer_class  = FacultySerializer

class DepartmentViewSets(BaseViewSets):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class YearViewSets(BaseViewSets):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class LevelViewSets(BaseViewSets):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class SemesterViewSets(BaseViewSets):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class CourseViewSets(BaseViewSets):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class PastQuestionViewSets(BaseViewSets):
    queryset = PastQuestion.objects.all()
    serializer_class = PastQuestionSerializer
