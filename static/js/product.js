var vacio=""
let errorNamePro="The product name must have more than 6 characters"
let errorminimopro="the stock minimum must be greater than or equal to 1"
let errorminimopro2="the stock minimum is required"


function validacionmin(){
    let Nom1 = document.getElementById("name2").value
    document.getElementById("name2").value = Nom1

    let min = document.getElementById("minimo").value
    document.getElementById("minimo").value = min

    if(Nom1 == "" || Nom1.length < 6){
        document.getElementById('idname2').innerHTML=errorNamePro
    }

    if(min<1){
        document.getElementById('idminimo').innerHTML=errorminimopro
    }

    if(min == ""){
        document.getElementById('idminimo').innerHTML=errorminimopro2
    }
}