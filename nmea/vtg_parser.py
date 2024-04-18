from .util import to_cksum
from .base_parser import BaseParser

class VTGParser(BaseParser):
    def parse_true_azimuth(self, row):
        if self.parse_mode(row) != 'M':
            return float(row['COL2'])
        else:
            return super().parse_true_azimuth(row)

    def parse_magnetic_azimuth(self, row):
        if row['COL4'] != '':
            return float(row['COL4'])
        else:
            return super().parse_magnetic_azimuth(row)

    def parse_mode(self, row):
        return row['COL10']
    
    def parse_knot(self, row):
        if self.parse_mode(row) != 'M':
            return float(row['COL6'])
        else:
            return super().parse_knot(row)
        
    def parse_kmh(self, row):
        if self.parse_mode(row) != 'M':
            return float(row['COL8'])
        else:
            return super().parse_kmh(row)
        
    def parse_mode(self, row):
        return to_cksum(row['COL10'])[0]
    
    def parse_cksum(self, row):
        return to_cksum(row['COL10'])[1]