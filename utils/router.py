import requests
import logging
from requests import auth
from requests.auth import HTTPBasicAuth


__TP_LINK_REBOOT_URL__ = "/userRpm/SysRebootRpm.htm?Reboot=Reboot"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Router:
    def __init__(self, ip: str, user: str, password: str) -> None:
        self.ip = ip
        self.user = user
        self.password = password

    def reboot(self) -> None:
        url = f"http://{self.ip}"
        url_reboot = url + __TP_LINK_REBOOT_URL__
        auth = HTTPBasicAuth(username=self.user, password=self.password)

        try:
            response = requests.get(url, auth=auth, timeout=2)
            if response.status_code == requests.codes.ok:
                response = requests.get(url_reboot, auth=auth)
                if response.status_code != requests.codes.ok:
                    logger.error(
                        f"Error while rebooting the router: {self.ip} with http error: {response.status_code}"
                    )
                else:
                    logger.debug(f"Router: {self.ip} robooted with success.")
            else:
                logger.error(
                    f"Error while connecting to the router: {self.ip} with http error: {response.status_code}"
                )
        except requests.exceptions.ConnectTimeout as cte:
            logger.error(f"Timeout while connection to router: {self.ip}")
        except requests.exceptions.ConnectionError as ce:
            logger.error(f"Unknow error while connection to router: {self.ip}", ce)
