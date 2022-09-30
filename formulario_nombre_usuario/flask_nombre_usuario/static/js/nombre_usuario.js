var input_username
var input_email


//no importa el orden de declaracion de los funciones de js
//porque se aplica hoisting de las funciones

//cuando cargue l apgina entonces se llena la tabla de datos
window.onload = function()
{
    input_username = document.getElementById("username")
    input_email = document.getElementById("email")

    getall_PostDict()
}

function llenar_tabla(data){
    var table = document.getElementById("myTable").getElementsByTagName("tbody")[0];
    var largo_tabla = table.rows.length;


     for (var i = 0; i <= data['data_json'].length-1 ; i++)
     {
       var fila = table.insertRow(largo_tabla);
       var celda1 = fila.insertCell(0);
       var celda2 = fila.insertCell(1);
       celda1.innerHTML = data['data_json'][i]['username'];
       celda2.innerHTML = data['data_json'][i]['email'];
     }
}

function agregar_registro_tabla(data){
     var table = document.getElementById("myTable");
     var largo_tabla = table.rows.length;

        var fila = table.insertRow(largo_tabla);
        var celda1 = fila.insertCell(0);
        var celda2 = fila.insertCell(1);
        celda1.innerHTML = data['data_respuesta_json'][0]['username'];
        celda2.innerHTML = data['data_respuesta_json'][0]['email'];
        input_username.value = "";
        input_email.value = "";
}


function getall_PostDict() {
    //Se llama a un fetch para llenar la tabla en la ruta raiz
    fetch("/getall")
    .then(response => response.json() )
    .then(coderData => llenar_tabla(coderData))
    .catch(err => console.log(err) )
}



function save_PostDict() {

    // var input_username = document.getElementById("username")
    // var input_email = document.getElementById("email")

         if (confirm("Desea agregar el usuario" + input_username.value + "a la base de datos via Json Dict?"))
         {
            //se envia la informacion del prompt via ajax usando fetch
            //se arma una variable json tipo objeto dict
            //al no usar un form el body se reemplaza de form por un objeto
            let data = {
                "username": input_username.value,
                "email"   : input_email.value
            }

            //se ejecuta el fetch de tipo POST y la promesa
            fetch("/agregarusuariojsondict", {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body":  JSON.stringify(data),
                }).then(function(response){
                 return response.json()
                }).then(function(data){
                 agregar_registro_tabla(data);
                 return console.log(data);
                });
         }

}


