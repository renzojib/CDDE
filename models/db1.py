# -*- coding: utf-8 -*-
db.define_table(
    'states',
    Field('code'),
    Field('state_name'),
    auth.signature,
    format='%(state_name)s'
)

db.define_table(
    'company',
    Field('name'),
    Field('industry'),
    Field('main_location'),
    Field('state_name', 'reference states'),
    Field('website'),
    Field('main_phone_number', requires = IS_MATCH('[\d\-\(\) ]+')),
    Field('sales_rep'),
    Field('linkedin'),
    Field('twitter'),
    Field('facebook'),
    auth.signature,
    format='%(name)s'
)

db.define_table(
    'event_type',
    Field('event_name'),
    Field('description'),
    auth.signature,
    format='%(event_name)s'
)

db.define_table(
    'locations',
    Field('company_id', 'reference company'),
    Field('name', requires=IS_IN_SET(['Headquarter', 'Plant', 'Research facility', 'Bank'])),
    Field('address', 'text'),
    Field('city'),
    Field('state_name', 'reference states'),
    Field('zip_code'),
    Field('main_phone_number', requires = IS_MATCH('[\d\-\(\) ]+')),
    auth.signature,
    format='%(name)s'
)

db.define_table(
   'people_type',
   Field('people_type', requires=IS_IN_SET(['Customer', 'Vendor', 'Consultant', 'Lead'])),
   auth.signature,
   format='%(people_type)s'
   )


db.define_table(
    'people',
    Field('first_name',notnull=True),
    Field('last_name',notnull=True),
    Field('company_id', 'reference company'),
    Field('location_id', 'reference locations'),
    Field('people_type', 'reference people_type'),
    Field('email', requires=IS_EMAIL()),
    Field('phone_number'),
    Field('office_phone'),
    Field('title'),
    Field('role'),
    Field('address',notnull=True),
    Field('linkedin'),
    Field('twitter'),
    Field('facebook'),
    Field('birthday', 'date'),
    auth.signature,
    format='%(first_name)s'
)

db.define_table(
    'events',
    Field('person_id', 'reference people'),
    Field('event_date', 'date'),
    Field('event_time', 'time'),
    Field('event_id', 'reference event_type'),
    Field('status', requires=IS_IN_SET(['Upcoming', 'Completed'])),
    Field('notes'),
    auth.signature
)
