$(document).ready(function() {
    var groupColumn = 2;
    var table = $('#index-table').DataTable({
        "ajax": '/json/',
        "columnDefs": [
            { "visible": false, "targets": [2] }
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
        "search": {
        "search":  localStorage.getItem("search")
        },
        columnDefs: [{
		"render": function(data, type, row) {

			return(data === false ? "<span class='text-danger'>DOWN</span>" : "<span class='text-success'>UP</span>");
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

    $(document).on('click', '.start-proxy ', function(){
    $this = $(this);
    $.get(`/start/${$this.data('id')}/`, function(data, textStatus, xhr) {
    if (data.status === true) {
        $this.parent().parent().prev().html("<span class='text-success'>UP</span>")
    }
    else {
        $this.parent().parent().prev().html("<span className='text-danger'>DOWN</span>")
    }
    }, 'json');

  });
    $(document).on('click', '.stop-proxy ', function(){
    $this = $(this);
    $.get(`/stop/${$this.data('id')}/`, function(data, textStatus, xhr) {
    if (data.status === true) {
        $this.parent().parent().prev().html("<span class='text-danger'>DOWN</span>")
    }

    }, 'json');

  });
        function update() {

        setTimeout(function() {
            table.ajax.reload(null, false);
            update();
        }, 5000);
    }

    update();

$(`.dataTables_filter input[type="search"]`).keyup(function(e){
localStorage.setItem("search", $(this).val());
console.log($(`.dataTables_filter input[type="search"]`).val());
});
});
