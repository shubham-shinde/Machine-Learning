from faker import Faker
import sys
from babel.dates import format_date
import random
import pandas as pd
sys.version

fake = Faker()

dt = fake.date_object()
dt

FORMATS = ['short',
           'medium',
           'long',
           'full',
           'full',
           'full',
           'full',
           'full',
           'full',
           'full',
           'full',
           'full',
           'full',
           'd MMM YYY', 
           'd MMMM YYY',
           'dd MMM YYY',
           'd MMM, YYY',
           'd MMMM, YYY',
           'dd, MMM YYY',
           'd MM YY',
           'd MMMM YYY',
           'MMMM d YYY',
           'MMMM d, YYY',
           'dd.MM.YY']

format_date(dt, format=FORMATS[random.randint(0, len(FORMATS)-1)], locale='en_US').replace(',', '')


dt.isoformat()


def load_data(m=10000):
    data_set = pd.DataFrame({ 'humanized': [], 'machine': []})
    for i in range(m):
        dt = fake.date_object() 
        humanized_date = format_date(dt, format=FORMATS[random.randint(0, len(FORMATS)-1)], locale='en_US').replace(',', '')
        machine_date = dt.isoformat()
        data_set = data_set.append({'humanized': humanized_date, 'machine': machine_date}, ignore_index=True)
    return data_set
data_set = load_data()

data_set.to_csv('./data_set.csv')


