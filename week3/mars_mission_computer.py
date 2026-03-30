import random
import datetime
import os


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
        log_file_name = 'sensor_log.csv'
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

        header = (
            'timestamp,'
            'mars_base_internal_temperature,'
            'mars_base_external_temperature,'
            'mars_base_internal_humidity,'
            'mars_base_external_illuminance,'
            'mars_base_internal_co2,'
            'mars_base_internal_oxygen\n'
        )

        log_line = (
            f'{timestamp},'
            f'{self.env_values["mars_base_internal_temperature"]:.2f},'
            f'{self.env_values["mars_base_external_temperature"]:.2f},'
            f'{self.env_values["mars_base_internal_humidity"]:.2f},'
            f'{self.env_values["mars_base_external_illuminance"]:.2f},'
            f'{self.env_values["mars_base_internal_co2"]:.4f},'
            f'{self.env_values["mars_base_internal_oxygen"]:.2f}\n'
        )

        try:
            file_exists = os.path.exists(log_file_name)

            with open(log_file_name, 'a', encoding='utf-8') as log_file:
                if not file_exists:
                    log_file.write(header)
                log_file.write(log_line)

            print('\n[시스템] 센서 데이터가 sensor_log.csv 파일에 기록되었습니다.')

        except OSError as error:
            print(f'\n[시스템] 로그 파일 저장 중 오류가 발생했습니다: {error}')

        return self.env_values


def main():
    ds = DummySensor()
    ds.set_env()
    current_environment = ds.get_env()

    print('--- 화성 기지 더미 센서 측정 결과 ---')
    for key, value in current_environment.items():
        if key == 'mars_base_internal_co2':
            print(f'{key}: {value:.4f}')
        else:
            print(f'{key}: {value:.2f}')


if __name__ == '__main__':
    main()