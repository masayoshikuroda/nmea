from .util import to_cksum
from .base_parser import BaseParser

class TXTParser(BaseParser):
    def parse_msg_num(self, row):
        return row['COL2']
    
    def parse_msg_no(self, row):
        return row['COL3']
    
    def parse_msg_type(self, row):
        return row['COL4']
    
    def parse_msg_txt(self, row):
        return to_cksum(row['COL5'])[0]
    
    def parse_cksum(self, row):
        return to_cksum(row['COL5'])[1]