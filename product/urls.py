from django.urls import path
from product import views
app_name = 'product'
urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<int:product_id>/',views.product_detail,name='product_detail'),
    path('new/',views.product_new, name='product_new'),
    path('<int:product_id>/update',views.product_update,name='product_update'),

]