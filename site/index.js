function doCall() {


    $(".dark").fadeOut(500, function() {
        $.ajax({
            url: "http://127.0.0.1:5000/",
            type: 'GET',
            dataType: 'json', //you may use jsonp for cross origin request
            success: function(res) {

                $(".dark-text").text(res[0]['blackCard'])
            },
            error: function(err) {
                console.log(err)
            }
        });
        $(".dark").fadeIn(500);
    });


};