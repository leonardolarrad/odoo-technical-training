from xmlrpc import client

url = 'https://leonardolarrad-odoo-technical-training-academy-7147007.dev.odoo.com'
db = 'leonardolarrad-odoo-technical-training-academy-7147007'
username = 'admin'
password = 'admin'
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# print the version
print('client version:', common.version())

# print user id
uid = common.authenticate(db, username, password, {})
print('user id:', uid)

# call a method
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model_access = models.execute_kw(
    db, uid, password,
    'academy.session', 'check_access_rights',
    ['write'], {'raise_exception': False})

print('academy.session access:', model_access)

courses = models.execute_kw(
    db, uid, password,
    'academy.course', 'search_read',
    [[['level', '=', ['intermediate', 'beginner']]]])

print('courses:', courses)

course = models.execute_kw(
    db, uid, password,
    'academy.course', 'search',
    [[['name', '=', 'Contabilidad']]])


print('course:', course)
