from .base_parser import BaseParser
from .rmc_parser import RMCParser
from .gga_parser import GGAParser
from .zda_parser import ZDAParser
from .vtg_parser import VTGParser
from .gll_parser import GLLParser
from .gsv_parser import GSVParser
from .gsa_parser import GSAParser
from .txt_parser import TXTParser

class Parser:
    base = BaseParser()
    rmc = RMCParser()
    gga = GGAParser()
    zda = ZDAParser()
    vtg = VTGParser()
    gll = GLLParser()
    gsv = GSVParser()
    gsa = GSAParser()
    txt = TXTParser()

    def select(row):
        rtype = row['COL1']
        if rtype == '$GNRMC' or rtype == '$GPRMC':
            return Parser.rmc
        elif rtype == '$GNGGA' or rtype == '$GPGGA':
            return Parser.gga
        elif rtype == '$GNZDA':
            return Parser.zda
        elif rtype == '$GNVTG':
            return Parser.vtg
        elif rtype == '$GNGLL' or rtype == '$GPGLL':
            return Parser.gll
        elif rtype == '$GPGSV' or rtype == '$GLGSV' or rtype == '$GBGSV' or rtype == '$GAGSV' or rtype == '$GQGSV' or rtype =='$BDGSV':
            return Parser.gsv
        elif rtype =='$GPGSA' or rtype == '$BDGSA':
            return Parser.gsa
        elif rtype == '$GPTXT':
            return Parser.txt
        else:
            return Parser.base

    def parse_talker_id(row):
        return row['COL1'][1:2]

    def parse_cksum(row):
        return Parser.select(row).parse_cksum(row)
    
    def parse_status(row):
        return Parser.select(row).parse_status(row)

    def parse_mode(row):
        return Parser.select(row).parse_mode(row)
    
    def parse_time(row):
        return Parser.select(row).parse_time(row)
    
    def parse_date(row):
        return Parser.select(row).parse_date(row)
    
    def parse_datetime(row):
        return Parser.select(row).parse_datetime(row)
    
    def parse_tz_offset(row):
        return Parser.select(row).parse_tz_offset(row)
    
    def parse_latitude(row):
        return Parser.select(row).parse_latitude(row)
    
    def parse_longitude(row):
        return Parser.select(row).parse_longitude(row)
    
    def parse_knot(row):
        return Parser.select(row).parse_knot(row)

    def parse_kmh(row):
        return Parser.select(row).parse_kmh(row)
        
    def parse_true_azimuth(row):
        return Parser.select(row).parse_true_azimuth(row)
    
    def parse_declination(row):
        return Parser.select(row).parse_declination(row)
    
    def parse_satellites(row):
        return Parser.select(row).parse_satellites(row)
    
    def parse_hdop(row):
        return Parser.select(row).parse_hdop(row)
    
    def parse_altitude(row):
        return Parser.select(row).parse_altitude(row)
    
    def parse_geoid(row):
        return Parser.select(row).parse_geoid(row)
    
    def parse_age(row):
        return Parser.select(row).parse_age(row)
    
    def parse_magnetic_azimuth(row):
        return Parser.select(row).parse_magnetic_azimuth(row)
    
    def parse_sv_type(row):
        return Parser.select(row).parse_sv_type(row)
    
    def parse_sv_msgs(row):
        return Parser.select(row).parse_sv_msgs(row)
    
    def parse_sv_msg_no(row):
        return Parser.select(row).parse_sv_msg_no(row)
    
    def parse_sv_visibles(row):
        return Parser.select(row).parse_sv_visibles(row)

    def parse_vdop(row):
        return Parser.select(row).parse_vdop(row)
       
    def parse_pdop(row):
        return Parser.select(row).parse_pdop(row)
    
    def parse_sat_type(row):
        return Parser.select(row).parse_sat_type(row)
    
    def parse_sat_nos(row):
        return Parser.select(row).parse_sat_nos(row)
    
    def parse_msg_num(row):
        return Parser.select(row).parse_msg_num(row)
    
    def parse_msg_no(row):
        return Parser.select(row).parse_msg_no(row)
    
    def parse_msg_type(row):
        return Parser.select(row).parse_msg_type(row)
    
    def parse_msg_txt(row):
        return Parser.select(row).parse_msg_txt(row)