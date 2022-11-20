$("form").submit(function () {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    var file = $('#id_file')[0].files[0];

    if (file && file.size > 2 * 1024 * 1024) {
      alert("File " + file.name + " of type " + file.type + " is too big");
      return false;
    }
  }
});

