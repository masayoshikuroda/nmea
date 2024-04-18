import math
import datetime
from .util import to_cksum, to_time
from .base_parser import BaseParser

class ZDAParser(BaseParser):
    def parse_cksum(self, row):
        return to_cksum(row['COL7'])[1]
    
    def parse_time(self, row):
        return to_time(row['COL2'])

    def parse_date(self, row):
        if isinstance(row['COL3'], float) and math.isnan(row['COL3']):
            return super().parse_datetime(row) 
        return datetime.datetime(int(row['COL5']), int(row['COL4']), int(row['COL3']))
    
    def parse_tz_offset(self, row):
        if isinstance(row['COL3'], float) and math.isnan(row['COL3']):
            return super().parse_tz_offset(row)
        hh = row['COL6']
        if len(hh) == 2:
            hh = '+' + hh
        mm = to_cksum(row['COL7'])[0]
        return hh + ':' + mm

            