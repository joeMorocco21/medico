function readURL(input) {
    if (input.files) {
      var file = document.getElementById("img").files.length;
        console.log(file)
        for (var i = 0; i < file; i++) {
        var reader = new FileReader();
        reader.onload = function (e) {    
          var tr = document.createElement("tr")
          var td = document.createElement("td")
          var imag = document.createElement('img')
          imag.src= e.target.result
          var tbody = document.getElementById("tbimage")
          td.append(imag)
          tr.append(td)
          td.setAttribute('class','tds pt-4')
          tr.setAttribute('class','trs')
          tbody.append(tr)
          var img = e.target.result
        }
        reader.readAsDataURL(input.files[i]);
      }
      
    }
  };
