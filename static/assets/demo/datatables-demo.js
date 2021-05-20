// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    "language": {
            url: '/static/lib/spanish.txt' // si encuentra el documento pero por alguna razon no funciona
        },
  });
});
