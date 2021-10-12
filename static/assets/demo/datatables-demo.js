$(document).ready(function() {
    $('#dataTable').DataTable( {
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por pagina",
            "zeroRecords": "No se encontro nada - disculpa",
            "info": "Mostrando pagina _PAGE_ de _PAGES_",
            "infoEmpty": "Aun no hay registros, porfavor inserte datos...",
            "infoFiltered": "(Filtrado de _MAX_ registros totales)",
            'search': 'Buscar:',
            'paginate': {
                'previous': 'Anterior',
                'next': 'Siguiente'
            }
        }
    } );
} );

