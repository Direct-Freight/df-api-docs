var $ = require("jquery");
var openSample = function (evt, sampleName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {        
        $(tabcontent[i]).fadeOut();
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");       
    }
    if (tablinks.length > 0 && tabcontent.length > 0) {
        tablinks[0].className = tablinks[0].className.replace(" active", "");
    }
    $('#' + sampleName).fadeIn();
    evt.currentTarget.className += " active";
}

module.exports = {
    openSample: openSample
}

// The if is only for when this is run from the browser
if (typeof window !== 'undefined') {
    // grab existing namespace object, or create a blank object
    // if it doesn't exist
    var CodeSnippets = window.CodeSnippets || {}

    // define that object
    CodeSnippets = {
        openSample: openSample
    }

    // replace/create the global namespace
    window.CodeSnippets = CodeSnippets
}