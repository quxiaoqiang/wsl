#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import logging.config
import yaml

def setup_logging02(default_path='logConf.yaml',default_level=logging.INFO,env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    path = default_path
    print path
    value = os.getenv(env_key, None)
    print value
    if value:
        path = value
        print path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
        print config
    else:
        logging.basicConfig(level=default_level)
#LOG_CFG=my_logging.yaml python my_server.py

setup_logging02()

#test