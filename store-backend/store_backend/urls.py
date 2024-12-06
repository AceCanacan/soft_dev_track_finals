from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('checkout/', views.checkout, name='checkout'),  # user checkout
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)