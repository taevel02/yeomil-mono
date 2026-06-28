# Yeomil Mono (여밀 모노)

여밀 모노는 개발자 터미널 및 IDE 환경을 위해 디자인된 고품질 CJK-영문 통합 고정폭(Monospace) 서체입니다. <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong>의 영문 기하학적 형태와 <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong>의 실용적인 한글 서체 구조를 결합하여, 한글 글리프가 깨지거나 세로 정렬이 흐트러지는 현상을 보정했습니다.

## 설치 방법

### macOS (Homebrew Cask)

저장소를 Tap으로 추가한 후 Cask로 설치할 수 있습니다:
```bash
brew tap buddy-proiectio/yeomil-mono https://github.com/buddy-proiectio/yeomil-mono.git
brew install --cask font-yeomil-mono
```

### curl (macOS / Linux)

자동 설치 스크립트를 사용하여 `curl`로 서체를 설치할 수 있습니다:
```bash
curl -fsSL https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/install.sh | bash
```

또는 아래와 같이 `curl`을 통해 서체 파일을 직접 다운로드하여 설치할 수도 있습니다:

**macOS:**
```bash
curl -fLo ~/Library/Fonts/'YeomilMono-#1.ttf' 'https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-{Regular,Bold,Light}.ttf'
```

**Linux:**
```bash
mkdir -p ~/.local/share/fonts
curl -fLo ~/.local/share/fonts/'YeomilMono-#1.ttf' 'https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-{Regular,Bold,Light}.ttf'
fc-cache -f
```

### PowerShell (Windows)

PowerShell 자동 설치 스크립트를 사용하여 Windows 환경에 서체를 설치할 수 있습니다:
```powershell
irm https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/install.ps1 | iex
```

또는 `curl.exe`를 통해 서체 파일을 직접 다운로드하여 설치할 수도 있습니다:
```cmd
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Regular.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Regular.ttf"
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Bold.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Bold.ttf"
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Light.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Light.ttf"
```
*(주의: 파일을 수동으로 다운로드한 경우, `%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts` 경로를 열어 서체 파일을 더블 클릭하여 직접 윈도우에 등록하거나, 위의 PowerShell 스크립트를 사용하여 자동 등록을 진행해야 합니다.)*



## 빌드 방법

로컬에서 서체 바이너리를 컴파일하려면 다음을 실행하십시오:

```bash
make dev
make run
```

이 과정은 `fonts/` 경로 하위에 TTF, OTF 및 WOFF2 포맷 서체를 컴파일하여 생성합니다.

## 저장소 구조
```
yeomil-mono/
├── fonts/              # 컴파일 완료된 서체 파일 (TTF, OTF, WOFF2)
├── docs/               # 테크니컬 라이트 테마 웹 문서화 페이지
├── src/                # 파이썬 빌더 소스 코드
├── Casks/              # Homebrew 포뮬러
└── Makefile            # 태스크 실행 스크립트
```

## 라이선스

[SIL Open Font License 1.1](LICENSE)
