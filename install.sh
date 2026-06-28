#!/bin/bash
set -e

# Detect OS
OS_TYPE=$(uname)

if [ "$OS_TYPE" = "Darwin" ]; then
    FONT_DIR="$HOME/Library/Fonts"
    echo "Installing Yeomil Mono for macOS..."
elif [ "$OS_TYPE" = "Linux" ]; then
    FONT_DIR="$HOME/.local/share/fonts"
    echo "Installing Yeomil Mono for Linux..."
else
    echo "Unsupported OS: $OS_TYPE"
    exit 1
fi

# Create directory if it doesn't exist
mkdir -p "$FONT_DIR"

# Download fonts
FONTS=("Regular" "Bold" "Light")
BASE_URL="https://raw.githubusercontent.com/buddy-proiectio/yeomil-mono/main/fonts/ttf"

for weight in "${FONTS[@]}"; do
    FILE_NAME="YeomilMono-${weight}.ttf"
    echo "Downloading ${FILE_NAME}..."
    curl -fsSL "${BASE_URL}/${FILE_NAME}" -o "${FONT_DIR}/${FILE_NAME}"
done

# Update font cache for Linux
if [ "$OS_TYPE" = "Linux" ]; then
    if command -v fc-cache >/dev/null 2>&1; then
        echo "Updating font cache..."
        fc-cache -f
    else
        echo "Warning: fc-cache command not found. You might need to update your font cache manually."
    fi
fi

echo "Yeomil Mono installed successfully!"
