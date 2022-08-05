import argparse
import os
import sys

from awsgoes16 import __version__
from .commands import COMMANDS
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16


class CLI:
    def __init__(self):
        self.__api_goes = AwsS3ApiGoes16()

        self.__api_goes.local_bucket = os.getenv('AWS_GOES16_CLI_REMOTE_BUCKET', 'noaa-goes16')
        self.__api_goes.local_bucket = os.getenv('AWS_GOES16_CLI_LOCAL_BUCKET', os.getcwd())
        self.__api_goes.product = os.getenv('AWS_GOES16_CLI_PRODUCT', 'GLM-L2-LCFA')
        self.__api_goes.initial_date = os.getenv('AWS_GOES16_CLI_INITIAL_DATE', '')
        self.__api_goes.due_date = os.getenv('AWS_GOES16_CLI_DUE_DATE', '')
        self.__api_goes.data_variable = os.getenv('AWS_GOES16_CLI_DATA_VARIABLE', '')
        self.__api_goes.lat_long_coords = {'n_lat': float(os.getenv('AWS_GOES16_CLI_NORTH_LATITUDE', '')), 's_lat': float(os.getenv('AWS_GOES16_CLI_SOUTH_LATITUDE', '')),'w_lon': float(os.getenv('AWS_GOES16_CLI_WEST_LONGITUDE', '')),'e_lon': float(os.getenv('AWS_GOES16_CLI_EAST_LONGITUDE', ''))}

        self.__run()

    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog="apigoes16",
            description="API Wrapper para download dos arquivos do satélite NOAA GOES-16",
            epilog="Developed by: @anthonyvii27 e @mateusrlopez",
            usage="%(prog)s [options]"
        )

        self.parser.version = __version__
        self.parser.add_argument("-v", "--version", action="version")

        subparsers = self.parser.add_subparsers(help="APIGOES16 Methods", dest="command")
        self.__create_subparsers(subparsers)

        parser_args = self.parser.parse_args()
        if parser_args:
            try:
                if parser_args.command == 'remote_bucket':
                    if parser_args.value:
                        os.environ['AWS_GOES16_CLI_REMOTE_BUCKET'] = parser_args.value
                        self.__api_goes.remote_bucket = parser_args.value
                    else:
                        print(self.__api_goes.remote_bucket)

                if parser_args.command == 'local_bucket':
                    if parser_args.value:
                        os.environ['AWS_GOES16_CLI_LOCAL_BUCKET'] = parser_args.value
                        self.__api_goes.local_bucket = parser_args.value
                    else:
                        print(self.__api_goes.local_bucket)

                if parser_args.command == 'authenticate':
                    self.__api_goes.authenticate(access_key=parser_args.access_key, secret_key=parser_args.secret_key)

                if parser_args.command == 'list_buckets':
                    self.__api_goes.list_buckets()

                if parser_args.command == 'list_bucket_files':
                    self.__api_goes.list_bucket_files(bucket_name=parser_args.bucket_name)

                if parser_args.command == 'product':
                    if parser_args.value:
                        os.environ['AWS_GOES16_CLI_PRODUCT'] = parser_args.value
                        self.__api_goes.product = parser_args.value
                    else:
                        print(self.__api_goes.product)

                if parser_args.command == 'list_products':
                    self.__api_goes.list_products()

                if parser_args.command == 'period':
                    if parser_args.initial_date and parser_args.due_date:
                        os.environ['AWS_GOES16_CLI_INITIAL_DATE'] = f'{parser_args.initial_date} {parser_args.initial_hour or "00"}'
                        self.__api_goes.initial_date = f'{parser_args.initial_date} {parser_args.initial_hour or "00"}'

                        os.environ['AWS_GOES16_CLI_DUE_DATE'] = f'{parser_args.due_date} {parser_args.due_hour or "23"}'
                        self.__api_goes.due_date = f'{parser_args.due_date} {parser_args.due_hour or "23"}'
                    else:
                        print(f'Initial date: {self.__api_goes.initial_date or "NOT DEFINED"}\nDue date: {self.__api_goes.due_date or "NOT DEFINED"}')

                if parser_args.command == 'data_variable':
                    if parser_args.value:
                        os.environ['AWS_GOES16_CLI_DATA_VARIABLE'] = parser_args.value
                        self.__api_goes.product = parser_args.value
                    else:
                        print(self.__api_goes.data_variable)

                if parser_args.command == 'coords':
                    if parser_args.n_lat and parser_args.s_lat and parser_args.w_lon and parser_args.e_lon:
                        os.environ['AWS_GOES16_CLI_NORTH_LATITUDE'] = parser_args.n_lat
                        os.environ['AWS_GOES16_CLI_SOUTH_LATITUDE'] = parser_args.s_lat
                        os.environ['AWS_GOES16_CLI_WEST_LONGITUDE'] = parser_args.w_lon
                        os.environ['AWS_GOES16_CLI_EAST_LONGITUDE'] = parser_args.e_lon
                        self.__api_goes.lat_long_coords = {
                            'n_lat': float(parser_args.n_lat),
                            's_lat': float(parser_args.s_lat),
                            'w_lon': float(parser_args.w_lon),
                            'e_lon': float(parser_args.e_lon)
                        }
                    else:
                        print(self.__api_goes.lat_long_coords)

                if parser_args.command == 'get_file':
                    self.__api_goes.get_file(
                        datetime=f'{parser_args.date} {parser_args.time}',
                        filename=parser_args.filename
                    )

                if parser_args.command == 'get_all_files_one_day':
                    self.__api_goes.get_all_files_one_day(date=parser_args.date, logs=parser_args.logs)

                if parser_args.command == 'incremental_download':
                    self.__api_goes.get_all_files_from_the_last(logs=parser_args.logs)

            except Exception as e:
                print("Invalid argument: {}".format(e))
                sys.exit(1)
        else:
            self.parser.print_help()
            sys.exit(1)

    @staticmethod
    def __create_subparser(subparsers, subparser_config):
        new_parser = subparsers.add_parser(subparser_config['name'], help=subparser_config['help'])
        for argument in subparser_config['arguments']:
            new_parser.add_argument(
                argument['name'],
                argument['alias'],
                help=argument['help'],
                type=argument['type'],
                required=argument['required'],
                default=argument['default'],
            )

    def __create_subparsers(self, subparsers):
        for subparser_config in COMMANDS:
            self.__create_subparser(subparsers, subparser_config)
