var vacio1=""
let errorNameVi="Username must have 6 or more characters"
let errorproducto="The product must have 6 or more characters"
let erroremailvi="The email must be valid"
let erroremailvi2="The email field must not be empty"
let errornumero="The contact number must have from 10 to maximum 12 digits"
let errornumero2="The contact number field must not be empty"


function validacionpro(){
    let Nom3 = document.getElementById("name3").value
    document.getElementById("name3").value = Nom3

    let prod = document.getElementById("producto").value
    document.getElementById("producto").value = prod

    let ema3 = document.getElementById("email3").value
    document.getElementById("email3").value = ema3

    let nume = document.getElementById("numero").value
    document.getElementById("numero").value = nume


    if(Nom3 == "" || Nom3.length < 6){
        document.getElementById('idname3').innerHTML=errorNameVi
    }

    if (prod=="" || prod.length<6){
        document.getElementById('idproducto').innerHTML=errorproducto
    }

    if(ema3.includes('@') && ema3.includes('.')){
        document.getElementById('idemail3').innerHTML=vacio1
    }else{
        document.getElementById('idemail3').innerHTML=erroremailvi
    }

    if(ema3 == ""){
        document.getElementById('idemail3').innerHTML=erroremailvi2
    }

    if (nume.length < 10 || nume.length>12){
        document.getElementById('idnumero').innerHTML=errornumero
    }

    if (nume==""){
        document.getElementById('idnumero').innerHTML=errornumero2
    }
}