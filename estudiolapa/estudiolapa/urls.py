from django.contrib import admin
from django.urls import path
from home.views import home
# import home, blog

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    # path('blog/', blog.urls),
]
