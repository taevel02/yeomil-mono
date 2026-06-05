# Yeomil Mono (여밀 모노)

여밀 모노는 개발자 터미널 및 IDE 환경을 위해 디자인된 고품질 CJK-영문 통합 고정폭(Monospace) 서체입니다. <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong>의 영문 기하학적 형태와 <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong>의 실용적인 한글 서체 구조를 결합하여, 한글 글리프가 깨지거나 세로 정렬이 흐트러지는 현상을 보정했습니다.

## 설치 방법

### macOS (Homebrew Cask)

```bash
brew tap taevel02/yeomil-mono
brew install --cask font-yeomil-mono
```

## 빌드 방법

로컬에서 서체 바이너리를 컴파일하려면 다음을 실행하십시오:

```bash
make dev
make run
```

이 과정은 `packages/yeomil-mono/dist/` 경로 하위에 TTF와 WOFF2 포맷 서체를 각각 컴파일하여 생성합니다.

## 라이선스

[SIL Open Font License 1.1](LICENSE)
