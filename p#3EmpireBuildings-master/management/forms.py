from django.forms import forms,ModelForm

from management.models import Building, Apartment, Tenant


class BuildingCreateForm(ModelForm):
    class Meta:
        model=Building
        fields = ("number", "street")


class BuildingUpdateForm(ModelForm):
    class Meta:
        model=Building
        fields = ("number", "street")


class ApartmentCreateForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ("number", "monthly_rent","building")

class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ("number", "monthly_rent","building")

class TenantCreateForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ("first_name", "last_name", "age", "gender","apartment")


class TenantUpdateForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ("first_name", "last_name", "age", "gender","apartment")


