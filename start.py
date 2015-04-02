#!/usr/bin/env python
import json
import os
import re
import signal
import subprocess
import time
import sys
sys.path.insert(0, 'lib')
import buildpackutil
from m2ee import M2EE, logger
import logging

logger.setLevel(logging.INFO)

logger.info('Started Mendix Cloud Foundry Buildpack')

logger.info('scanning for newrelic')
subprocess.call(['find', '/', '-name', 'newrelic'])
logger.info('now scanning /tmp')
subprocess.call(['find', '/tmp'])
