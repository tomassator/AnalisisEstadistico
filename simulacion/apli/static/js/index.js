
//DATOS GLOBALES
API_URL = 'http://127.0.0.1:8000'
NROS = [];

function fetchGetText(URL, funcCallback){
    fetch(`${URL}`)
    .then(
        response => response.text()
    ).then(
        html => funcCallback(html)
    );
}

function fetchGetTextForm(URL, idform, funcCallback){
    fetch(`${URL}`, {
        method : "POST",
        body: new FormData(document.getElementById(`${idform}`)),
    }).then(
        response => response.text()
    ).then(
        html => funcCallback(html)
    );
}

//Hace un request para traer el html correspondiente para pasar los parametros
function actualizarDistElegida() {
    var droplist = document.getElementById('selectDistribucion');
    var URL = API_URL + `/${droplist.options[droplist.selectedIndex].value}`;
    fetchGetText(URL, cargarHTMLDistADocument);
}

//esta funcion se ubicara en el callback del request que desvuelva el HTML de la distribucion
function cargarHTMLDistADocument(contHTML){
    document.getElementById("form-distribucion").innerHTML = contHTML;
}

function cargarHTMLResultadoNros(contHTML){
    document.getElementById("content-resultados").innerHTML = contHTML;
}

function configForms(){
    var formDatos = document.querySelector('#formDatos');
    formDatos.addEventListener('submit', event => {
        event.preventDefault();
        // TODO: debe traer el html de los resultados por un lado, y los datos crudos del otro.
        //fetchGetText(API_URL + `/${formDatos.getAttribute("action")}`, cargarHTMLResultadoNros);
        fetchGetTextForm(API_URL + `/${formDatos.getAttribute("action")}`, 'formDatos', cargarHTMLResultadoNros)
    });
}

//TODO: Ver si implementamos el histograma aca o en el HTML
// function cargarHistograma(){
//     Highcharts.chart('container', {
//         chart: {
//             type: 'column'
//         },
//         title: {
//             text: 'Histograma'
//         },
    
//         accessibility: {
//             announceNewData: {
//                 enabled: true
//             }
//         },
//         xAxis: {
//             type: 'category'
//         },
//         yAxis: {
//             title: {
//                 text: 'frecuencias'
//             }
    
//         },
//         legend: {
//             enabled: false
//         },
//         plotOptions: {
//             series: {
//                 borderWidth: 0,
//                 dataLabels: {
//                     enabled: true,
//                     format: '{point.y:.1f}'
//                 }
//             }
//         },
    
//         tooltip: {
//             headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
//             pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b> of total<br/>'
//         },
    
//         series: [
//             {
//                 name: "intervalos",
//                 colorByPoint: true,
//                 data: [
//                     
//                     {% for int in histograma.intervalos%}
//                     {
//                         name: "{{int.0}} - {{int.1}}",
//                         y: {{int.3}},
    
//                     },
//                     {% endfor %}
//                 ]
//             }
//         ],
//     })
// }
configForms();