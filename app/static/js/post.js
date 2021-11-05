<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#cartbutton").on("click", function () {
                var td = $(this).parent("td");
                var id = td.data("id");
                var type = td.data("type");
                sendToServer(id, type);

            });

                                                        function sendToServer(id,type) {
            console.log(id);
                                                            console.log(type);
                                                            $.ajax(
                                                                {
            url: "/menu/addtocart/",
                                                                    type: "POST",
                                                                    data: {
            id: id, type: type
                                                                    },
                                                                })
                                                                .done(function (response) {
            console.log(response);
                                                                })
                                                                .fail(function () {
            console.log("Error Occured");                                                                })
                                                        }
                                                    });

                                                </script>