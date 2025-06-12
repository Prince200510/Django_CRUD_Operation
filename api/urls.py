from django.urls import path
from .views import get_user, create_user, user_details
from .views_APIView import UserAPIView, UserOperation
from .view_generics import UserGenerics, UserDetails

urlpatterns = [
    path('users/', get_user, name = 'get_user'),
    # path('users/create/', create_user, name = 'create_user'),
    # path('users/<int:pk>', user_details, name = 'user_details')
    # path('users/<int:pk>', UserAPIView.as_view(), name = 'user_view'),
    # path('users/operation/<int:pk>', UserOperation.as_view(), name = 'user_operation')
    path('users/<int:pk>', UserDetails.as_view(), name = 'user_view'),
    path('users/operation/<int:pk>', UserDetails.as_view(), name = 'user_operation')
]
