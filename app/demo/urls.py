from django.urls import path, include

import core.urls

urlpatterns = [
    path('', include(core.urls)),
]
