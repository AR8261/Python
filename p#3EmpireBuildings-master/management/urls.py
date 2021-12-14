from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("building/list", views.BuildingList.as_view(), name='buildinglist'),
    path("apartment/list", views.ApartmentList.as_view(), name='apartmentlist'),
    path("tenant/list", views.TenantList.as_view(), name='tenantlist'),

    path("building/create", views.BuildingCreate.as_view(), name='buildingcreate'),
    path("apartment/create", views.ApartmentCreate.as_view(), name='apartmentcreate'),
    path("tenant/create", views.TenantCreate.as_view(), name='tenantcreate'),

    path("building/update/<pk>", views.BuildingUpdate.as_view(), name='buildingupdate'),
    path("apartment/update/<pk>", views.ApartmentUpdate.as_view(), name='apartmentupdate'),
    path("tenant/update/<pk>", views.TenantUpdate.as_view(), name='tenantupdate'),


    path("building/delete/<pk>", views.BuildingDelete.as_view(), name='buildingdelete'),
    path("apartment/delete/<pk>", views.ApartmentDelete.as_view(), name='apartmentdelete'),
    path("tenant/delete/<pk>", views.TenantDelete.as_view(), name='tenantdelete'),

 ]