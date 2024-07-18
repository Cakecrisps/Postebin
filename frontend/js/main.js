document.getElementById('post-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const postContent = document.getElementById('post-content').value;
    const postLifetime = document.getElementById('post-lifetime').value;

    if (!postContent || !postLifetime) {
        alert('Пожалуйста, заполните все поля.');
        return;
    }

    const postListItem = document.createElement('li');
    postListItem.textContent = `Содержание: ${postContent} | Время жизни: ${postLifetime} минут`;

    document.getElementById('posts-list').appendChild(postListItem);

    // Очистить форму после отправки
    document.getElementById('post-form').reset();
});
