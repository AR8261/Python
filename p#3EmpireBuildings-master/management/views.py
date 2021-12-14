from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from management.forms import BuildingCreateForm, ApartmentCreateForm, TenantCreateForm, BuildingUpdateForm, \
    ApartmentUpdateForm, TenantUpdateForm
from management.models import Building, Apartment, Tenant


def home(request):
    return render(request, 'management/home.html')



# ********Building*******************
class BuildingList(ListView):
    model = Building
    template_name = "management/building_list.html"



class BuildingCreate(CreateView):
    model = Building
    template_name = "management/building_create_form.html"
    form_class=BuildingCreateForm


    def get_success_url(self):
        return reverse('buildingcreate')



class BuildingUpdate(UpdateView):
    model = Building
    template_name = "management/building_update_form.html"
    form_class = BuildingUpdateForm

    def get_success_url(self):
        return reverse('buildinglist')

#
class BuildingDelete(DeleteView):
    model = Building
    template_name = "management/building_delete_form.html"

    def get_success_url(self):
        return reverse('buildinglist')
# ********Apartment******************
class ApartmentList(ListView):
    model=Apartment
    template_name = "management/apartment_list.html"


class ApartmentCreate(CreateView):
    model = Apartment
    template_name = "management/apartment_create_form.html"
    form_class=ApartmentCreateForm

    def get_success_url(self):
        return reverse('apartmentcreate')


class ApartmentUpdate(UpdateView):
    model = Apartment
    template_name = "management/apartment_update_form.html"
    form_class=ApartmentUpdateForm

    def get_success_url(self):
        return reverse('apartmentlist')

class ApartmentDelete(DeleteView):
    model = Apartment
    template_name = "management/apartment_delete_form.html"

    def get_success_url(self):
        return reverse('apartmentlist')

# ********Tenant*******************
class TenantList(ListView):
    model=Tenant
    template_name = "management/tenant_list.html"

class TenantCreate(CreateView):
    model = Tenant
    template_name = "management/tenant_create_form.html"
    form_class=TenantCreateForm
    def get_success_url(self):
        return reverse('tenantcreate')

class TenantUpdate(UpdateView):
    model = Tenant
    template_name = "management/tenant_update_form.html"
    form_class=TenantUpdateForm
    def get_success_url(self):
        return reverse('tenantlist')

class TenantDelete(DeleteView):
    model = Tenant
    template_name = "management/tenant_delete_form.html"

    def get_success_url(self):
        return reverse('tenantlist')