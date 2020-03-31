# xlogger

A cross-project logger instance for logging across files in a project. Basically a convenience layer on top of Python's `logging` module. 

By importing the logger instance into different files in a project, the logger automatically writes to the same file, and each log line states which file it came from.

Creates a new log file every midnight.

### install:
```bash
pip install git+https://github.com/ks93/xlogger.git
```

### basic use:
```python
# app.py
from xlogger.logger import logger
logger.info('foo') # 2020-03-22 23:12:19,692 - app - INFO - foo
```

```python
# utils.py
from xlogger.logger import logger
logger.info('bar') # 2020-03-22 23:22:11,578 - utils - INFO - bar
```

The `logger` is used exactly like in Python's [`logging`](https://docs.python.org/3.7/library/logging.html) module.

### setup:
Available setups are: log file path, log level for file and log level for console.
Choose one of the follwing log levels (in order): `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

#### ubuntu:
```bash
export LOG_FILE_PATH=/your/logfile/path/
export LOG_LEVEL_FILE={DEBUG/INFO/WARNING/ERROR/CRITICAL}
export LOG_LEVEL_CONSOLE={DEBUG/INFO/WARNING/ERROR/CRITICAL}
```

#### windows:
```cmd
set LOG_FILE_PATH="/your/logfile/path/"
set LOG_LEVEL_FILE={"DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"}
set LOG_LEVEL_CONSOLE={"DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"}
```
