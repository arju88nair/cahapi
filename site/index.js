function doCall() {


    $(".card").fadeOut(500, function() {
        $.ajax({
            url: "http://127.0.0.1:5000/",
            type: 'GET',
            dataType: 'json', //you may use jsonp for cross origin request
            success: function(res) {
                $(".dark-text").text(res[0]['blackCard'])
                $(".light2.card .text").text(res[0]['whiteCard'][0])
                var count = res[0]['whiteCard'].length;
                if (count > 2) {
                    $(".light.card .text").text(res[0]['whiteCard'][1])
                    $(".light.card ").show()

                }

                $(".card").fadeIn(500);


            },
            error: function(err) {
                console.log(err)
            }
        });
    });


};