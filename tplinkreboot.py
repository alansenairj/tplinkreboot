#!/usr/bin/env python3
"""TP Link Rebooter.

Usage:
  tplinkreboot.py (--ip=<ip> --user=<user> --password=<password>) | (--config=<config>)
  tplinkreboot.py -h | --help | --version

  Use --config or --ip --user --password

Options:
  --ip<ip>                  Router ip address
  --user<user>              Router username
  --password<password>      Router password
  --config<config>          Configuration file with ip and credentials
  -h --help                 Show the help
"""
import logging
import os
from typing import Final

from docopt import docopt

from utils import config
from utils.router import Router

__VERSION__ = "1.0.0"

# Logging configuration
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    arguments = docopt(__doc__, version=__VERSION__, help=True)
    # check if has configuration option set
    config_file = arguments.get("--config")
    if config_file:
        ip, user, password = config.get_config_from_file(config_file)
    else:
        ip, user, password = config.get_config_from_args(arguments)

    router = Router(ip=ip, user=user, password=password)
    router.reboot()


if __name__ == "__main__":
    main()
