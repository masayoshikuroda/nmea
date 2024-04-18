from .util import to_cksum
from .base_parser import BaseParser

class GSVParser(BaseParser):
    def parse_sv_type(self, row):
        rtype = row['COL1']
        return rtype[2]
    
    def parse_sv_msgs(self, row):
        if (row['COL2'] == 'A'):
            print(row['COL1'], row['COL2'], row['COL3'])
        return int(row['COL2'])
    
    def parse_sv_msg_no(self, row):
        return int(row['COL3'])
    
    def parse_sv_visibles(self, row):
        return to_cksum(row['COL4'])[0]
    
    def parse_cksum(self, row):
        for i in range(24):
            name = 'COL' + str(i+1)
            if '*' in str(row[name]):
                return to_cksum(row[name])[1]
        
        return super().parse_cksum(row)
    
