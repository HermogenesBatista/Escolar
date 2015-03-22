$(document).ready(function(){

    $('#id_cpf').on('keyup', function(){

        var $vCpf = $(this).val();
        console.log($vCpf);
        $vCpf = $vCpf.replace('.', '');
        $vCpf = $vCpf.replace('-', '');

        console.log($vCpf.length);
        if($vCpf.length >3 || $vCpf.length <6)
        {
            $vCpf = $vCpf.substring(0,4)+'.'+$vCpf.substring(4,6);

        }

    });


})