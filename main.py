import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import argparse
from bs4 import BeautifulSoup

def return_adif_string(call,name, gridsqare,mode, rst_sent, rst_rcvd, qso_date,time_on,time_off,band,freq,my_gridsquare,tx_pwr, station_callsign="M/9A3ICE",operator="9A3ICE"):
    adi_log_string = ""
    if call:
        adi_log_string +=f"<call:{len(call)}>{call} "
    if name:
        adi_log_string +=f"<name:{len(name)}>{name} "
    if gridsqare:
        adi_log_string +=f"<gridsquare:{len(gridsqare)}>{gridsqare} "
    if mode:
        if mode == "LSB" or mode == "USB":
            mode = "SSB"

        if mode == "FT4":
            adi_log_string +=f"<mode:4>MFSK <submode:3>FT4 "
        else:
            adi_log_string +=f"<mode:{len(mode)}>{mode} "
    if rst_sent:
        adi_log_string +=f"<rst_sent:{len(rst_sent)}>{rst_sent} "
    if rst_rcvd:
        adi_log_string +=f"<rst_rcvd:{len(rst_rcvd)}>{rst_rcvd} "
    if qso_date:
        qso_date = qso_date.replace("-", "")
        adi_log_string +=f"<qso_date:{len(qso_date)}>{qso_date} "
    if time_on:
        time_on = time_on.replace(":", "")
        adi_log_string +=f"<time_on:{len(time_on)}>{time_on} "
    if time_off:
        time_off = time_off.replace(":", "")
        adi_log_string +=f"<time_off:{len(time_off)}>{time_off} "
    if band:
        adi_log_string +=f"<band:{len(band)}>{band} "
    if freq:
        adi_log_string +=f"<freq:{len(freq)}>{freq} "
    if my_gridsquare:
        adi_log_string +=f"<my_gridsquare:{len(my_gridsquare)}>{my_gridsquare} "
    if tx_pwr:
        adi_log_string +=f"<tx_pwr:{len(tx_pwr)}>{tx_pwr} "
    if station_callsign:
        adi_log_string +=f"<station_callsign:{len(station_callsign)}>{station_callsign} "
    if operator:
        adi_log_string +=f"<operator:{len(operator)}>{operator} "
    adi_log_string += "<eor>"
    return adi_log_string


def html_to_adif(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    rows = soup.find_all('tr', class_='lrow')
    # Exclude rows that have class lrow-nav
    rows = [row for row in rows if 'lrow-nav' not in row['class']]
    logger.info("Found %d rows", len(rows))

    for row in rows:
        call = row.find('td', class_='td_call2 rxData').text.strip()
        name = row.find('td', class_='td_name2 rxData').text.strip()
        gridsquare = row.find('td', class_='td_grid2 rxData').text.strip()
        mode = row.find('td', class_='td_mode2 rxData').text.strip()
        qso_date = row.find('td', class_='td_date').text.strip()
        time_on = row.find('td', class_='td_time').text.strip()
        band = row.find('td', class_='td_band1 rxData').find('span').text.strip()
        freq = row.find('td', class_='td_freq2 txData').text.strip()

        adif_entry = return_adif_string(call=call,name=name, gridsqare=gridsquare,mode=mode, qso_date=qso_date,time_on=time_on,time_off=time_on,band=band,freq=freq, station_callsign="M/9A3ICE",operator="9A3ICE", rst_sent=None, rst_rcvd=None, my_gridsquare=None, tx_pwr=None)
        print(adif_entry)
       

def main():
    parser = argparse.ArgumentParser(description='Convert HTML table to ADIF format')
    parser.add_argument('html_file', help='Path to the HTML file containing the records')
    args = parser.parse_args()

    with open(args.html_file, 'r') as file:
        html_content = file.read()

    html_to_adif(html_content)

if __name__ == '__main__':
    main()
