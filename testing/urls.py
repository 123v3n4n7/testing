from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from test_app.views import ListOfQuestionsView

router = SimpleRouter()
router.register(r'api/get_tests', ListOfQuestionsView, basename='tests')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('test_app.urls')),
]
urlpatterns += router.urls
