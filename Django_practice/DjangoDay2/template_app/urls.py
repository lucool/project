from django.urls import path

from template_app.views import *

urlpatterns = [
    path('vars/',show_var),
    path('student/<int:score>/',if_view),
    path('for/',for_view),
    path('child/',child_view),
    path('filter/',filter_view),
    path('custom/<int:number>/',custom_filter_view)
]