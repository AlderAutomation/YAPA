import config
import requests
import time 
import hashlib
import json
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

class rss_manipulator():

    def __init__(self) -> None:
        
        api_key = config.key
        api_secret = config.secret
        epoch_time = int(time.time())

        data_to_hash = api_key + api_secret + str(epoch_time)
        sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()

        self.headers = {
            'X-Auth-Date': str(epoch_time),
            'X-Auth-Key': api_key,
            'Authorization': sha_1,
            'User-Agent': 'postcasting-index-python-cli'    
        }

        self.base_url = "https://api.podcastindex.org/api/1.0"


    def find_cast(self, query: str) -> json:
        url = self.base_url + "/search/byterm?q=" + query

        response = requests.post(url, headers=self.headers)

        if response.status_code == 200:
            print ('<< Received >>')
            json_data = json.loads(response.text)
            logger.info(json.dumps(json_data, indent=2))

            return json_data
        else:
            print ('<< Received ' + str(r.status_code) + '>>')


    def get_episodes(self, id_val) -> json:
        url = self.base_url + "/episodes/byfeedid?id=" + str(id_val)

        r = requests.post(url, headers=self.headers)

        if r.status_code == 200:
            print ('<< Received >>')
            pretty_json = json.loads(r.text)
            logger.info(json.dumps(pretty_json, indent=2))
            # print (json.dumps(pretty_json, indent=2))
            return pretty_json                    
        else:
            print ('<< Received ' + str(r.status_code) + '>>')
    


    def subscribe_to_cast(self):
        pass


    def play_cast(self):
        pass


def main():
    # self.coder_radio_id = 487548
    # self.talk_python_id = 742305

    # rss_manipulator().find_cast("talk python")
    rss_manipulator().get_episodes()


if __name__ == "__main__":
    main()