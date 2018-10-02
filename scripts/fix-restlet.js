#!/usr/bin/node
'use strict'
require('shelljs/global');
var fs = require('fs');
var YAML = require('js-yaml');
var filename = process.argv[2];

//now load that file
var swagger = YAML.safeLoad(fs.readFileSync(filename, 'utf-8'));

console.log('Saving unmodified yaml:' + filename + '-sorted');
fs.writeFile(filename + '-sorted', YAML.safeDump(swagger, {indent: 2, lineWidth: -1, noRefs: false, sortKeys: true}), (err) => {
        if (err) 
                {
                console.log('ERROR WRITING: ' + filename + '-sorted');
                console.log(err);
                console.log(process.cwd());
                }
        });

function process_parameters(parameters)
        {
        var x = 0;
        parameters.forEach(function(level5) {
                if(level5.name == 'end-user-token')  //this hack is breaking curl and other code samples.
                        {
                        if(level5.required)
                                {
                                parameters.splice(x,1);
                                parameters.unshift({ '$ref': '#/parameters/end-user-token' });
                                //parameters.push({ '$ref': '#/parameters/end-user-token' });
                                //parameters[x] = { '$ref': '#/parameters/end-user-token' };
                                }
                        else
                                {
                                parameters.splice(x,1);
                                parameters.unshift({ '$ref': '#/parameters/end-user-token-optional' });
                                }
                        }
                if(level5.name == 'board_type' || level5.name == 'posting_type')
                        {
                        parameters.splice(x,1);
                        parameters.unshift({ '$ref': '#/parameters/' + level5.name });
                        }
                x++;
                });
        }

swagger['info']['x-logo'] = { url: 'https://www.directfreight.com/home/images/logo-direct-freight.png' };

Object.keys(swagger).forEach(function(level1) {
        //toplevels console.log(level1);
        Object.keys(swagger[level1]).forEach(function(level2) {
                //methods console.log(level2);
                Object.keys(swagger[level1][level2]).forEach(function(level3) {
                        //get/post/delete  console.log(level3); //sometimes restlet puts global path parameters at level3
//                        if(swagger[level1][level2]['parameters']) { process_parameters(swagger[level1][level2]['parameters']); }
//                        if(swagger[level1][level2][level3]['parameters']) { process_parameters(swagger[level1][level2][level3]['parameters']); }

                        if(swagger[level1][level2][level3]['responses'] && 
                           swagger[level1][level2][level3]['responses']['201'] &&
                           swagger[level1][level2][level3]['responses']['201']['schema'] &&
                           swagger[level1][level2][level3]['responses']['201']['schema']['$ref'] &&
                           swagger[level1][level2][level3]['responses']['201']['schema']['$ref'] == '#/definitions/create_status')
                                {
                                swagger[level1][level2][level3]['responses']['201'] = { '$ref': '#/responses/object_created' };
                                }
                        if(swagger[level1][level2][level3]['responses'] && 
                           swagger[level1][level2][level3]['responses']['422'] &&
                           swagger[level1][level2][level3]['responses']['422']['schema'] &&
                           swagger[level1][level2][level3]['responses']['422']['schema']['$ref'] &&
                           swagger[level1][level2][level3]['responses']['422']['schema']['$ref'] == '#/definitions/error_object')
                                {
                                swagger[level1][level2][level3]['responses']['422'] = { '$ref': '#/responses/error_422' };
                                }
                });
        });
});

console.log('Saving modified yaml:' + filename + '-modified');
fs.writeFile(filename + '-modified', YAML.safeDump(swagger, {indent: 2, lineWidth: -1, noRefs: false, sortKeys: true}), (err) => {
        if (err) 
                {
                console.log('ERROR WRITING: ' + filename + '-modified');
                console.log(err);
                console.log(process.cwd());
                }
        });

