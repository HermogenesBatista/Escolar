$(document).ready(function(){

    $('#id_cpf').on('keyup', function(){

        var $vCpf = $(this).val();
        $vCpf = $vCpf.replace('.', '');
        $vCpf = $vCpf.replace('-', '');

        console.log($vCpf.length);
        if($vCpf.length >3 && $vCpf.length <6)
        {

            $vCpf = $vCpf.substring(0,3)+'.'+$vCpf.substring(3,6);

        }else if($vCpf.length >6 && $vCpf.length <9)
        {
            $vCpf = $vCpf.substring(0,3)+'.'+$vCpf.substring(3,6)+'.'+$vCpf.substring(6,9);
        }else if($vCpf.length >9)
        {
            $vCpf = $vCpf.substring(0,3)+'.'+$vCpf.substring(3,6)+'.'+$vCpf.substring(6,9)+"-"+$vCpf.substring(9,12);
        }

        $(this).val($vCpf);
    });


})