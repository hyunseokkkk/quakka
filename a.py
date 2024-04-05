import subprocess

# cmd를 사용하여 ls 명령어 실행
result = subprocess.run(['cmd.exe', '/c', 'dir'], stdout=subprocess.PIPE, text=True)

# 결과 출력
print(result.stdout)