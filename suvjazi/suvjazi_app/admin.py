from django.contrib import admin
from suvjazi_app.models import Person, Company


class Person_Admin(admin.ModelAdmin):
    # to show many person fields in admin panel
    list_display = ('full_name', 'companies')

    def companies(self, obj):
        # to show list of companies of persons in admin panel
        return ', '.join([c.company_name for c in obj.company.all()])

admin.site.register(Person, Person_Admin)


class Company_Admin(admin.ModelAdmin):
    # to show many company fields in admin panel
    list_display = ('company_name', 'company_url', 'employees')

    def employees(self, obj):
        return ', '.join([p.full_name for p in obj.person_set.all()])

admin.site.register(Company, Company_Admin)
