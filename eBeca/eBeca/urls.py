from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, shop, user_login, signup
from product.views import product

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('signup/', signup, name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'), name="user_login"),
    path('shop/', shop, name="shop"),
    path('shop/<slug:slug>/', product, name="product"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
