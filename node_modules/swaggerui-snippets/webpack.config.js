const path = require('path');

module.exports = {
  entry: './code-snippets/swaggerui-snippets.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'swaggerui-snippets.bundle.js'
  }
};