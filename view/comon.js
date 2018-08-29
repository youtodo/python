window.onload = function() {
    console.log( 'Документ и все ресурсы загружены');
    url = '/cgi-bin/get-comments.py';
      
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
        mass = mass.slice(2,mass.length-4).split("'), (");
        // mass = mass.slice(2,mass.length-3);

        // '), (
        
        // mass = mass.replace(/'\)\, \(/g,'|')
        console.log('START=>'+mass);

        var id = 0;
        mass.forEach(function(el){            
            id = el.slice(0,el.indexOf(','));
            el = el.slice(el.indexOf(',')+3);
            
            
            html+="<tr><td><input type=radio name=idcomment value="+id+">"+el.replace(/', '/g,"</td><td>")+"</td></tr>";
        });  
        
        html +=`</table>`;

        document.getElementById('table-comments').innerHTML = html;
      }    
    }
  };