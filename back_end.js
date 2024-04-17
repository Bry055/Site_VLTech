function WhatsCelular(){

    window.open( 'https://wa.link/fg78j4', '_blank');

}

function WhatsNotebook(){
    window.open( 'https://wa.link/ficdbb', '_blank');
}

function AbreInstagram(){
    window.open( 'https://www.instagram.com/vltech.informatica/', '_blank');
}
   

document.getElementById("celularBtn").addEventListener("click", function() {
    WhatsCelular();
});

document.getElementById("notebookBtn").addEventListener("click", function() {
    WhatsNotebook();
});