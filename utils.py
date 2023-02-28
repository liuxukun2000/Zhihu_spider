import time
import django
import os, sys
from pathlib import Path

def get_time(fmt:str='%Y-%m-%d %H-%M-%S') -> str:
    '''
    获取当前时间
    '''
    ts = time.time()
    ta = time.localtime(ts)
    t = time.strftime(fmt, ta)
    return t

def init(cwd: str = ""):
    cwd = cwd or str(Path(os.getcwd()))
    sys.path.append(cwd)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "database.settings")
    django.setup()

