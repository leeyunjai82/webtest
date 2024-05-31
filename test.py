import serial
import time

# 시리얼 포트 설정
ser = serial.Serial(
    port='/dev/ttyS0',        # 사용중인 포트에 맞게 수정하세요
    baudrate=115200,
    timeout=1
)

while True:
  lines = ser.readlines()
  print(lines)

  if len(lines) > 0:
    with open('aaa.py', 'w') as file:
      for line in lines:
        # 바이트 데이터를 문자열로 디코딩하여 파일에 쓰기
        decoded_line = line.decode('utf-8')
        file.write(decoded_line)
    print('file save ok')
    
