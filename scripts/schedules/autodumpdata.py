import json
import os
import time
from datetime import datetime

import schedule

with open(r'..\..\secrets.json') as f:
    s = f.read()


d = json.loads(s)
PYTHONPATH_ABS = d['PYTHONPATH_ABS']
REPO_ROOT = d['REPO_ROOT']

def dumpdata_from_DB():
    datenow = datetime.now().strftime("%Y%m%d%H%M")
    backup_cmd = f"{PYTHONPATH_ABS} {REPO_ROOT}\\manage.py dumpdatautf8 --output=dumpdata\db.{datenow}.json"
    print('start...')
    os.system(backup_cmd)


# schedule.every().day.at('09:00').do(dumpdata_from_DB)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

dumpdata_from_DB()