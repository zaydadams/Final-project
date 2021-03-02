function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

//contact form script//

const x =document.getElementById('login');
const y =document.getElementById('register');
const z =document.getElementById('btn');


function register(){
    x.style.display = "none";
    y.style.display = "block"
    x.style.left='400px';
    y.style.left='50px'
    z.style.left='110px'
}
function login(){
    y.style.display = "none";
    x.style.display = "block"
    x.style.left='50px';
    y.style.left='450px'
    z.style.left='0px'
}


const modal = document.getElementById('login-form');
window.onclick = function(event){
    if (event.target == modal){
        modal.style.display ="none";
    }
}

