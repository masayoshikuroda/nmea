from .util import to_cksum, to_time, to_date, to_datetime, to_degree, to_dir_diff
from .base_parser import BaseParser

class RMCParser(BaseParser):

    def parse_status(self, row):
        return row['COL3']
        
    def parse_time(self, row):
        if self.parse_status(row) == 'A':
            return to_time(row['COL2'])
        else:
            return super().parse_time(row)
  
    def parse_datetime(self, row):
        if self.parse_status(row) == 'A':
            return to_datetime(row['COL10'], row['COL2'])
        
    def parse_latitude(self, row):
        if self.parse_status(row) == 'A':
            return to_degree(float(row['COL4']), row['COL5'])
        else:
            return super().parse_latitude(row)
        
    def parse_longitude(self, row):
        if self.parse_status(row) == 'A':
           return to_degree(float(row['COL6']), row['COL7'])
        else:
           return super().parse_longitude(row) 
     
    def parse_knot(self, row):
        if self.parse_status(row) == 'A':
            return float(row['COL8'])
        else:
            return super().parse_knot(row)

    def parse_true_azimuth(self, row):
        if self.parse_status(row) == 'A':
            return float(row['COL9']) 
        
    def parse_date(self, row):
        if self.parse_status(row) == 'A':
            return to_date(row['COL10'])
        else:
            return super().parse_date(row)
    
    def parse_declination(self, row):
        if self.parse_status(row) == 'A':
            return to_dir_diff(row['COL11'], row['COL12'])
        else:
            return super().parse_declination(row)

    def parse_mode(self, row):
        return to_cksum(row['COL13'])[0]
        
    def parse_cksum(self, row):
        return to_cksum(row['COL13'])[1]    