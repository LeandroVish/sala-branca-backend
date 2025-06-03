from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignUpView, LogoutView, UserDetailView

urlpatterns = [
    # signup
    path('signup/', SignUpView.as_view(), name='signup'),

    # login (token obtain)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh do access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # logout (endpoint customizado; atualmente só retorna 204)
    path('logout/', LogoutView.as_view(), name='logout'),

    # detalhes do usuário logado (GET /api/auth/me/)
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
