
import pandas as pd
from .parser import Parser

def read_nmea(name):
    names = []
    for i in range(24):
        names.append('COL' + str(i+1))

    nmeaDF = pd.read_csv(name, header=None, names=names, comment='#',dtype='object')
        

    # skip comment line
    meaDF = nmeaDF.query("not COL1.str.contains('^.+program.+$', regex=True)")

    nmeaDF['talker_id']   = nmeaDF.apply(Parser.parse_talker_id,    axis=1)
    nmeaDF['cksum']       = nmeaDF.apply(Parser.parse_cksum,        axis=1)

    nmeaDF['status']      = nmeaDF.apply(Parser.parse_status,       axis=1)
    nmeaDF['mode']        = nmeaDF.apply(Parser.parse_mode,         axis=1)
    nmeaDF['time']        = nmeaDF.apply(Parser.parse_time,         axis=1)
    nmeaDF['date']        = nmeaDF.apply(Parser.parse_date,         axis=1)
    nmeaDF['datetime']    = nmeaDF.apply(Parser.parse_datetime,     axis=1)
    nmeaDF['tz_offset']   = nmeaDF.apply(Parser.parse_tz_offset,    axis=1)

    nmeaDF['latitude']    = nmeaDF.apply(Parser.parse_latitude,     axis=1)
    nmeaDF['longitude']   = nmeaDF.apply(Parser.parse_longitude,    axis=1)

    nmeaDF['knot']        = nmeaDF.apply(Parser.parse_knot,         axis=1)
    nmeaDF['kmh']         = nmeaDF.apply(Parser.parse_kmh,          axis=1)

    nmeaDF['satellites']  = nmeaDF.apply(Parser.parse_satellites,   axis=1)
    nmeaDF['hdop']        = nmeaDF.apply(Parser.parse_hdop,         axis=1)

    nmeaDF['altitude']    = nmeaDF.apply(Parser.parse_altitude,     axis=1)
    nmeaDF['geoid']       = nmeaDF.apply(Parser.parse_geoid,        axis=1)
    nmeaDF['age']         = nmeaDF.apply(Parser.parse_age,          axis=1)

    nmeaDF['true_azimuth']         = nmeaDF.apply(Parser.parse_true_azimuth,      axis=1)
    nmeaDF['magnetic_azimuth']     = nmeaDF.apply(Parser.parse_magnetic_azimuth,  axis=1)
    nmeaDF['magnetic_declination'] = nmeaDF.apply(Parser.parse_declination,       axis=1)

    nmeaDF['sv_type']     = nmeaDF.apply(Parser.parse_sv_type,      axis=1)
    nmeaDF['sv_msgs']     = nmeaDF.apply(Parser.parse_sv_msgs,      axis=1)
    nmeaDF['sv_msg_no']   = nmeaDF.apply(Parser.parse_sv_msg_no,    axis=1)
    nmeaDF['sv_vlsibles'] = nmeaDF.apply(Parser.parse_sv_visibles,  axis=1)

    nmeaDF['pdop']        = nmeaDF.apply(Parser.parse_pdop,         axis=1)
    nmeaDF['vdop']        = nmeaDF.apply(Parser.parse_vdop,         axis=1)
    nmeaDF['sat_type']    = nmeaDF.apply(Parser.parse_sat_type,     axis=1)
    nmeaDF['sat_nos']     = nmeaDF.apply(Parser.parse_sat_nos,      axis=1)

    nmeaDF['msg_num']     = nmeaDF.apply(Parser.parse_msg_num,      axis=1)
    nmeaDF['msg_no']      = nmeaDF.apply(Parser.parse_msg_no,       axis=1)
    nmeaDF['msg_type']    = nmeaDF.apply(Parser.parse_msg_type,     axis=1)
    nmeaDF['msg_txt']     = nmeaDF.apply(Parser.parse_msg_txt,      axis=1)

    return nmeaDF

if __name__ == '__main__':
    df = read_nmea('gps.txt')
    print(df)