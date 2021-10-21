var vacio2=""
let errorNameUse="Username must have 6 or more characters"
let erroremailuse="The email entered must be a valid email"
let erroremailuse2="The mail field must not be empty"

function validacion(){
    let Nom = document.getElementById("firstname").value
    document.getElementById("firstname").value = Nom

    let ema = document.getElementById("email1").value
    document.getElementById("email1").value = ema

    if(Nom == "" || Nom.length < 6){
        document.getElementById('idname').innerHTML=errorNameUse
    }

    if(ema.includes('@') && ema.includes('.')){
        document.getElementById('idemail').innerHTML=vacio2
    }else{
        document.getElementById('idemail').innerHTML=erroremailuse
    }

    if(ema == ""){
        document.getElementById('idemail').innerHTML=erroremailuse2
    }
}