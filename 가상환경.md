# 1. pyenv 사용 방법
pyenv는 Python 버전 관리 도구로, 여러 Python 버전을 쉽게 설치하고 전환할 수 있게 해주는 유용한 도구입니다. 이를 통해 글로벌 Python 환경에 영향을 주지 않고, 특정 프로젝트에서 원하는 Python 버전을 사용할 수 있습니다. 아래에서는 pyenv를 사용하는 방법

## 1. pyenv 설치
### 1. Linux (Ubuntu/Debian)
Ubuntu나 Debian 기반 시스템에서는 다음 명령어를 사용해 pyenv를 설치
```
sudo apt update
sudo apt install -y curl git
curl https://pyenv.run | bash
```
### 2. macOS (Homebrew)
```
brew install pyenv
```
### 3. Windows
WSL을 통해 Ubuntu 환경을 설정한 뒤, 위의 Linux 설치 방법에 따름

## 2. 환경 설정
pyenv를 사용하려면 터미널 환경 설정 파일(~/.bashrc 또는 ~/.zshrc)에 다음 내용을 추가 합니다.
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
설정을 적용하려면 터미널을 재시작하거나 다음 명령어를 실행합니다.
```
source ~/.bashrc  # 또는 source ~/.zshrc
```
## 3. Python 버전 설치
pyenv를 사용하면 원하는 Python 버전을 쉽게 설치
```
pyenv install 3.11.4
```
설치 과정에서 의존성 문제가 발생할 수 있는데, 특히 Linux에서는 아래와 같은 추가 패키지를 설치해야 합니다.
```
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```
## 4. 가상 환경 생성
pyenv는 virtualenv 플러그인을 통해 프로젝트별로 독립적인 가상 환경을 만듭니다.
- myenv는 가상 환경의 이름으로, 원하는 이름으로 변경할 수 있습니다.
```
pyenv virtualenv 3.11.4 myenv
```
## 5. 가상 환경 활성화
pyenv local 명령어는 현재 디렉토리와 그 하위 디렉토리에서 myenv 가상 환경을 사용하도록 설정하며, .python-version 파일을 생성합니다. 이후 해당 디렉토리에 들어갈 때마다 자동으로 가상 환경이 활성화됩니다.
```
cd my_project  # 프로젝트 디렉토리로 이동
pyenv local myenv
```
## 5. Python 버전 확인
```
python --version
```
## 6. 패키지 설치 및 작업
가상 환경 내에서는 pip를 사용해 필요한 패키지를 설치하고 Python 스크립트를 실행
```
pip install requests  # requests 패키지 설치
python my_script.py   # Python 스크립트 실행
```
## 7. 가상 환경 비활성화
```
pyenv deactivate
```

## 8. 제공된 requirements.txt 파일 있으면 
```
pip install --upgrade pip
pip install -r requirements.txt
```

## 9. 가상 환경 없이 직접 실행하기
```
/path/to/my_project/venv/bin/python /path/to/my_project/app.py
```

## 10. 백그라운드에서 실행하기
### 1.  쉘 스크립트를 작성
```
#!/usr/bin/env bash
source "/path/to/my_project/venv/bin/activate"
python -u /path/to/my_project/app.py
```
### 2. nohup을 사용하여 백그라운드에서 실행
```
chmod +x run_script.sh
nohup ./run_script.sh > output.log &
```
### 3. 시스템 서비스로 실행하기
애플리케이션을 시스템 서비스로 실행하려면 systemd 서비스 파일을 생성
```
[Unit]
Description=My Python Application

[Service]
ExecStart=/path/to/my_project/venv/bin/python /path/to/my_project/app.py
WorkingDirectory=/path/to/my_project
Restart=always
User=username

[Install]
WantedBy=multi-user.target
```
