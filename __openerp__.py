{
    'name': 'Fnx Customer Portal',
    'version': '0.1',
    'category': 'Generic Modules',
    'description': """\
            Phoenix Portal for customers.

        Allows entering orders on-line instead of through hand-held
        devices.
            """,
    'author': 'Ethan Furman',
    'maintainer': 'Ethan Furman',
    'website': '',
    'depends': [
        'base',
        'fis_integration',
	'fnx_sr',
        'mail',
	'portal',
	'sample',
        'web',
        ],
    'js': [
        ],
    'css':[
        ],
    'data': [
        'order_entry_view.xaml',
	'res_partner_view.xaml',
	'security/fnx_customer_portal_security.xaml',
	'security/ir.model.access.csv',
        ],
    'test': [],
    'installable': True,
    'active': False,
}

