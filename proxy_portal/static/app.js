$(document).ready(function() {
    var groupColumn = 2;
    var table = $('#index-table').DataTable({
        "columnDefs": [
            { "visible": false, "targets": groupColumn }
        ],
        "bInfo" : false,
        //"bLengthChange" : false,
        "order": [[ groupColumn, 'asc' ]],
        "pageLength": 50,
        "lengthMenu": [[50, 75, 100, -1], [50, 75, 100, "All"]],
        "columns": [
            null,
            null,
            {"width": "0px"},
            null,
            {"width": "120px"},
            {"width": "120px"},
            null,
            null,
        ],
        columnDefs: [{
		"render": function(data, type, row) {
			return(data == 'False' ? "<span class='text-danger'>DOWN</span>" : "<span class='text-success'>UP</span>");
		},
		"targets": 6
	}],
        "displayLength": 25,
        "drawCallback": function ( settings ) {
            var api = this.api();
            var rows = api.rows( {page:'current'} ).nodes();
            var last=null;

            api.column(groupColumn, {page:'current'} ).data().each( function ( group, i ) {
                if ( last !== group ) {
                    $(rows).eq( i ).before(
                        '<tr class="group"><td colspan="10">'+group+'</td></tr>'
                    );

                    last = group;
                }
            } );
        }
    } );
$('#start_date_input, #stop_date_input').inputmask('datetime', {
        mask: "1.2.y h:s",
        alias: "dd.mm.yyyy",
        placeholder: "ДД.ММ.ГГГГ ЧЧ:ММ",
        separator: '.',
        hourFormat: "24",
        leapday: "29.02."
    });
    // Order by the grouping
    $('#index-table tbody').on( 'click', 'tr.group', function () {
        var currentOrder = table.order()[0];
        if ( currentOrder[0] === groupColumn && currentOrder[1] === 'asc' ) {
            table.order( [ groupColumn, 'desc' ] ).draw();
        }
        else {
            table.order( [ groupColumn, 'asc' ] ).draw();
        }
    } );
} );
