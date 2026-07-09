from django.urls import path
from . import views

urlpatterns = [
    path("", views.MembersView.as_view(), name="miembros"),
    path("miembros/create/", views.MemberCreate.as_view(), name="miembros_create"),
    path("miembros/update/<int:pk>/", views.MemberUpdate.as_view(), name="miembros_update"),
    path("miembros/delete/<int:pk>/", views.MemberDelete.as_view(), name="miembros_delete"),
]