import math
from datetime import datetime

def to_cksum(s):
    arr = s.split('*')
    if (len(arr)>1):
        return arr[0], arr[1]
    else:
        return arr[0], None

def to_time(value):
   if isinstance(value, float) and math.isnan(value):
       return None
   s = str(value)
   if '.' in s:
        return datetime.strptime(s, '%H%M%S.%f').time()
   else:
        return datetime.strptime(s, '%H%M%S').time()

def to_date(str):
   return datetime.strptime(str, '%d%m%y').date()

def to_datetime(dstr, tstr):
    if '.' in tstr:
        return datetime.strptime(dstr + ' ' + tstr, '%d%m%y %H%M%S.%f')
    else:
        return datetime.strptime(dstr + ' ' + tstr, '%d%m%y %H%M%S')

def to_degree(dms, flag):
    if math.isnan(dms):
        raise ValueError("error!")
    d = math.floor(dms/100) + 100*(dms/100 - math.floor(dms/100))/60
    if flag == 'S' or flag == 'W':
        return -1 * d
    else:
        return d
    
def to_dir_diff(diff, flag):
    if diff == '':
        return None
    
    d = float(diff)
    if flag == 'W':
        return -1 * d
    else:
        return d
