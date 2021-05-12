$(document).ready(function() {
    $('#aparato').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true, // Permite reinicializar la tabla con un proceso
        deferRender: true, // Se usa cuando la tabla tiene mas de 500,000 registros para agilisarla
        "language": {
            url: '/static/lib/spanish.txt'
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action':'searchdata'},
            dataSrc: "" // si se manda el resultado en una variable se tendria que poner aqui la variable pero aqui asi no se manda
        },
        columns: [

        ]
});
});