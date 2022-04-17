
function mostrarContenido() {

    checkIntervalo = document.getElementById("btnintervalo")
    histograma = document.getElementById("container")

    if(checkIntervalo.value == "5"){
        histograma.style.display='flex'
    }

    console.log(checkIntervalo.value)
}
