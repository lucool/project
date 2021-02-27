from django.urls import path,include

from cookie_session_app.views.cookie_views import *
from cookie_session_app.views.session_views import *

urlpatterns = [
    path('addcookie/',add_cookie_view),
    path('cookies/',show_cookies_view),
    path('cookie/<name>/',get_cookie_view),
    path('delcookie/<name>/',delete_cookie_view),

    path('addsession/',add_session_view),
    path('session/<name>/',get_session_data),
    path('delsession/<name>/',del_session_data),
    path('flush/',flush_session)
]