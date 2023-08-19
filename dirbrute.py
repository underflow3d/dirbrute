import requests
import argparse

valid_status_codes = [200, 301]

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True)
parser.add_argument('-w', '--wordlist', type=str, required=True)
args = parser.parse_args()

wordlist = open(args.wordlist, 'r')

while True:
    page = wordlist.readline().replace('\n', '')
    if page == '':
        break
    else:
        m_url = args.url + page
        resp = requests.get(m_url)
        if resp.status_code in valid_status_codes:
            print(f'Found: {m_url}')
        else:
            continue

wordlist.close()

print('Attack finished!')
