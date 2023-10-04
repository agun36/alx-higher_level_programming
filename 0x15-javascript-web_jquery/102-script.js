$(() => {
  $('#btn_translate').click(() => {
    $.get(
      'https://www.fourtonfish.com/hellosalut/?lang=' +
        $(`#language_code`).val(),
      (data) => {
        $('#hello').text(data.hello)
      }
    )
  })
  $('#language_code').keypress((e) => {
    if (e.which == 13) {
      $.get(
        `https://www.fourtonfish.com/hellosalut/?lang=` +
          $('#language_code').val(),
        (data) => {
          $('#hello').text(data.hello)
        }
      )
    }
  })
})
