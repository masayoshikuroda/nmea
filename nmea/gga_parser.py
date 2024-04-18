from .util import to_cksum, to_time, to_degree
from .base_parser import BaseParser

class GGAParser(BaseParser):
    def parse_time(self, row):
        if self.parse_mode(row) != 0:
            return to_time(row['COL2'])
        else:
           return super().parse_time(row) 

    def parse_latitude(self, row):
        if self.parse_mode(row) != 0:
            return to_degree(float(row['COL3']), row['COL4'])
        else:
           return super().parse_latitude(row)  
    
    def parse_longitude(self, row):
        if self.parse_mode(row) != 0:
            return to_degree(float(row['COL5']), row['COL6'])
        else:
            return super().parse_longitude(row)
        
    def parse_mode(self, row):
        return int(row['COL7'])

    def parse_satellites(self, row):
        return row['COL8']
    
    def parse_hdop(self, row):
        if self.parse_mode(row) != 0:
            return float(row['COL9'])
        else:
            return super().parse_hdop(row)  
    
    def parse_altitude(self, row):
        if self.parse_mode(row) != 0:
            return float(row['COL10'])
        else:
            return super().parse_altitude(row)  
        
    def parse_geoid(self, row):
        if self.parse_mode(row) != 0:
            return float(row['COL12'])
        else:
            return super().parse_geoid(row)
        
    def parse_age(self, row):
        if self.parse_mode(row) == 2:
            if row['COL14'] !=  '':
                return float(row['COL14'])
        return super().parse_age(row)
    
    def parse_cksum(self, row):
        return to_cksum(row['COL15'])[1]