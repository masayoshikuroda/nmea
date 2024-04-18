from .util import to_cksum, to_time, to_degree
from .base_parser import BaseParser

class GLLParser(BaseParser):
    def parse_latitude(self, row):
        if self.parse_status(row) != 'V':
            return to_degree(float(row['COL2']), row['COL3'])
        else:
            return super().parse_latitude(row)
        
    def parse_longitude(self, row):
        if self.parse_status(row) != 'V':
           return to_degree(float(row['COL4']), row['COL5'])
        else:
           return super().parse_longitude(row) 
     
    def parse_time(self, row):
        if self.parse_status(row) != 'V':
            return to_time(row['COL6'])
        else:
            return super().parse_time(row)
        
    def parse_status(self, row):
        return row['COL7']
    
    def parse_mode(self, row):
        return to_cksum(row['COL8'])[0]
    
    def parse_cksum(self, row):
        return to_cksum(row['COL8'])[1]