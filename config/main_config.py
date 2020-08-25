from os import path
from os.path import dirname
from pathlib import Path
import pathlib

'This file contains configuration details for general use in all files'

PROJECT_HOME = dirname(dirname(path.abspath(__file__)))
# needed path module as fileconfig file use unix parsing for writing log file
LOGGING_PATH = pathlib.PurePosixPath(Path(path.join(PROJECT_HOME, "logs", "run_log.log")))
LOGGING_CONFIG = Path(PROJECT_HOME, "config", "logging", "local.conf")