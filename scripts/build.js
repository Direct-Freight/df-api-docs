#!/usr/bin/env node
'use strict';
var Path = require('path');

require('shelljs/global');
set('-e');

rm('-rf', 'web_deploy')
mkdir('-p', 'web_deploy')

cp('-R', 'web/*', 'web_deploy/');

exec('npm run swagger bundle --        -o web_deploy/swagger.json');
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

var SWAGGER_UI_DIST = Path.dirname(require.resolve('swagger-ui'));
cp('-R', SWAGGER_UI_DIST, 'web_deploy/swagger-ui/')
sed('-i', 'http://petstore.swagger.io/v2/swagger.json', '../swagger.json', 'web_deploy/swagger-ui/index.html')

console.log("create a version without code but has everything");
mkdir('-p', 'web_deploy/nocode/swagger-ui/')
cp('web_deploy/*.*', 'web_deploy/nocode/');
cp('-R', 'web_deploy/swagger-ui/', 'web_deploy/nocode/swagger-ui/');

console.log("generating code samples");
exec('npm run generate-code-samples');

console.log("rebundle with the code");
exec('npm run swagger bundle --        -o web_deploy/swagger.json');
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

console.log("create a version that shows everything");
mkdir('-p', 'web_deploy/everything/swagger-ui/')
cp('web_deploy/*.*', 'web_deploy/everything/');
cp('-R', 'web_deploy/swagger-ui/', 'web_deploy/everything/swagger-ui/');


console.log("make the restlet directory public");
mkdir('-p', 'web_deploy/restlet_studio/')
cp('restlet_studio/*.*', 'web_deploy/restlet_studio/');

console.log("create a version that hides stuff from the default view");
console.log("hiding items from public view");
exec('npm run hide-items skip-regenerate');

