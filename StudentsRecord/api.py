from rest_framework import routers
from StudentInfo import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'course', myapp_views.CourseViewset)
router.register(r'test', myapp_views.TestViewset)
router.register(r'club', myapp_views.ClubViewset)
router.register(r'section', myapp_views.SectionViewset)
router.register(r'student', myapp_views.StudentViewset)