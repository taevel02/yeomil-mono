cask "font-yeomil-mono" do
  version "1.0.1"
  sha256 :no_check

  url "https://github.com/buddy-proiectio/yeomil-mono/releases/download/v#{version}/YeomilMono-TTF.zip"
  name "Yeomil Mono"
  desc "Unified monospace font merging Geist Mono and Pretendard CJK for developer environments"
  homepage "https://github.com/buddy-proiectio/yeomil-mono"

  font "YeomilMono-Regular.ttf"
  font "YeomilMono-Bold.ttf"
  font "YeomilMono-Light.ttf"

  # No complex uninstall block needed for fonts
end
