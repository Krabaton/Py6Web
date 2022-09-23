let protocol = null

if (window.location.protocol === 'http:') {
    protocol = 'ws://'
} else {
    protocol = 'wss://'
}

socket = new WebSocket(protocol + window.location.host + '/ws');

// событие происходит при присоединении к чату
socket.onopen = (e) => {
    console.log('Hello WebSocket!')
}

socket.onmessage = (e) => {
    console.log(e.data)
    text = e.data
    $('.chat').append(`<div class="users__item">${text}</div>`)
}

$(function () {
    // событие отправки сообщения с формы
    $('.msg')
        .on('submit', function (e) {
            e.preventDefault();
            const message = $('#msg').val();
            $('#msg').val('');
            socket.send(message); // socket.emit('message', message)
        });
    // можем отправить нажатием клавиши
    $('#msg').on('keypress', function (e) {
        if (e.which === 13) {
            $('.msg').submit();
            e.preventDefault();
        }
    });
});