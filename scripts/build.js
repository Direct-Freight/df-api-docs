#!/usr/bin/env node
'use strict';
var Path = require('path');

require('shelljs/global');
set('-e');

rm('-rf', 'web_deploy')
mkdir('-p', 'web_deploy')

cp('-R', 'web/*', 'web_deploy/');

console.log("create initial bundle without code samples");
rm('-rf', 'spec/code_samples/');
exec('npm run swagger bundle --        -o web_deploy/swagger.json');
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

console.log("we need the swagger without code for restlet");
cp('web_deploy/swagger.yaml', 'web_deploy/swagger-nocode.yaml');

console.log("generate code samples");
mkdir('-p', 'spec/code_samples/');
exec('npm run generate-code-samples skip-pre-bundle');

console.log("re-bundle with code samples");
exec('npm run swagger bundle --        -o web_deploy/swagger.json');
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

console.log("create swagger-ui directory");
var SWAGGER_UI_DIST = Path.dirname(require.resolve('swagger-ui'));
cp('-R', SWAGGER_UI_DIST, 'web_deploy/swagger-ui/')
sed('-i', 'http://petstore.swagger.io/v2/swagger.json', '../swagger.json', 'web_deploy/swagger-ui/index.html')

console.log("create a version with everything including code");
mkdir('-p', 'web_deploy/everything/swagger-ui/')
cp('web_deploy/*.*', 'web_deploy/everything/');
cp('-R', 'web_deploy/swagger-ui/', 'web_deploy/everything/swagger-ui/');

console.log("create a version that hides STAGE= items from the public view");
console.log("hiding items from public view");
exec('npm run hide-items skip-regenerate');

