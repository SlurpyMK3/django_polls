// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
