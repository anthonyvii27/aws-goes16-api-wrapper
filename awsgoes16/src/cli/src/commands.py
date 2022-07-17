COMMANDS = [
    {
        'name': 'remote_bucket',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'local_bucket',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'authenticate',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--access_key',
                'alias': '-ak',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--secret_key',
                'alias': '-sk',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            },
        ]
    },
    {
        'name': 'list_buckets',
        'help': 'Lorem ipsum...',
        'arguments': []
    },
    {
        'name': 'list_bucket_files',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--bucket_name',
                'alias': '-bn',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            }
        ]
    },
    {
        'name': 'list_products',
        'help': 'Lorem ipsum...',
        'arguments': []
    },
    {
        'name': 'get_file',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--filename',
                'alias': '-fn',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--datetime',
                'alias': '-dt',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            }
        ]
    },
    {
        'name': 'get_all_files_one_day',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--date',
                'alias': '-dt',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--logs',
                'alias': '-l',
                'help': 'Lorem ipsum...',
                'type': bool,
                'required': False,
                'default': True,
            }
        ]
    },
    {
        'name': 'product',
        'help': 'Lorem ipsum...',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Lorem ipsum...',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
]
