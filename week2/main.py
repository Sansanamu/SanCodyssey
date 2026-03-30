# main.py

def main():
    csv_file = 'Mars_Base_Inventory_List.csv'
    danger_csv_file = 'Mars_Base_Inventory_danger.csv'
    bin_file = 'Mars_Base_Inventory_List.bin'

    inventory_list = []
    header = []

    # 1. & 2. 파일 읽어서 출력 및 Python 리스트 객체로 변환
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            print('--- 원본 파일 내용 ---')
            for line in lines:
                print(line.strip())
                
            if not lines:
                return

            # 첫 줄은 헤더로 분리
            header_line = lines[0].strip()
            header = header_line.split(',')
            
            # 리스트(배열) 객체로 변환
            for line in lines[1:]:
                row = line.strip().split(',')
                inventory_list.append(row)
                
    except FileNotFoundError:
        print(f"'{csv_file}' 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return
    except Exception as e:
        print(f'파일을 읽는 중 오류가 발생했습니다: {e}')
        return

    # 3. 인화성이 높은 순(내림차순)으로 정렬
    # 인화성 지수는 마지막인 4번 인덱스에 위치하므로 float 형변환 후 정렬
    try:
        inventory_list.sort(key=lambda x: float(x[4]), reverse=True)
    except ValueError as e:
        print(f'정렬 중 오류가 발생했습니다 (숫자 변환 실패): {e}')
        return

    # 4. 인화성 지수가 0.7 이상인 목록 추출 및 화면 출력
    danger_list = []
    
    print('\n--- 인화성 0.7 이상인 화물 목록 ---')
    print(','.join(header))
    
    for row in inventory_list:
        flammability = float(row[4])
        if flammability >= 0.7:
            danger_list.append(row)
            print(','.join(row))

    # 5. 인화성 지수 0.7 이상 목록을 별도 CSV로 저장
    try:
        with open(danger_csv_file, 'w', encoding='utf-8') as f:
            f.write(','.join(header) + '\n')
            for row in danger_list:
                f.write(','.join(row) + '\n')
        print(f'\n위험 물질 목록이 \'{danger_csv_file}\'에 성공적으로 저장되었습니다.')
    except Exception as e:
        print(f'CSV 파일 저장 중 오류가 발생했습니다: {e}')

    # 6. 보너스 과제: 인화성 순서로 정렬된 배열을 이진(Binary) 파일로 저장
    try:
        # 이진 파일은 'wb' (write binary) 모드로 열어야 함
        with open(bin_file, 'wb') as f:
            # 문자열을 이진 데이터(bytes)로 변환(encode)하여 저장
            f.write((','.join(header) + '\n').encode('utf-8'))
            
            for row in inventory_list:
                line_data = ','.join(row) + '\n'
                f.write(line_data.encode('utf-8'))
        print(f'정렬된 목록이 이진 파일 \'{bin_file}\'에 성공적으로 저장되었습니다.')
    except Exception as e:
        print(f'이진 파일 저장 중 오류가 발생했습니다: {e}')

    # 7. 보너스 과제: 저장된 이진 파일의 내용을 다시 읽어 들여서 화면에 출력
    try:
        # 이진 파일은 'rb' (read binary) 모드로 열어야 함
        with open(bin_file, 'rb') as f:
            binary_data = f.read()
            # 이진 데이터(bytes)를 다시 문자열로 변환(decode)
            decoded_data = binary_data.decode('utf-8')
            
            print('\n--- 이진 파일에서 읽어 들인 내용 ---')
            print(decoded_data.strip())
            
    except Exception as e:
        print(f'이진 파일 읽기 중 오류가 발생했습니다: {e}')

if __name__ == '__main__':
    main()