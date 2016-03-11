/**
 * menu function takes in defaultData that is passed from the template when base.html is rendered and
 * creates the tree node structure and creates takes care of requesting for version information of file through
 * AJAX requests to the flask server
 * @param defaultData Contains information that is used to build the tree node directory structure.
 */
function menu(defaultData) {
    "use strict";
    $('#treeview-selectable').treeview({
        data: defaultData,
        multiSelect: $('#chk-select-multi').is(':checked'),
        onNodeSelected: function(event, node) {
            var type = ""; // Type of object we are looking at
            if (node.tags.length === 2) {
                type = 'DIR';
            } else if (node.tags.length === 4) {
                type = 'FILE';
            }
            $.ajax({ // ajax call for revision data for file is mades
                url: '/info',
                data: JSON.stringify({ // data that is sent to the flask server
                    url: node.url,
                    revision: (node.tags[0].split(':'))[1],
                    name: node.text,
                    type: type
                }),
                type: 'POST',
                contentType: 'application/json;charset=UTF-8',
                success: function (response) { // response that is sent back from the flask server
                    if (response['msg'] === 'YES') {
                        var revisions = response['revisions'];
                        revisions.forEach(function( // iterate through all revision entries and add it to the table
                            entry) {
                            var tr = '<tr> <td>' + entry['_date'] + '</td> <td>' + entry['_author'] +
                                '</td> <td>' + entry['_revision'] + '</td><td>' + entry['_msg'] + '</td></tr>';
                            $('#info').append(tr);});
                    }
                },
                dataType: "json",
                error: function(error) {
                    console.log(error); // log error on invalid ajax request
                }
            });
            var codeFrame = $('#code'); // retrieve iframe that contains the code
            if (type === 'FILE') {
                codeFrame.attr('src', node.url); // load source code of file on iframe
            }
        },
        onNodeUnselected: function(event, node) { // when the node is unselected/another file is selected
            var codeFrame = $('#code');
            codeFrame.attr('src',
                'https://subversion.ews.illinois.edu/svn/sp16-cs242/gvndprs2/Assignment3.0/app/static/welcome.txt'
            ); // clear iframe
            $("#info td").remove(); // clear table containing revision information
        }
    });
}
