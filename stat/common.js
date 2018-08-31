window.onload = function() {
    console.log( 'Документ и все ресурсы загружены');
    url = '/cgi-bin/get-stats.py';
      
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send(); // (1)
    
    xhr.onreadystatechange = function() { // (3)
      if (xhr.readyState != 4) return;
    
      if (xhr.status != 200) {
        alert(xhr.status + ': ' + xhr.statusText);
      } else {
        mass = xhr.responseText+'';
        var html = `<table> `
        // преобразовываю в массив полученные данные от сервера
        mass = mass.slice(3,mass.length-3).split("), ('");
        // mass = mass.slice(3,mass.length-3);

        // '), (
        
        // mass = mass.replace(/'\)\, \(/g,'|')
        // console.log('START=>'+mass);

        var id = 0;
        mass.forEach(function(el){            

          // id = el.slice(el.indexOf(', '));
          console.log('===>',id)
            console.log(el)
            
            html+="<tr><td><a href='./city/?idcity='>"+el.replace(/', /g,"</a></td><td>")+"</td></tr>";
        });  
        
        html +=`</table>`;

        document.getElementById('table-stat').innerHTML = html;
      }    
    }
  };