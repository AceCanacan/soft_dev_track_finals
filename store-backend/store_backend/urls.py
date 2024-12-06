from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/admin/')),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('checkout/', views.checkout, name='checkout'),  # Checkout endpoint
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)