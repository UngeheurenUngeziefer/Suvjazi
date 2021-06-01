from django.contrib import admin
from suvjazi_app.models import Person, Company, CompanyMembership


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_url', 'employees')

    def employees(self, obj):
        # to show employees per company
        return ', '.join([p.full_name for p in obj.person.all()])


class Person_Admin(admin.ModelAdmin):
    list_display = ('full_name', 'companies')

    def companies(self, obj):
        # to show list of companies per person
        return ', '.join([c.company_name for c in obj.company_set.all()])


admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, Person_Admin)
admin.site.register(CompanyMembership)
