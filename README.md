# Yeomil Mono

Yeomil Mono is a unified CJK-Latin monospace font optimized for developer terminals and IDE environments. It aligns the horizontal metrics of <strong>[Geist Mono](https://github.com/vercel/geist-font)</strong> (Latin) and <strong>[Pretendard](https://github.com/orioncactus/pretendard)</strong> (CJK) to ensure Hangul glyphs render reliably without clipping or vertical misalignment.

## Installation

### macOS (Homebrew Cask)

```bash
brew tap taevel02/yeomil-mono
brew install --cask font-yeomil-mono
```

## Building

To build the font binaries locally:

```bash
make dev
make run
```

This compiles both TTF and WOFF2 formats under the `packages/yeomil-mono/dist/` directory.

## License

[SIL Open Font License 1.1](LICENSE)
