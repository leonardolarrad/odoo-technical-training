from xmlrpc import client

url = 'https://leonardolarrad-odoo-technical-training-academy-7147007.dev.odoo.com'
db = 'leonardolarrad-odoo-technical-training-academy-7147007'
username = 'admin'
password = 'admin'
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# print the version
print(common.version())