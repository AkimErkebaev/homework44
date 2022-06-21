from django.urls import path

from webapp.views import index_view, create_solution

urlpatterns = [
    path("", index_view),
    path("solution/", create_solution),
]
