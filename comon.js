var mass = '';
var getCity = function (val){
    console.log(val);
    url = '/cgi-bin/get-citys.py?idregion='+val
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send(); // (1)
    
    xhr.onreadystatechange = function() { // (3)
      if (xhr.readyState != 4) return;
    
      if (xhr.status != 200) {
        alert(xhr.status + ': ' + xhr.statusText);
      } else {
        mass = xhr.responseText+'';

        // преобразовываю в массив полученные данные от сервера
        mass = mass.slice(3,mass.length-5).split("',), ('");
        
        var select_city = `<select class='inputs'  name='city' >
                <option value='' disabled selected>Выберите город</option>`
        i=1;
        mass.forEach(function(el){
            console.log(el);
            select_city+= "<option value='"+i+"'>"+el+"</option>"
            i++;
        });                
        select_city +="</select>";
        document.getElementById('el-city').innerHTML = select_city + '<br>';
        
        



      }    
    }

}
