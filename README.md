# Yeomil Mono

Yeomil Mono is a unified CJK-Latin monospace font optimized for developer terminals and IDE environments. It aligns the horizontal metrics of <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong> (Latin) and <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong> (CJK) to ensure Hangul glyphs render reliably without clipping or vertical misalignment.

## Installation

### macOS (Homebrew Cask)

You can install the font by tapping the repository and installing the cask:

```bash
brew tap buddy-proiectio/yeomil-mono https://github.com/buddy-proiectio/yeomil-mono.git
brew install --cask font-yeomil-mono
```

### curl (macOS / Linux)

You can install the font using `curl` via the automated installation script:

```bash
curl -fsSL https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/install.sh | bash
```

Or you can download the font files directly using `curl`:

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

You can install the font on Windows using PowerShell via the automated installation script:

```powershell
irm https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/install.ps1 | iex
```

Or you can download the font files directly using `curl.exe`:

```cmd
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Regular.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Regular.ttf"
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Bold.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Bold.ttf"
curl.exe -fLo "%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts\YeomilMono-Light.ttf" "https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf/YeomilMono-Light.ttf"
```

_(Note: If downloading manually, you will need to open `%USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts` and double-click the files to register them in Windows, or run the PowerShell script to register them automatically.)_

## Building

To build the font binaries locally, set up the environment and run the pipeline:

```bash
make dev
make run
```

Downloads the original Geist Mono and Pretendard release files, applies the 1:2 scaling transformations, and compiles them to `fonts/` in TTF, OTF, and WOFF2 formats.

### Linting & Formatting

```bash
make lint
make format
```

### Test Suite

```bash
make test
```

## License

[SIL Open Font License 1.1](LICENSE)
