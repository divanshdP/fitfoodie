$(document).ready(function () {
    $("#alertcontainer").hide();
});
$("#submit").click(function (e) {
    $.ajax({
        type: "GET",
        url: '/signup/',
        })
        .done(function (response) {
            console.log(response);
            $('#alertcontainer').show();
        })
        .fail(function () {
            console.log("Error Occured");
        })

});
