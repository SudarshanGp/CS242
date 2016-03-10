function test(data){
    console.log(data);
}

function menu(defaultData){
     var search = function(e) {
        var pattern = $('#input-search').val();
        var options = {
            ignoreCase: $('#chk-ignore-case').is(':checked'),
            exactMatch: $('#chk-exact-match').is(':checked'),
            revealResults: $('#chk-reveal-results').is(':checked'),
            enableLinks: true

        };
        var results = $searchableTree.treeview('search', [pattern, options]);

        var output = '<p>' + results.length + ' matches found</p>';
        $.each(results, function(index, result) {
            console.log(result);
            output += '<p>- ' + result.text + '</p>';
        });
        $('#search-output').html(output);
    }

    $('#btn-search').on('click', search);
    $('#input-search').on('keyup', search);

    $('#btn-clear-search').on('click', function(e) {
        $searchableTree.treeview('clearSearch');
        $('#input-search').val('');
        $('#search-output').html('');
    });


    var initSelectableTree = function() {

        return $('#treeview-selectable').treeview({
            data: defaultData,
            multiSelect: $('#chk-select-multi').is(':checked'),
            onNodeSelected: function(event, node) {
                //var data_pass = {name: node.url}
                // $.ajax({
                //     url: '/subversion',
                //     data: JSON.stringify({url: node.url}),
                //     type: 'POST',
                //     contentType: 'application/json;charset=UTF-8',
                //     success: function(response) {
                //         console.log(response);
                //     },
                //     dataType: "json",
                //     error: function(error) {
                //         console.log(error);
                //     }
                // });
                var iframe = $('#code');
                console.log(node.url);
                iframe.attr('src', node.url);
                iframe.attr('height', $(window).height()+'px')
                console.log(node);
                $('#selectable-output').html('<p>' + node.text + ' was selected</p>');
            },
            onNodeUnselected: function(event, node) {
                $('#selectable-output').html('<p>' + node.text + ' was unselected</p>');
            }
        });
    };
    var $selectableTree = initSelectableTree();
    var findSelectableNodes = function() {
        return $selectableTree.treeview('search', [$('#input-select-node').val(), {
            ignoreCase: false,
            exactMatch: false
        }]);
    };
    var selectableNodes = findSelectableNodes();

    $('#chk-select-multi:checkbox').on('change', function() {
        console.log('multi-select change');
        $selectableTree = initSelectableTree();
        selectableNodes = findSelectableNodes();
    });

    // Select/unselect/toggle nodes
    $('#input-select-node').on('keyup', function(e) {
        selectableNodes = findSelectableNodes();
        $('.select-node').prop('disabled', !(selectableNodes.length >= 1));
    });

    $('#btn-select-node.select-node').on('click', function(e) {
        $selectableTree.treeview('selectNode', [selectableNodes, {
            silent: $('#chk-select-silent').is(':checked')
        }]);
    });

    $('#btn-unselect-node.select-node').on('click', function(e) {
        $selectableTree.treeview('unselectNode', [selectableNodes, {
            silent: $('#chk-select-silent').is(':checked')
        }]);
    });

    $('#btn-toggle-selected.select-node').on('click', function(e) {
        $selectableTree.treeview('toggleNodeSelected', [selectableNodes, {
            silent: $('#chk-select-silent').is(':checked')
        }]);
    });
}

