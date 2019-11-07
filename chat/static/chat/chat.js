$(function () {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + '/ws' + window.location.pathname);

    chatsock.onmessage = function (message) {
        var data = JSON.parse(message.data);
        var chat = $("#chat")
        var ele = $('<tr></tr>')

        ele.append(
            $("<td></td>").text(data.sender_username)
        )
        ele.append(
            $("<td></td>").text(data.message)
        )
        // ele.append(
        //     $("<td></td>").text(data.message)
        // )

        chat.append(ele)
    };

    $("#chatform").on("submit", function (event) {
        var message = {
            sender_id: $('#handle').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
});