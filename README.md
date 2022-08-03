# FEAPDER Chinese log display to English
拷贝 cn2en 到 feapder 项目目录

在启动文件里开启以下代码可用把常见中文 console 转成英文输出，目前 log 还不能翻译.

```
from loguru import logger
logger.remove()
logger.add(sys.stderr, format=cn2en.formatter)
```