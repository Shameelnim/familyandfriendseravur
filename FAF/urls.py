from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
	path('course',views.course,name="course"),
	 path('join', views.register_student, name='register_student'),
	 path('about',views.about,name="about")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
