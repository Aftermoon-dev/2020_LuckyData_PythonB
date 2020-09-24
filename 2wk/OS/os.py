import os

# system - Windows에서는 CMD 명령어 사용, 리눅스에서는 Shell 사용
print('Network Interface Info (Windows) : ')
os.system('ipconfig')

# getcwd - 현재 디렉토리 가져옴
print('Current Directory : ', os.getcwd())

# listdir - 지정한 디렉토리의 파일 리스트를 가져옴
print('Get Current Directory File List : ')
print(os.listdir(os.getcwd()))

# chdir - 디렉토리 경로 설정 (CMD나 Shell의 cd같은 역할)
print('Change Dir to C Drive')
os.chdir('C:\\')
print('Current Directory : ', os.getcwd())

# getpid - 현재 실행중인 프로그램의 Process ID를 가져옴
print('Current PID :')
print(os.getpid())

