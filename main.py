import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import argparse
from bs4 import BeautifulSoup

def html_to_adif(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    adi_log_string = ""

    rows = soup.find_all('tr', class_='lrow')
    logger.info("Found %d rows", len(rows))
    for row in rows:
        pass
        
       

def main():
    parser = argparse.ArgumentParser(description='Convert HTML table to ADIF format')
    parser.add_argument('html_file', help='Path to the HTML file containing the records')
    args = parser.parse_args()

    with open(args.html_file, 'r') as file:
        html_content = file.read()

    html_to_adif(html_content)

if __name__ == '__main__':
    main()
