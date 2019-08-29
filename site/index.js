function doCall() {


    // $(".dark").fadeOut();
    $.ajax({
        url: "http://127.0.0.1:5000/",
        type: 'GET',
        dataType: 'json', //you may use jsonp for cross origin request
        success: function(res) {
            $(".dark").text(Math.random())
            $(".dark").fadeIn();

            console.log(res[0]['blackCard']);
        },
        error: function(err) {
            console.log(err)
        }
    });
};