#!/usr/bin/env node
'use strict';
var Path = require('path');

require('shelljs/global');
set('-e');

mkdir('-p', 'web_deploy')

cp('-R', 'web/*', 'web_deploy/');

console.log("bundling json");
exec('npm run swagger bundle --        -o web_deploy/swagger.json');
console.log("bundling yaml");
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

console.log("regenerating swagger-ui");
var SWAGGER_UI_DIST = Path.dirname(require.resolve('swagger-ui'));
rm('-rf', 'web_deploy/swagger-ui/')
cp('-R', SWAGGER_UI_DIST, 'web_deploy/swagger-ui/')
sed('-i', 'http://petstore.swagger.io/v2/swagger.json', '../swagger.json', 'web_deploy/swagger-ui/index.html')
console.log("done regenerating swagger-ui");

