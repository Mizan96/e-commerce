$('document').ready(function(){
        
    var mark = marked($('.product-description').text());
    $('.product-description').html(mark);

   $('.user-rating-div').change(function(){
    //    console.log('You have clicked me');
       var star = $('.rating-form').serializeArray()
       console.log(star)
       $.ajax({
           data: star,
           method: 'POST',
           url: '/rating/api/',
           success: function(data){
               console.log('success');
               console.log(data);
               $('.rating-count-div').html(data.avg_rating +' Rating ('+ data.counter +')')
           },
           error: function(errorData){
               console.log('error');
               console.log(errorData);
           }
       })
   })
});