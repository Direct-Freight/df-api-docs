#!/usr/bin/node
'use strict'
var fs = require('fs');
var YAML = require('js-yaml');
var swagger = YAML.safeLoad(fs.readFileSync('web_deploy/swagger.yaml', 'utf-8'));
Object.keys(swagger).forEach(function(level1) {
        //toplevels console.log(level1);
        Object.keys(swagger[level1]).forEach(function(level2) {
                //methods console.log(level2);
                Object.keys(swagger[level1][level2]).forEach(function(level3) {
                        //get/post/delete  console.log(level3);
                        if(swagger[level1][level2][level3]['summary'] && swagger[level1][level2][level3]['summary'].indexOf('HIDE=') >= 0) 
                                {
                                delete swagger[level1][level2][level3]; //hide the method
                                }
                });
        });
});
console.log(YAML.safeDump(swagger, {noRefs: true}));

