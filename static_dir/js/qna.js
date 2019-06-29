$('document').ready(function(){
    function markedFun(){
        $('.repeating-body p').each(function(){
            var content = $(this);
            content.html('<p>'+ marked(content.text()) +'</p>')
            console.log('You are calling me')
            
        })
    }
    markedFun();
    $('.q-and-a-form').submit(function(event){
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
                
                $('.comment-short-list').html('');
                $('#id_question').val('');
                $('#id_question_wmd_preview').html('');
                len = data.info.length;
                console.log(len);
                for(i=len-1; i>=0; i--){
              

                    var temp = '<div class="design-question-div">'+
                    '<div class="container repeating-body">'+
                        '<p>' + data.info[i].question + '</p>'+
                    '</div>' +
                    '<p class="text-right container">By <a href="#">'+ data.info[i].user + '</a> | on ' + data.info[i].updated + '</p>'+
                    '</div>'


                    $('.comment-short-list').prepend(temp)
                }
                if(data.ques_count < 2 ){
                    $('.ques-count-div').html(data.ques_count +' Question')
                }
                else{
                    $('.ques-count-div').html(data.ques_count +' Questions')
                }
                markedFun()
                    
            },
            error: function(errorData){
                console.log('error');
                console.log(errorData)
            }
        })
    })
});