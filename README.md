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

These two calls, also result in a log file, `app.log`:
```
2020-03-22 23:12:19,692 - app - INFO - foo
2020-03-22 23:22:11,578 - utils - INFO - bar
```

Otherwise, `logger` is used exactly like in Python's [`logging`](https://docs.python.org/3.7/library/logging.html) module.

### advanced use:
to change settings like log file location, log levels, etc.:
```python
# app.py
from xlogger.logger import logger
from xlogger.config import config
from xlogger.logger import update_config

logger.info('bar') # logs/app.log: 2020-03-22 23:22:11,578 - utils - INFO - bar
config['handlers']['file']['filename'] = 'logs/new_log_file.txt' # other things can be configured here too.
update_config() # remember to update config fo make new config work.
logger.info('new bar') # logs/new_log_file.txt: 2020-03-22 23:22:11,578 - utils - INFO - new bar
```
