module.exports = function () {
    var SwaggerSnippet = require('swagger-snippet');
    var HighlightJs = require('highlight.js');
    var $ = require("jquery");
    var CodeSnippets = require('./code-snippets-tabs.js');

    var codeSamplesStyle = document.createElement('style');
    codeSamplesStyle.innerHTML = '/* Style the tab */div.tab{overflow: hidden;}/* Style the buttons inside the tab */div.tab button{color:#000000; float: left; outline: none; cursor: pointer; padding: 7px 8px; transition: 0.3s; font-size: 14px;}/* Change background color of buttons on hover */div.tab button:hover{background-color: #0f6ab4; color:#ffffff;}/* Create an active/current tablink class */div.tab button.active{background-color: #0f6ab4; color:#ffffff;}/* Style the tab content */.tabcontent{display: none; padding: 6px 12px; border: 1px solid #ccc; border-top: none; background-color:#ffffff;}';
    document.head.append(codeSamplesStyle);
    
    $(function () {
        /*******************************
        * The following code contains:
        * Custom Code to create Language tabs
        *
        * Swagger Snippets generator to generate Code Snippets
        * https://github.com/ErikWittern/swagger-snippet
        *
        * Highlight.js to highlight keywords in Code Snippets: https://highlightjs.org/
        * Languages Supported in Swagger-UI in this code: C#, jQuery, php, ruby, nodejs
        ********************************/
        $(document).ready(function () {
            var swaggerSpec = $('#select_document').val();
            if (swaggerSpec !== undefined) {
                $.get(swaggerSpec, function (data) {
                    $('ul.operations > li > .content').each(function (index, item) {

                        var csharpCode = 'C# Code here';
                        var jqueryCode = 'jQuery Code here';
                        var phpCode = 'php Code here';
                        var rubyCode = 'ruby Code here';
                        var nodejsCode = 'nodejs Code here';

                        var endpoint = $(this).parent().find('.path').text().trim();
                        var httpMethod = $(this).parent().find('.http_method').text().trim();
                        try {
                            var result = SwaggerSnippet.getEndpointSnippets(data, endpoint, httpMethod, ['csharp_restsharp', 'javascript_jquery', 'php_http2', 'ruby_native', 'node_native']);
                            var websiteUrl = window.location.protocol.replace(/:/g, '') + "://" + window.location.hostname + ':' + window.location.port;
                            if (result !== undefined && result.snippets[0].content !== undefined) {
                                csharpCode = unescape(result.snippets[0].content.replace('http://undefined', websiteUrl));
                                jqueryCode = unescape(result.snippets[1].content.replace('http://undefined', websiteUrl));
                                phpCode = unescape(result.snippets[2].content.replace('http://undefined', websiteUrl));
                                rubyCode = unescape(result.snippets[3].content.replace('http://undefined', websiteUrl));
                                nodejsCode = unescape(result.snippets[4].content.replace('"hostname": "undefined"', '"hostname": "' + websiteUrl + '"'));
                            }
                        } catch (err) {
                            console.log(err);
                        }
                        var toInsert = $("<div class='codeSamples'><h4>Code Samples: </h4></div>");
                        var codeSampleTabs = toInsert.append('<div class="tab"> <button class="tablinks" onclick="CodeSnippets.openSample(event, \'csharp' + index.toString() + '\')">C#</button> <button class="tablinks" onclick="CodeSnippets.openSample(event, \'javascript_jquery' + index.toString() + '\')">jQuery</button> <button class="tablinks" onclick="CodeSnippets.openSample(event, \'php' + index.toString() + '\')">php</button> <button class="tablinks" onclick="CodeSnippets.openSample(event, \'ruby' + index.toString() + '\')">Ruby</button> <button class="tablinks" onclick="CodeSnippets.openSample(event, \'nodejs' + index.toString() + '\')">Nodejs</button></div><div id="csharp' + index.toString() + '" class="tabcontent"> <h3>C# Code</h3> <p><pre><code class="C#">' + csharpCode + '</code></pre></p></div><div id="javascript_jquery' + index.toString() + '" class="tabcontent"> <h3>JavaScript / jQuery</h3> <p><pre><code class="JavaScript">' + jqueryCode + '</code></pre></p></div><div id="php' + index.toString() + '" class="tabcontent"> <h3>php</h3> <p><pre><code class="php">' + phpCode + '</code></pre></p></div><div id="ruby' + index.toString() + '" class="tabcontent"> <h3>Ruby</h3> <p><pre><code class="ruby">' + rubyCode + '</code></pre></p></div><div id="nodejs' + index.toString() + '" class="tabcontent"> <h3>Nodejs</h3> <p><pre><code class="JavaScript">' + nodejsCode + '</code></pre></p></div>');
                        $(item).append(codeSampleTabs);
                    });
                    jQuery('pre code').each(function (i, block) {
                        hljs.highlightBlock(block);
                    });
                });
            }
        });
    });
}();