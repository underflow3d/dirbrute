import requests
import argparse

valid_status_codes = [200, 301]

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, required=True)
parser.add_argument("-w", "--wordlist", type=str, required=True)
args = parser.parse_args()

if args.url.endswith("/") == False:
    args.url = args.url + "/"

wordlist = open(args.wordlist, "r")

while True:
    word = wordlist.readline().replace("\n", "")
    if word == "":
        break
    else:
        url = args.url + word
        resp = requests.get(url)
        if resp.status_code in valid_status_codes:
            print(f"Found: {url}")
        else:
            continue

wordlist.close()

print("Attack finished!")
