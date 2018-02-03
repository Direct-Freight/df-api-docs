#!/usr/bin/node
'use strict'
var fs = require('fs')
var mkdirp = require('mkdirp')
var stringifyObject = require('stringify-object');
var SwaggerSnippet = require('swagger-snippet')

var SwaggerFile = require('./web_deploy/swagger.json')

//var result = SwaggerSnippet.getEndpointSnippets(SwaggerFile, '/boards/{board_type}', 'post' ,['shell_wget','shell_curl'])
var results = SwaggerSnippet.getSwaggerSnippets(SwaggerFile, ['shell_curl'])


results.forEach(function(result)
        {
        var path = result.url.replace(/http.*api\//,'').replace(/\//g,'@');
        const pretty = stringifyObject(result.snippets, { indent: '  ', singleQuotes: false });
        console.log(pretty);
        result.snippets.forEach(function(snippet)
                {
                var ext = '.txt';
                var lang = 'Unknown';
                if(snippet.id == 'shell_curl') { var ext = '.sh'; var lang = 'Shell'; }
                var dir = 'spec/code_samples/' + lang + '/' + path + '/';
                mkdirp(dir);
                console.log(dir);
                console.log(snippet.id);
                console.log(snippet.content);
                fs.writeFile(dir + result.method.toLowerCase() + ext,snippet.content);
                })
        })

console.log("WARNING:  this uses the web_deploy directory which is in .gitignore so make sure to run 'npm start'")
console.log("WARNING:  before using this program to make sure your full swagger.yaml is up to date.")
