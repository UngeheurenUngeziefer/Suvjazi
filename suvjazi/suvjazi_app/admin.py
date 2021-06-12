from django.contrib import admin
from suvjazi_app.models import Person, Company, CompanyMembership


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'slug', 'company_url', 'all_time_employees')
    prepopulated_fields = {'slug':('company_name', )}

    def all_time_employees(self, obj):
        # to show employees per company
        return ', '.join([p.full_name for p in obj.person.all()])


class Person_Admin(admin.ModelAdmin):
    list_display = ('full_name', 'slug', 'companies')
    prepopulated_fields = {'slug':('first_name', 'last_name')}

    def companies(self, obj):
        # to show list of companies per person
        return ', '.join([c.company_name for c in obj.company.all()])


admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, Person_Admin)
admin.site.register(CompanyMembership)
