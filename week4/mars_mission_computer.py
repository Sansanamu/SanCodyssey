import random
import json
import time


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = random.uniform(18.0, 30.0)
        self.env_values['mars_base_external_temperature'] = random.uniform(0.0, 21.0)
        self.env_values['mars_base_internal_humidity'] = random.uniform(50.0, 60.0)
        self.env_values['mars_base_external_illuminance'] = random.uniform(500.0, 715.0)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4.0, 7.0)

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

        self.ds = DummySensor()

        self.history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

    def print_average(self):
        average_values = {}

        for key, value_list in self.history.items():
            if len(value_list) > 0:
                average_values[key] = round(sum(value_list) / len(value_list), 3)
            else:
                average_values[key] = 0.0

        print('--- 5분 평균 환경값 ---')
        print(json.dumps(average_values, indent=4))
        print()

    def get_sensor_data(self):
        count = 0

        try:
            while True:
                self.ds.set_env()
                self.env_values = self.ds.get_env().copy()

                for key, value in self.env_values.items():
                    self.history[key].append(value)

                print(json.dumps(self.env_values, indent=4))
                print()

                count += 1

                if count % 60 == 0:
                    self.print_average()

                    for key in self.history:
                        self.history[key] = []

                time.sleep(5)

        except KeyboardInterrupt:
            print('System stopped....')


RunComputer = MissionComputer()
RunComputer.get_sensor_data()