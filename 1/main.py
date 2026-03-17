# main.py

def main():
    # 'Hello Mars' 출력
    print('Hello Mars')
    print('-' * 30)

    log_filename = 'mission_computer_main.log'
    error_filename = 'error_log.txt'

    try:
        # UTF-8 인코딩으로 파일 열기
        with open(log_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 보너스 과제 1: 출력 결과를 시간의 역순으로 정렬
        reversed_lines = lines[::-1]

        error_lines = []

        # 전체 내용을 역순으로 화면에 출력 및 예외 상황(사고 원인) 수집
        for line in reversed_lines:
            clean_line = line.strip()
            if clean_line:
                print(clean_line)
                
                # 'unstable'이나 'explosion' 키워드가 있으면 문제로 간주
                if 'unstable' in clean_line or 'explosion' in clean_line:
                    error_lines.append(clean_line)

        # 보너스 과제 2: 문제가 되는 부분만 따로 파일로 저장
        if error_lines:
            with open(error_filename, 'w', encoding='utf-8') as error_file:
                for error_line in error_lines:
                    error_file.write(error_line + '\n')
            print('-' * 30)
            print(f'문제가 발생한 로그를 {error_filename} 파일에 저장했습니다.')

    # 발생할 수 있는 예외 처리
    except FileNotFoundError:
        print('로그 파일을 찾을 수 없습니다. 파일 이름을 확인해 주세요.')
    except Exception as e:
        print(f'파일을 처리하는 중 알 수 없는 오류가 발생했습니다: {e}')

if __name__ == '__main__':
    main()