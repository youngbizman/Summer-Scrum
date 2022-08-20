from django.contrib import admin
from django.urls import path

from core.views import user
from core.views import content

urlpatterns = [
    path('admin/', admin.site.urls),

    # User API
    path('user/register/', user.RegisterView.as_view()),
    path('user/login/', user.LoginView.as_view()),
    path('user/list/', user.ListView.as_view()),

    # Content API
    path('content/create/', content.CreateView.as_view()),
    path('content/retrieve/<pk>', content.RetrieveView.as_view()),
    path('content/list/', content.ListView.as_view()),
]
