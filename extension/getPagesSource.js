function GenericOnClick(document_root) 
{
    var html = '',
        node = document_root.firstChild;
    while (node) {
        switch (node.nodeType) {
        case Node.ELEMENT_NODE:
            html += node.outerHTML;
            break;
        case Node.TEXT_NODE:
            html += node.nodeValue;
            break;
        case Node.CDATA_SECTION_NODE:
            html += '<![CDATA[' + node.nodeValue + ']]>';
            break;
        case Node.COMMENT_NODE:
            html += '<!--' + node.nodeValue + '-->';
            break;
        case Node.DOCUMENT_TYPE_NODE:
            // (X)HTML documents are identified by public identifiers
            html += "<!DOCTYPE " + node.name + (node.publicId ? ' PUBLIC "' + node.publicId + '"' : '') + (!node.publicId && node.systemId ? ' SYSTEM' : '') + (node.systemId ? ' "' + node.systemId + '"' : '') + '>\n';
            break;
        }
        node = node.nextSibling;
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/getNextMove", false);
    xhr.setRequestHeader('Content-type', 'text/plain');
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4) {
          console.log('xhr response: '+ xhr.responseText);
      }
    }
    xhr.send(html);
    return xhr.responseText;
}

chrome.runtime.sendMessage({
    action: "getSource",
    source: GenericOnClick(document)
});