from flask import request
import config
import requests
import time 
import hashlib
import json
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

api_key = config.key
api_secret = config.secret
epoch_time = int(time.time())

data_to_hash = api_key + api_secret + str(epoch_time)
sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()

headers = {
    'X-Auth-Date': str(epoch_time),
    'X-Auth-Key': api_key,
    'Authorization': sha_1,
    'User-Agent': 'postcasting-index-python-cli'    
}

coder_radio_id = 487548
base_url = "https://api.podcastindex.org/api/1.0"

def find_cast(query: str):
    url = base_url + "/search/byterm?q=" + query

    r = requests.post(url, headers=headers)

    if r.status_code == 200:
        print ('<< Received >>')
        pretty_json = json.loads(r.text)
        logger.info(json.dumps(pretty_json, indent=2))
        print (json.dumps(pretty_json, indent=2))
    else:
        print ('<< Received ' + str(r.status_code) + '>>')


def get_episodes(feed_id:int):
    url = base_url + "/episodes/byfeedid?id=" + str(feed_id)

    r = requests.post(url, headers=headers)

    if r.status_code == 200:
        print ('<< Received >>')
        pretty_json = json.loads(r.text)
        logger.info(json.dumps(pretty_json, indent=2))
        print (json.dumps(pretty_json, indent=2))
    else:
        print ('<< Received ' + str(r.status_code) + '>>')
 


def subscribe_to_cast():
    pass


def play_cast():
    pass


def main():
    # find_cast("coder radio")
    get_episodes(coder_radio_id)


if __name__ == "__main__":
    main()