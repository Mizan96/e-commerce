$('document').ready(function(){
    $('#id_search').keyup(function(){    
        $.ajax({
            url: '/search/',
            data: $('.search-form-ajax').serialize(),
            method: 'POST',
            success: function(data){
                console.log(data);
                console.log('success')
                $('.result-of-form').html('')
                $.each(data.result, function(index, obj){
                    var temp = "<div class='container' style='border:1px solid #ccc;>"+
                    "<div class='row'><a  class='small' href='/products/product/"+ obj.id +"'>"+ obj.title +
                    "</a><img src='"+ obj.image +"' width='50px' heigth='50px' ><div></div>"
                    $('.result-of-form').prepend(temp)
                })
            },
            error: function(errorData){
                console.log('errror')
                console.log(errorData)
            }
        })
    });

    $('body').click(function(){
        $('.result-of-form').html('');
        console.log('Hello World')
    })
});

