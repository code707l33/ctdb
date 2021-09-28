import csv
import sys
import os


BASE_DIR = os.path.dirname(os.getcwd())
PROJECT_DIR = str(BASE_DIR) + '/CTDB'
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django
django.setup()
from pilotadmin.models import Pilotadmin


data = csv.reader(open(BASE_DIR + "/pilotadmin/dbo.pilot_admin.csv", 'r', encoding="big5"), delimiter=",")
for row in data:
    if row[0] != 'customer_name':
        instance = Pilotadmin()
        instance.customer_name = row[0]
        instance.bg_name = row[1]
        instance.direct_number = row[2]
        instance.adminpassword = row[3]

        print(instance.customer_name)
        instance.save()
