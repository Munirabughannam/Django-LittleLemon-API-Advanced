from django.urls import path
from . import views


urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view()),
    path('groups/manager/users/', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk>/', views.ManagerSingleUserView.as_view()),
    path('groups/delivery-crew/users/', views.Delivery_crew_management.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', views.Delivery_crew_management_single_view.as_view()),
    path('cart/menu-items/', views.Customer_Cart.as_view()),
    path('orders/', views.Orders_view.as_view()),
    path('orders/<int:pk>/', views.Single_Order_view.as_view()),

]
