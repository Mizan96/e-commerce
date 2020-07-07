$('document').ready(function(){
    
    function markedFun2(){
        $('.repeating-body-review p').each(function(){
            var content = $(this);
            content.html('<p>'+ marked(content.text()) +'</p>')
            
        })
    }
    markedFun2();
    
    $('.review-form').submit(function(event){
        event.preventDefault();
        console.log(window.location.href);
        console.log($(this).serializeArray())
        $.ajax({
            url: window.location.href,
            data: $(this).serialize(),
            method: 'POST',
            success: function(data){
                console.log('success');
                console.log(data)
                
                $('.comment-short-list-review').html('');
                $('#id_review').val('');
                $('#id_review_wmd_preview').html('');
                len = data.info.length;
                console.log(len);
                for(i=len-1; i>=0; i--){
                var temp = '<div class="design-question-div-review">'+
                '<div class="container repeating-body-review">'+
                    '<p>' + data.info[i].review +'</p>'+
                '</div>'+
                '<p class="text-right container">By <a href="#">'+ data.info[i].user +'</a> | on '+  data.info[i].updated +'</p>'+
                '</div>'

                    $('.comment-short-list-review').prepend(temp)
                }
                if(data.reviews_count < 2 ){
                    $('.ques-count-div-review').html(data.reviews_count +' Review')
                }
                else{
                    $('.ques-count-div-review').html(data.reviews_count +' Reviews')
                }
                markedFun2()
                    
            },
            error: function(errorData){
                console.log('error');
                console.log(errorData)
            }
        })
    })
});