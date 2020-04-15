#!/usr/bin/node
'use strict'
require('shelljs/global');
var fs = require('fs');
var YAML = require('js-yaml');

if(process.argv[2] != 'skip-regenerate')
        {
        console.log("first regenerate combined file to ensure it is up to date");
        exec('swagger-repo bundle -y -o ./web_deploy/swagger.yaml'); //this wants a single dot
        }

//now load that file
var swagger = YAML.safeLoad(fs.readFileSync('web_deploy/swagger.yaml', 'utf-8'));

function hide_items(tree) {
        Object.keys(tree).forEach(function(key) { 
                if(typeof(tree[key]) === 'object') 
                        {
                        hide_items(tree[key]); 
                        if (typeof(tree[key]['delete_me']) === 'string') 
                                { 
                                delete tree[key]; 
                                }
                        } 
                if(typeof(tree[key]) === 'string' && tree[key].indexOf('STAGE=') >= 0) 
                        {
                        tree['delete_me'] = "delete_me";
                        }
                });
}

hide_items(swagger);

/*  OLD METHOD THAT JUST HID SUMMARY NOT ANY NODE
Object.keys(swagger).forEach(function(level1) {
        //toplevels console.log(level1);
        Object.keys(swagger[level1]).forEach(function(level2) {
                //methods console.log(level2);
                Object.keys(swagger[level1][level2]).forEach(function(level3) {
                        //get/post/delete  console.log(level3);
                        if(swagger[level1][level2][level3]['summary'] && swagger[level1][level2][level3]['summary'].indexOf('STAGE=') >= 0) 
                                {
                                delete swagger[level1][level2][level3]; //hide the method
                                }
                });
        });
});
*/

console.log('Saving modified yaml');
fs.writeFile('web_deploy/swagger.yaml', YAML.safeDump(swagger, {indent: 2, lineWidth: -1, noRefs: true, sortKeys: true}), (err) => {
        if (err) 
                {
                console.log('ERROR WRITING: web_deploy/swagger.yaml');
                console.log(err);
                console.log(process.cwd());
                }
        });

console.log('Saving modified json');
fs.writeFile('web_deploy/swagger.json', JSON.stringify(swagger, null, 2) + '\n' , (err) => {
        if (err) 
                {
                console.log('ERROR WRITING: web_deploy/swagger.json');
                console.log(err);
                console.log(process.cwd());
                }
        });
