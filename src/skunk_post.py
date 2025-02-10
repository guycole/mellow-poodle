import datetime
import json
import os
import pytz
import requests
import sys

import yaml
from yaml.loader import SafeLoader

class SkunkPost:

        def __init__(self, url: str):
                self.url = url

        def skunk_post(self, payload: dict[str, float]) -> None:
                response = requests.post(self.url, json=payload)
                print(response)
                print(response.text)
                
        def execute(self) -> None:
                buffer = {}

                try:
                        with open("/tmp/sensor.json") as infile:
                                buffer = json.load(infile)
                except Exception as error:
                        print(error)

                self.skunk_post(buffer)


if __name__ == '__main__':
        if len(sys.argv) > 1:
                config_name = sys.argv[1]
        else:
                config_name = "config.yaml"

        with open(config_name, "r", encoding="utf-8") as stream:
                try:
                        configuration = yaml.load(stream, Loader=SafeLoader)
                except yaml.YAMLError as error:
                        print(error)

        url = configuration['skunk_url']
                        
        poster = SkunkPost(url)
        poster.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
