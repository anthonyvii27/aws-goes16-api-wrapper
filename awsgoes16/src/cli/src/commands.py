COMMANDS = [
    {
        'name': 'remote_bucket',
        'help': 'Setar o remote bucket ao qual desejas trabalhar no futuro',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Nome referente ao remote bucket',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'local_bucket',
        'help': 'Setar o local bucket ao qual desejas trabalhar no futuro',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Nome referente ao local bucket',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'authenticate',
        'help': 'Responsável por realizar a autenticação do usuário. OBS.: Para acesso aos repositório do NOAA GOES16 '
                'não é necessário realizar autenticação',
        'arguments': [
            {
                'name': '--access_key',
                'alias': '-ak',
                'help': 'AWS Access Key',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--secret_key',
                'alias': '-sk',
                'help': 'AWS Secret Key',
                'type': str,
                'required': True,
                'default': '',
            },
        ]
    },
    {
        'name': 'list_buckets',
        'help': 'Listagem dos buckets',
        'arguments': []
    },
    {
        'name': 'list_bucket_files',
        'help': 'Listagem dos arquivos presentes no bucket informado',
        'arguments': [
            {
                'name': '--bucket_name',
                'alias': '-bn',
                'help': 'Nome do bucket ao qual será feito a listagem',
                'type': str,
                'required': True,
                'default': '',
            }
        ]
    },
    {
        'name': 'list_products',
        'help': 'Listagem dos produtos do NOAA GOES16 permitidos',
        'arguments': []
    },
    {
        'name': 'get_file',
        'help': 'Responsável por fazer o download do arquivo especificado',
        'arguments': [
            {
                'name': '--filename',
                'alias': '-fn',
                'help': 'Nome do arquivo',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--date',
                'alias': '-d',
                'help': 'Data no formato yyyy-mm-dd',
                'type': str,
                'required': True,
                'default': '',
            },
{
                'name': '--time',
                'alias': '-t',
                'help': 'Valor referente à hora do dia com valor entre 00 e 23',
                'type': int,
                'required': True,
                'default': '',
            }
        ]
    },
    {
        'name': 'get_all_files_one_day',
        'help': 'Realiza o download de todos os arquivos do dia informado',
        'arguments': [
            {
                'name': '--date',
                'alias': '-d',
                'help': 'Data no formato yyyy-mm-dd',
                'type': str,
                'required': True,
                'default': '',
            },
            {
                'name': '--logs',
                'alias': '-l',
                'help': 'Caso True, apresenta os logs no momento do download. Default: True',
                'type': bool,
                'required': False,
                'default': True,
            }
        ]
    },
    {
        'name': 'product',
        'help': 'Responsável por setar o valor de produto',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Nome do produto',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'period',
        'help': 'Responsável por setar as datas/horas de início e fim para utilizar em downloads futuros',
        'arguments': [
            {
                'name': '--initial_date',
                'alias': '-id',
                'help': 'Data de início no formato yyyy-mm-dd',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--initial_hour',
                'alias': '-ih',
                'help': 'Valor referente à hora do dia com valor entre 00 e 23',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--due_date',
                'alias': '-dd',
                'help': 'Data de término no formato yyyy-mm-dd',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--due_hour',
                'alias': '-dh',
                'help': 'Valor referente à hora do dia com valor entre 00 e 23',
                'type': str,
                'required': False,
                'default': '',
            },
        ]
    },
    {
        'name': 'data_variable',
        'help': 'netCDN Variable para filtragem. Default: event-energy',
        'arguments': [
            {
                'name': '--value',
                'alias': '-v',
                'help': 'Variável de dados',
                'type': str,
                'required': False,
                'default': '',
            }
        ]
    },
    {
        'name': 'coords',
        'help': 'Responsável por setar as coordenadas para filtragem',
        'arguments': [
            {
                'name': '--n_lat',
                'alias': '-nl',
                'help': 'North Latitude',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--s_lat',
                'alias': '-sl',
                'help': 'South Latitude',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--w_lon',
                'alias': '-wl',
                'help': 'West Longitude',
                'type': str,
                'required': False,
                'default': '',
            },
            {
                'name': '--e_lon',
                'alias': '-el',
                'help': 'East Longitude',
                'type': str,
                'required': False,
                'default': '',
            },
        ]
    },
    {
        'name': 'incremental_download',
        'help': 'Responsável por realizar o download incremental dos arquivos a partir do arquivo mais recente '
                'presente no local bucket',
        'arguments': [
            {
                'name': '--logs',
                'alias': '-l',
                'help': 'Caso True, apresenta os logs no momento do download. Default: True',
                'type': bool,
                'required': False,
                'default': True,
            }
        ]
    },
]
