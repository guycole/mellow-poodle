import datetime
import json
import os
import pytz
import requests
import sys
import time

import yaml
from yaml.loader import SafeLoader

from sense_hat import SenseHat

class SensorCollector:
        def collector(self) -> dict[str, float]:
                results = {}
                results['time_stamp_z'] = datetime.datetime.now(datetime.timezone.utc).isoformat()

                sense = SenseHat()

                sense.low_light = True
                sense.set_imu_config(False, True, True)

                sense.show_message("xxx")

                results['temperature_c'] = sense.get_temperature()
                results['humidity_pct']= sense.get_humidity()
                results['pressure_mb'] = sense.get_pressure()

                orientation = sense.get_orientation_radians()
                results['orientation_roll_rads'] = orientation['roll']
                results['orientation_pitch_rads'] = orientation['pitch']
                results['orientation_yaw_rads'] = orientation['yaw']                
                return results

        def execute(self) -> None:
                valuez = self.collector()
                print(valuez)

                with open("/tmp/sensor.json", "w") as stream:
                        try:
                                json.dump(valuez, stream)
                        except Exception as error:
                              print(error)  

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

        collector = SensorCollector()
        collector.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
