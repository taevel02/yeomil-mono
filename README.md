# Yeomil Mono

Yeomil Mono is a unified CJK-Latin monospace font optimized for developer terminals and IDE environments. It aligns the horizontal metrics of <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong> (Latin) and <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong> (CJK) to ensure Hangul glyphs render reliably without clipping or vertical misalignment.

## Installation

### macOS (Homebrew Cask)

```bash
brew tap taevel02/yeomil-mono
brew install --cask font-yeomil-mono
```

## Building

To build the font binaries locally, set up the environment and run the pipeline:

```bash
make dev
make run
```
Downloads the original Geist Mono and Pretendard release files, applies the 1:2 scaling transformations, and compiles them to `packages/yeomil-mono/fonts/` in TTF, OTF, and WOFF2 formats.

### Linting & Formatting
```bash
make lint
make format
```

### Test Suite
```bash
make test
```

---

## Repository Structure
```
yeomil-mono/
├── fonts/              # Compiled font formats (TTF, OTF, WOFF2)
├── docs/               # Technical light-theme web documentation
├── src/                # Python builder pipeline
├── Casks/              # Homebrew Formula
├── package.json        # NPM package configuration
└── Makefile            # Task runners
```

## License

[SIL Open Font License 1.1](LICENSE)
