$('document').ready(function(){
    var currentpath;
function refreshCartHome(){
    $.ajax({
        method: 'GET',
        url: '/carts/api/cart/siganl/',
        data:{},
        success: function(data){
            console.log('success yeah');
            window.location.href = currentpath
        },
        error: function(errorData){
            console.log('error');
            console.log(errorData)
        }
    })
}

$('.quantity-form').mouseleave(function(){
    var a = $('.qty-name-id');
    var inStock = $('.in-stock-amount').val();
    var forCart = a.val();
    console.log(forCart,'oi', inStock)
    if (parseInt(forCart) > parseInt(inStock)){
        $('.error-cart-amount').text(inStock + ' in stock')
    }else{
    $.ajax({
        url: '/carts/api/cart/total/',
        data: $(this).serialize(),
        method: 'POST',
        success:function(data){
            console.log('success');
            currentpath = window.location.href
            if (currentpath.indexOf('carts') != -1){
                refreshCartHome()
            }
        },
        error: function(errorData){
            console.log(errorData);
        }
    })
}
})


})
