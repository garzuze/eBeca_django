from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import frontpage, shop, login, signup
from product.views import product

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="signup"),
    path('shop/', shop, name="shop"),
    path('shop/<slug:slug>/', product, name="product"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
