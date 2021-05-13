import logging
import os
import sys
import yaml

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_config_from_file(config_file: str):
    """
    Recovery router connection properties from config file.

    Args:
        config_file (str): Router configuration properties file in teh format
    Raises:
        FileNotFoundError: If configuration file is not found.

    Returns:
        Tuple[str]: ip, user, password
    """
    if not os.path.exists(config_file):
        logger.error(f"Config file {config_file} not found.")
        sys.exit(-1)
        
    with open(config_file, "r") as fp:
        config = yaml.safe_load(fp)
    
    ip = config.get("ip")
    user = config.get("user")
    password = config.get("password")

    return ip, user, password


def get_config_from_args(arguments: dict):
    """
    Recovery router connection properties from arguments.

    Args:
        arguments (dict): Arguments dictionary form command line

    Returns:
        Tuple[str]: ip, user, password
    """
    ip = arguments.get("--ip")
    user = arguments.get("--user")
    password = arguments.get("--password")

    return ip, user, password
