from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .auth import userLogin, userLogout
from .views import UserListCreate, UserRUD, HackathonList, HackathonDetail, TeamListCreate, TeamRUD, SkillList

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='UserListCreate'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('users/<int:pk>/', UserRUD.as_view(), name='UserRUD'),
    
    path('hackathons/', HackathonList.as_view(), name='HackathonList'),
    path('hackathons/<int:pk>/', HackathonDetail.as_view(), name='HackathonDetail'),
   
    path('teams/', TeamListCreate.as_view(), name='TeamListCreate'),
    path('teams/<int:pk>', TeamRUD.as_view(), name='TeamRUD'),
   
    path('skills/', SkillList.as_view(), name='SkillList')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)