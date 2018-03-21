//  Busqueda ajax

$('#busqueda').keyup(function(event) {
    $('#content').dimmer('show');
    var p = $(this).val();
    $('.ui .dimmer').html(
        '<div class="content"><div class="center"><h1 class="busquedaHeader" style="color:white">'+ p + '</h1>'+
        '<table class="ui very basic inverted selectable table"><tbody id="resultadosBusqueda">'+
        '</tbody></table></div></div>'
    );
    if (p === ""){
        $('#content').dimmer('hide');
    } else {
        var url = "http://127.0.0.1:8000/buscar/" + p,
            timeout = null;
        $.getJSON( url, function( data ){
            $.each( data, function(key, val) {
                $('#resultadosBusqueda').append(
                    '<tr><td>' + val.numero_socio + '</td><td><a href="http://127.0.0.1:8000/socio/' + val.documento + ' "> ' +
                     val.nombre + '</a></td><td>' + val.apellido + '</td><td>' + val.habilitacion + '</td></tr>'
                );
            });
        }); 
    }
});

// Sidebar submenus accordion

$('.ui.vertical.accordion')
    .accordion();

// Sidebar on mobile

$('.ui.left.sidebar')
    .sidebar('setting', 'transition', 'overlay')
    .sidebar('attach events', '#sidebar-button', 'toggle');

// Fixed header 

$('#responsive-menu')
    .visibility({
        type: 'fixed',
        offset: 15,
});

// Contador Dashboard

$('.value').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 1500,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});



