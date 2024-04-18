from .util import to_cksum
from .base_parser import BaseParser

class GSAParser(BaseParser):
    def parse_mode(self, row):
        return row['COL2']
    
    def parse_status(self, row):
        return row['COL3']

    def parse_sat_nos(self, row):
        sat_nos = []
        for i in range(12):
            name = 'COL' + str(i + 4)
            if row[name] != '':
                sat_nos.append(row[name])
        return sat_nos
    
    def parse_pdop(self, row):
        return float(row['COL16'])
    
    def parse_hdop(self, row):
        return float(row['COL17'])
        
    def parse_vdop(self, row):
        return to_cksum(row['COL18'])[0]

    def parse_sat_type(self, row):
        return None

    def parse_cksum(self, row):
        return to_cksum(row['COL18'])[1]