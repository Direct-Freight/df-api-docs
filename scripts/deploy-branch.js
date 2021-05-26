#!/usr/bin/env node
'use strict';
require('shelljs/global');
var path = require('path');

set('-e');
set('-v');

console.log('jglog: deploy-branch START');
var branch = process.env.TRAVIS_BRANCH && process.env.TRAVIS_BRANCH.toLowerCase();
if (branch && branch !== 'gh-pages') {
  var branchPath = path.join('.tmp', 'preview', branch, '/');
  mkdir('-p', branchPath);
  exec('npm run swagger bundle -- -o ' + branchPath + 'swagger.json');
  exec('npm run swagger bundle -- --yaml -o ' + branchPath + 'swagger.yaml');
  exec('npm run hide-items ' + branchPath + ' skip-regenerate');
  console.log("copying index.html");
  cp('web/index.html', branchPath);
  exec('deploy-to-gh-pages --update .tmp');
}
console.log('jglog: deploy-branch END');
