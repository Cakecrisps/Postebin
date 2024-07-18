function createPost() {
    var posttext = document.getElementById('code').textContent;
    var time = document.getElementById('time').textContent;
    console.log(time,posttext);
    var xhr = new XMLHttpRequest();

    xhr.open('POST', '/createpost', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    var postData = {
        title: 'Название поста',
        body: 'Текст поста',
        lifetime: time,
    };
    xhr.send(JSON.stringify(postData));
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Пост успешно создан');
            } else {
                console.error('Ошибка при создании поста');
            }
        }
    };
};
