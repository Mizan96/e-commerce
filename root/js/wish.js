    $(document).ready(function(){
    var productForm = $(".wish-form-product-ajax") // #form-product-ajax
    productForm.submit(function(event){
        event.preventDefault();
        // console.log("Form is not sending")
        var thisForm = $(this)
        // var actionEndpoint = thisForm.attr("action"); // API Endpoint
        var actionEndpoint = thisForm.attr("data-endpoint")
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();
        var currentPath = window.location.href;
        $.ajax({
          url: actionEndpoint,
          method: httpMethod,
          data: formData,
          success: function(data){
            var submitSpan =thisForm.find('.change-div')
            submitSpan.html('')
            if (currentPath.indexOf("details") == -1) {
              if (data.added){
                submitSpan.html('<button type="submit"><p class="small"><i class="fas fa-heart" style="color: red;"></i> </button>')
              } else {
                submitSpan.html('<button type="submit"><p class="small"><i class="far fa-heart" style="color: red;"></i> </p></button>')
               }
            }
            else{
            if (data.added){
              submitSpan.html("<button type='submit' class='btn btn-primary btn-block'>In Wishlist</button>")
            } else {
              submitSpan.html("<button class='btn btn-info btn-block'><i class='far fa-heart add-to-wishlist-button' ></i>Add To Wishlist</button>")
             }
            }
          },
          error: function(errorData){
            console.log("error")
            console.log(errorData)
          }
        })
    })
    
  })