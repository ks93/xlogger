# xlogger

a cross-project logger instance for logging across files in a project | creating a new file every midnight
### install:
```bash
pip install git+https://github.com/ks93/xlogger.git
```

### use:
```python
from xlogger.logger import logger
logger.info('foo')
```

### setup:
available setups are: log file path, log level for file and log level for console.
choose one of the follwing log levels (in order): `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

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
