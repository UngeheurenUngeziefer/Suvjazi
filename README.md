### Tasks & Ideas:<br />
- [x] create db saver script
- [x] create table in readme
- [x] create script populating db from saved db 
- [x] space in last_name crush slug fix 
- [x] merge autoscripts & add multifunctional class
- [x] add new person to Suvjazi App page 
- [x] add new company 
- [x] edit button 
- [x] delete button 
- [x] successfully edited message 
- [x] successfully deleted message 
- [x] are you sure for delete 
- [x] select companies when person creating 
- [x] add dates for companies when person creating 
- [x] recreate this as a table or progress list
- [x] draw sitemap
- [x] create plan
- [x] add new companies when person creating (RelatedFieldWidgetWrapper)
- [x] blank=True in url field in Company model
- [x] django-autocomplete-light returned JSON
- [x] back to stable release
- [x] migrate from func-views to class-based-views:
    - [x] view SuvjaziApp (independent)
    - [x] view list of Entities (parent)
    - [x] view list of Persons (child)
    - [x] view list of Institutes (child)
    - [x] view one Person (independent)
    - [x] view one Institute (parent)
    - [x] view one Company (child)
    - [x] add Person (independent)
    - [x] add Institute (parent)
    - [x] add Company (child)
    - [x] edit Person (independent)
    - [x] edit Institute (parent)
    - [x] edit Company (child)
    - [x] delete Entity (parent)
    - [x] delete Person (child)
    - [x] delete Company (child)
    - [x] new views miro mind map 
- [x] implement working models with autocomplete 
- [x] try to compare and find out the way to merge and implement
- [x] implement autocomplete company field in person creation page
- [x] implement new form addition
- [x] working test formset+autocomplete
- [x] implement working models to project
- [x] change minimum input length
--------------------------------------------------------------------------------
- [x] copy working version of nesting formset
- [x] create new model for nested formset
- [x] pass model.id to nested formset
- [x] fix html for nested formset
- [ ] implement select2 for company field in nested formset
- [ ] rename entities to current project
- [ ] merge branches
--------------------------------------------------------------------------------
- [ ] for country field https://evileg.com/ru/post/608/ юзаем ChoiceField
- [ ] check cyrillic slugs, add logic for cyrillic
- [ ] realization of autocomplete in seperate tab
- [ ] dal framework not visible for VSCode pylances
- [ ] fix reverse popup plus button
- [ ] custom form/html for add new company button
- [ ] implement flake8 & black
- [ ] implement mypy
- [ ] CompanyMembership add nice admin panel view
- [ ] edit person page update
- [ ] add more fields to Person & Company obj's
- [ ] add separate folder in templates
- [ ] create hook for tests
- [ ] show statistic for progress log
- [ ] rename stuff
- [ ] frontend 
<br />
### Progress log:

| folder/file | change/progress |
 --- | --- 
| general | start reading Tango with Django |
| general | high-level design for web app created |
| general | start django project |
| suvjazi_app | create frist app for the project |
| urls | create first urls |
| urls | url for about page created |
| templates | templates folder created |
| views | view for project created |
| static | static usage added (test img added) |
| templates | templates usage added |
| templates | first html added |
| media | media usage added (test img added) |
| urls | about moved to general urls |
| templates | about html added |
| models | models for Person and Company created with m-to-m relations |
| models | superuser created, models added to admin panel |
| automation scripts | script for populating db created ver1 (outdated) |
| models | models switched, manyToMany fields logic understandable now |
| automation scripts | switched populating script |
| automation scripts | populating script updated ver2, work fine |
| models | Company field url renamed to company_url |
| admin | Company objects all fields in admin panel |
| admin | Person objects all fields in admin panel |
| tests | tests created |
| admin | nice view for Person and Company in admin panel and console also |
| tests | tests 100% coverage |
| settings | PROJECT_DIR added |
| models | improve models -> create through class for m-t-m relationship |
| automation scripts | start updating population script |
| admin | impove admin -> good looking admin panel as prev ver |
| automation scripts | population script updated ver3, work fine (faker added) |
| tests | tests updated 100% coverage |
| tests | tests updated with fake generator |
| tests | tests cleared & updated |
| models | slug added to Person obj |
| models | slug name resolver added for namesakes |
| html | iteration on Person objs in suvjazi_app html page |
| automation scripts | population script updated |
| admin | prepopulation of slug field logic added |
| models | slug corrected for more than 1, slug for Company obj created |
| automation scripts | save_db to JSON script created |
| tests | tests coverage for slug logic |
| urls | new path to Person obj page |
| views | view updated to show & iterate Person obj's |
| html | person page added, persons are links in suvjazi_app page now |
| automation scripts | population script now can upload info from saved JSON |
| forms | form for Person obj creation added, work fine |
| models | added fix for spaces in first or last name for slug |
| urls | added url for add person |
| views | view for add person |
| html | page for person creation |
| views | add Company same logic as for Person obj's |
| urls | structure of website changed |
| models| models connected more precisely |
| urls | new urls for Company & Person CRUD |
| views | views for Company & Person CRUD |
| html | html's for obj's CRUD |
| html | html's base added, updated |
| js | js added for inline forms and + & - buttons |
| forms | added CompanyMembership form |
| models | one argument name corrected |
| views | updated view add person & many companies only with select from existing for now |
