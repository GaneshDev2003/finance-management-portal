"""finance_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.user_auth.views import (
    home_view,
    logout_view,
    sign_up_view,
    login_view,
)
from django.conf import settings
from django.conf.urls.static import static

from apps.bank_account.views import(
    account_detail_view,
    account_view,
    account_add_view,
    transaction_add_view,
    transaction_delete_view,
    transaction_list_view,
    transaction_update_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view , name="home"),
    path('signup/', sign_up_view, name = 'signup'),
    path('login/' , login_view, name = 'login'),
    path('accounts/' , account_view , name = 'accounts'),
    path('logout/', logout_view, name  = 'logout'),
    path('add_account/', account_add_view, name = 'add_account'),
    path('account_details/<account_id>',account_detail_view, name = 'account_details'),
    path('account_details/<account_id>/add_transaction', transaction_add_view, name ='add_transaction'),
    path('account_details/<account_id>/transaction_list/page', transaction_list_view, name = "transaction_list"),
    path('account_details/<account_id>/transaction/<transaction_id>/delete_transaction', transaction_delete_view, name = "delete_transaction"),
    path('account_details/<account_id>transaction/<transaction_id>/update_transaction', transaction_update_view, name = "update_transaction")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

