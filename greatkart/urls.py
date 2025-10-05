from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.shortcuts import redirect  # Importing redirect

# Define a view for redirect
def redirect_store_html(request):
    return redirect('store')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('store/', include('store.urls')),  # Include the store URLs
    path('store.html', redirect_store_html),  # Redirect /store.html to /store/
    path('cart/',include('carts.urls')),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


