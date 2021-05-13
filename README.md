# TP Link Router Reboot Tool
Tool to reboot TP Link routers.

Project forked from: https://github.com/alansenairj/tplinkreboot

# Usage
```bash
Usage:
  tplinkreboot.py (--ip=<ip> --user=<user> --password=<password>) | (--config=<config>)
  tplinkreboot.py -h | --help | --version

Options:
  --ip<ip>                  Router ip address
  --user<user>              Router username
  --password<password>      Router password
  --config<config>          Configuration file with ip and credentials
  -h --help                 Show the help
```

The router ip address can be specified using a config file in yaml using `--config` or providing ip address, user name and password using `--ip=<ip> --user=<user> --password=<password>`

## Config file sample:
Example file in config/config.yaml

```yaml
---
ip: 192.168.1.1
user: admin
password: admin
```

## Usage example:
> Executing the script directly
```
./tplinkreboot.py --ip=192.168.1.1 --user=admin --password=admin
```

> Executing using python
```
python3 tplinkreboot.py --ip=192.168.1.1 --user=admin --password=admin
```

> Executing using config file
```
python3 tplinkreboot.py --config=config/config.yaml
```
