from django.urls import path
from django.contrib.auth import views

from core.views import frontpage, signup, shop, account, edit_account, about
from product.views import product

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('about/', about, name="about"),
    path('signup/', signup, name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'), name="login"),
    path('account/', account, name='account'),
    path('edit_account/', edit_account, name='edit_account'),
    path('shop/', shop, name="shop"),
    path('shop/<slug:slug>/', product, name="product"),
]