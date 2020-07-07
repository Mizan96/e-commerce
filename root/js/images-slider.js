var a = document.getElementById('left-image-section');
var b = a.getElementsByTagName('img');

new Vue({
    el: '#left-image-section',
    delimiters: ['[[',']]'],
    data:{
        imageSrc: b[0].getAttribute('src'),
    },
    methods: {
        image1: function(){
            this.imageSrc= b[0].getAttribute('src');
            
        },
        image2: function(){
            this.imageSrc=b[1].getAttribute('src');
        },
        image3: function(){
            this.imageSrc=b[2].getAttribute('src');;
        },
        image4: function(){
            this.imageSrc=b[3].getAttribute('src');;
        },
        image5: function(){
            this.imageSrc=b[4].getAttribute('src');;
        }
    }
    
})

