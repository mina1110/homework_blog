from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.blog),

    path('blog/', include('blogapp.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)