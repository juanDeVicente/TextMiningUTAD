function get_last_tweets() {
    event.preventDefault();
    document.getElementById('frequency_words_row').innerHTML = '';
    var form = $('#search_form');
    event.preventDefault();
    $.ajax({
        url : form.attr('action'),
        type : form.attr('method'),
        data: form.serialize(),

        success : function (response) {
            document.getElementById('frequency_words_row').innerHTML = response;
        }
    })
}
function delete_last_tweets() {
    document.getElementById('frequency_words_row').innerHTML = '';
    document.getElementById('id_screen_name').value = '';
}