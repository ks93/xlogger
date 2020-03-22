# xlogger

a cross-project logger instance
## Install:
```bash
pip install git+https://github.com/ks93/xlogger.git
```

## Use:
```python
from xlogger.logger import logger
logger.info('foo')
```

## Setup:
### Ubuntu:
```bash
export LOG_FILE_PATH=/your/logfile/path/
export LOG_LEVEL_FILE={DEBUG/INFO/WARNING/ERROR/CRITICAL}
export LOG_LEVEL_CONSOLE={DEBUG/INFO/WARNING/ERROR/CRITICAL}
```

### Windows:
```cmd
set LOG_FILE_PATH="/your/logfile/path/"
set LOG_LEVEL_FILE={"DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"}
set LOG_LEVEL_CONSOLE={"DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"}
```
