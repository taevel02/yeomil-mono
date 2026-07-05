# Yeomil Mono (여밀 모노)

여밀 모노는 개발자 터미널 및 IDE 환경을 위해 디자인된 고품질 CJK-영문 통합 고정폭(Monospace) 서체입니다. <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong>의 영문 기하학적 형태와 <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong>의 실용적인 한글 서체 구조를 결합하여, 한글 글리프가 깨지거나 세로 정렬이 흐트러지는 현상을 보정했습니다.

## 설치 방법

### 1. curl 설치 (권장)

터미널에서 아래의 `curl` 명령어를 실행하여 서체를 자동으로 설치할 수 있습니다 (macOS / Linux 지원):

```bash
curl -fsSL https://raw.githubusercontent.com/taevel02/yeomil-mono/main/install.sh | bash
```

### 2. 직접 다운로드

수동으로 설치하려면 GitHub Releases에서 컴파일된 서체 파일(TTF/OTF)을 직접 다운로드하여 설치하실 수 있습니다:

1. [GitHub Releases](https://github.com/taevel02/yeomil-mono/releases) 페이지로 이동합니다.
2. 최신 버전의 서체 압축 파일(`YeomilMono-TTF.zip` 또는 `YeomilMono-OTF.zip`)을 다운로드합니다.
3. 압축을 푼 뒤 서체 파일을 실행하여 시스템에 설치합니다.

### 3. Nerd Font

릴리스에는 전체 [Nerd Fonts](https://www.nerdfonts.com/) 심볼을 적용한
`YeomilMono-NerdFontMono-TTF.zip`도 포함됩니다. 설치 후 터미널에서
`YeomilMono Nerd Font Mono` 패밀리를 선택하세요.

FontForge가 설치된 환경에서는 아래 명령으로 Nerd Font 버전을 직접 빌드할 수 있습니다.

```bash
make nerd
```

결과는 `fonts/nerd-font`에 생성되며 기존 Yeomil Mono와 함께 설치할 수 있습니다.

## 라이선스

[SIL Open Font License 1.1](LICENSE)
