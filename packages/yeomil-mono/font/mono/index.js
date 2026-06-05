var localFont = require('next/font/local');
var YeomilMono = localFont({
  src: [
    {
      path: '../../dist/web/YeomilMono-Light.woff2',
      weight: '300',
      style: 'normal',
    },
    {
      path: '../../dist/web/YeomilMono-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: '../../dist/web/YeomilMono-Bold.woff2',
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
