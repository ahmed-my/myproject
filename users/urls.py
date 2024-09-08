from django.urls import path
from .views import (
    password_reset_request, CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView, CustomPasswordResetDoneView,
    register, email_confirm, login_user, logout_user, resend_password_reset_email,
    portfolio_view, profile_portfolio, upload_image, user_profile,
    UserListView, user_profile_list, profile_detail, edit_profile,
    inbox, message_detail, delete_message, reply_message,
    bulk_delete_messages, chat_message, send_message_form, send_message_ajax,
    delete_chat, folder_detail_view, add_folder, rename_folder, delete_folders,
    delete_image_view, folder_public_view, contact
)

app_name = 'users'

urlpatterns = [
    path('registration', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
