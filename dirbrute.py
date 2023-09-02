import requests
import argparse

valid_status_codes = [200, 301]

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, required=True)
parser.add_argument("-w", "--wordlist", type=str, required=True)
args = parser.parse_args()

if not args.url.endswith("/"):
    args.url = args.url + "/"

with open(args.wordlist, "r") as wordlist:
    for word in wordlist:
        url = args.url + word
        resp = requests.get(url)
        if resp.status_code in valid_status_codes:
            print(f"Found: {url}, status code {resp.status_code}")
        else:
            continue


print("Attack finished!")
