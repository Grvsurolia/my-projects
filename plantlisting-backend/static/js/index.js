document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var userName = document.querySelector('#room-name-input').value;
    console.log('userName',userName)
    window.location.pathname = '/chat/' + userName + '/';
};