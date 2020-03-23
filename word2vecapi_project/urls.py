from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

import word2vec_func.views as word2vec_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('word2vec/', include('word2vec_func.urls')),
]