var localFont = require('next/font/local');
var YeomilMono = localFont({
  src: [
    {
      path: '../../fonts/webfont/YeomilMono-Light.woff2',
      weight: '300',
      style: 'normal',
    },
    {
      path: '../../fonts/webfont/YeomilMono-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: '../../fonts/webfont/YeomilMono-Bold.woff2',
      weight: '700',
      style: 'normal',
    }
  ],
  variable: '--font-yeomil-mono'
});

module.exports = {
  YeomilMono: YeomilMono,
  default: YeomilMono
};
