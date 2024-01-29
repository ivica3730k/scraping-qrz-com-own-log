import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import argparse
from bs4 import BeautifulSoup

def html_to_adif(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    adi_log_string = ""

    rows = soup.find_all('tr', class_='lrow')
    # exculde rows that have class lrow-nav
    rows = [row for row in rows if 'lrow-nav' not in row['class']]
    logger.info("Found %d rows", len(rows))
    for row in rows:
        print(row)
        date = row.find('td', class_='td_date').text.strip()
        time = row.find('td', class_='td_time').text.strip()
        callsign_theirs = row.find('td', class_='td_call2').text.strip()
        band = row.find('td', class_='td_band1').find('span').text.strip()
        print(date)
        print(time)
        print(callsign_theirs)
        print(band)
        break
        
       

def main():
    parser = argparse.ArgumentParser(description='Convert HTML table to ADIF format')
    parser.add_argument('html_file', help='Path to the HTML file containing the records')
    args = parser.parse_args()

    with open(args.html_file, 'r') as file:
        html_content = file.read()

    html_to_adif(html_content)

if __name__ == '__main__':
    main()
