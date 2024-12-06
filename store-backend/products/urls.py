from django.urls import path
from . import views

urlpatterns = [
    # Login/Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Public-facing / user-facing product views
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Admin CRUD pages
    path('admin_products/', views.product_list_admin, name='product_list_admin'),
    path('admin_products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('admin_products/delete/<int:pk>/', views.product_delete, name='product_delete'),
]