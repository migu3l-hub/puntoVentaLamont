$.noConflict();
$(document).ready(function() {
    $('#aparato').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true, // Permite reinicializar la tabla con un proceso
        deferRender: true, // Se usa cuando la tabla tiene mas de 500,000 registros para agilisarla
        "language": {
            url: '/static/lib/spanish.txt' // si encuentra el documento pero por alguna razon no funciona
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action':'searchdata'},
            dataSrc: "" // si se manda el resultado en una variable se tendria que poner aqui la variable pero aqui asi no se manda
        },
        columns: [
            {"data":"id"},
            {"data":"tipo"},
            {"data":"nombre"},
            {"data":"descripcion"},
            {"data":"precio_venta"},
            {"data":"stock"},
            {"data":"stock"}, // botones
        ],
        columnDefs: [
            {
                targets: [-1], // Ultima columna la de los botones
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) { // row hace referencia al objeto por eso se puede obtener el id
                    var buttons = '<a href="/global/eliminar_aparato/'+row.id+'/" class="btn btn-danger btn-xs"><i class="fa fa-trash"></i></a>  ';
                    buttons += '<button type=button onclick=abrir_modal_edicion("/global/editar_aparato/'+row.id+'/") class="btn btn-warning btn-xs"><i class="fa fa-pencil" aria-hidden="true"></i></button>'; // mucho cuidado con las comillas dobles todas deben estar encendidas por pycharm lo que significa que estan activas
                    return buttons;
                }
            }
        ],
        initComplete: function (settings, json) {
            console.log("Tabla cargada con exito");
        }
});
});


function abrir_modal_edicion(url){
    var $ = jQuery.noConflict();
    $('#edicion').load(url, function (){
      $(this).modal('show');
    });
  }

function abrir_modal_creacion(url) {
    var $ = jQuery.noConflict();
    $('#creacion').load(url, function () {
        $(this).modal('show');
    });
}