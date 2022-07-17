import argparse
import sys

from awsgoes16 import __version__
from .commands import COMMANDS
from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16


class CLI:
    def __init__(self):
        self.__run()

    def __run(self):
        self.__api_goes = AwsS3ApiGoes16()
        self.parser = argparse.ArgumentParser(
            prog="apigoes16",
            description="API Wrapper para download dos arquivos do satélite NOAA GOES-16",
            epilog="Desenvolvido por: @anthonyvii27 e @mateusrlopez",
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
                        self.__api_goes.remote_bucket = parser_args.value
                    else:
                        print(self.__api_goes.remote_bucket)

                if parser_args.command == 'local_bucket':
                    if parser_args.value:
                        self.__api_goes.local_bucket = parser_args.value
                    else:
                        print(self.__api_goes.local_bucket)

                if parser_args.command == 'product':
                    if parser_args.value:
                        self.__api_goes.product = parser_args.value
                    else:
                        print(self.__api_goes.product)

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
            )

    def __create_subparsers(self, subparsers):
        for subparser_config in COMMANDS:
            self.__create_subparser(subparsers, subparser_config)