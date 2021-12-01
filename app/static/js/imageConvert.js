$(document).ready(function(e){
    $('#imgSub').on('click', function(){
        var form_data = new FormData();
        var ins = document.getElementById('img').files.length;
        if(ins== 0){
            $('#msg').html('<span>no files to upload</span>')
            return;
        }
        for (let x = 0; x < ins; x++) {
            form_data.append("file[]", document.getElementById('img').files[x])
            
        $.ajax({
            url: '/storImages',
            type : 'POST',
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            success: function(response){
                for (var i = 0; i < response.length ; i++)
                {
                var pred = `${response[i][0]}` 
                    var tr = document.createElement("tr")
                    var td = document.createElement("td")
                    var p = document.createElement('p')
                    var tbody = document.getElementById("tbpredict")
                    p.innerHTML= pred
                    td.append(p)
                    tr.append(td)
                    td.setAttribute('class','tds pt-5')
                    tr.setAttribute('class','trs')
                    tbody.append(tr)
                }
            },
 
        });
    }
    });
});
