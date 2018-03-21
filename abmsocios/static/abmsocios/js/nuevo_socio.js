$(document).ready(function(){    
    $('.ui.small.avatar.image').popup();
    $('.ui .dropdown').dropdown();
    
    $('#perfil').on('click', function(){
        $('#id_foto_perfil').click();
    });
    $("#id_foto_perfil").change(function(){
    readURL(this);
    });


    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#perfil').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }


    $('#crearSocio').form({
        inline: true,
        on: 'blur',
        fields:{
            nombre: {
                identifier: 'nombre',
                rules: [
                    {
                    type: 'empty',
                    prompt: 'Campo requerido.',
                },
                ]
            },
            apellido: {
                identifier: 'apellido',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido.'
                    },
                ]
            },
            documento: {
                identifier: 'documento',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido',
                    },
                    {
                        type: 'integer',
                        prompt: 'Debes ingresar solo numeros.'
                    },
                ]
            },
            nacimiento: {
                identifier: 'fecha_nacimiento',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido'
                    },
                ]
            },
            correo: {
                identifier: 'correo',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido.',
                    },
                    {
                        type: 'email',
                        prompt: 'Ingresa un email valido.',
                    },
                ]
            },
            sexo: {
                identifier: 'sexo',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido.'
                    },
                ]
            },
            fecha_inscripcion: {
                identifier: 'fecha_inscripcion',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Campo requerido.'
                    },
                ]
            }
        }
    });

});


var dateRegex = '^(?:(?:31(\/)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]/\d)?/\d{2})$'
