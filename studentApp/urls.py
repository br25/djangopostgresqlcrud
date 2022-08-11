from django.urls import include, path
from .views import StudentCreate, StudentList, StudentDetail, StudentUpdate, StudentDelete


urlpatterns = [
    path('create/', StudentCreate.as_view(), name='create-student'),
    path('list/', StudentList.as_view()),
    path('<int:pk>/', StudentDetail.as_view(), name='retrieve-student'),
    path('update/<int:pk>/', StudentUpdate.as_view(), name='update-student'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]