cask "font-yeomil-mono" do
  version "1.0.2"
  sha256 :no_check

  url "https://github.com/buddy-proiectio/yeomil-mono/releases/download/v#{version}/YeomilMono-TTF.zip"
  name "Yeomil Mono"
  desc "Monospace font combining Geist Mono and Pretendard CJK"
  homepage "https://github.com/buddy-proiectio/yeomil-mono"

  livecheck do
    url :url
    strategy :github_latest
  end

  font "YeomilMono-Regular.ttf"
  font "YeomilMono-Bold.ttf"
  font "YeomilMono-Light.ttf"

  # No complex uninstall block needed for fonts
end
