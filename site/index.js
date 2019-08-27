function doCall() {
    $.ajax({
        url: "/",
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            console.log(res);
            alert(res);
        },
        error: function(err) {
            console.log(err)
        }
    });
};