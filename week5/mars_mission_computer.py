# mars_mission_computer.py

import json
import platform
import psutil


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
        self.setting_file_name = 'setting.txt'

    def load_settings(self):
        default_settings = {
            'operating_system': True,
            'operating_system_version': True,
            'cpu_type': True,
            'cpu_core_count': True,
            'memory_size': True,
            'cpu_usage': True,
            'memory_usage': True
        }

        try:
            with open(self.setting_file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()

                    if not line or '=' not in line:
                        continue

                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().lower()

                    if key in default_settings:
                        default_settings[key] = (value == 'true')

        except FileNotFoundError:
            print('setting.txt 파일이 없어 기본 설정으로 실행합니다.')
        except Exception as error:
            print(f'setting.txt 파일을 읽는 중 오류가 발생했습니다: {error}')

        return default_settings

    def get_mission_computer_info(self):
        settings = self.load_settings()
        info = {}

        try:
            if settings['operating_system']:
                info['operating_system'] = platform.system()

            if settings['operating_system_version']:
                info['operating_system_version'] = platform.version()

            if settings['cpu_type']:
                info['cpu_type'] = platform.processor()

            if settings['cpu_core_count']:
                info['cpu_core_count'] = psutil.cpu_count(logical=True)

            if settings['memory_size']:
                memory_size = psutil.virtual_memory().total
                info['memory_size'] = f'{round(memory_size / (1024 ** 3), 2)} GB'

            print('--- Mission Computer System Info ---')
            print(json.dumps(info, indent=4))
            print()

            return info

        except Exception as error:
            print(f'시스템 정보를 가져오는 중 오류가 발생했습니다: {error}')
            return {}

    def get_mission_computer_load(self):
        settings = self.load_settings()
        load = {}

        try:
            if settings['cpu_usage']:
                load['cpu_usage'] = f'{psutil.cpu_percent(interval=1)} %'

            if settings['memory_usage']:
                load['memory_usage'] = f'{psutil.virtual_memory().percent} %'

            print('--- Mission Computer Load ---')
            print(json.dumps(load, indent=4))
            print()

            return load

        except Exception as error:
            print(f'시스템 부하 정보를 가져오는 중 오류가 발생했습니다: {error}')
            return {}


if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()