

const heart = document.querySelector('.heart_btn');
const header = document.querySelector("#header");
const sidebox = document.querySelector(".side_box");

heart.addEventListener('click',function(){
    console.log('hit');
    heart.classList.toggle('on');
});

function resizeFunc(){
    if(pageYOffset>=10){

        // innerWidth 화면의 좌우값 확인
        let calcWidth =(window.innerWidth*0.5)+167;
        console.log(window.innerWidth);

        sidebox.style.left= calcWidth+'px';
    }
}

function scrollFunc(){

    console.log(pageYOffset);
    
    if(pageYOffset>=10){
        header.classList.add("on");
        sidebox.classList.add("on");
        resizeFunc();
    }
    else{
        header.classList.remove("on");
        sidebox.classList.remove("on");
        sidebox.removeAttribute('style');
        }

}

window.addEventListener('scroll',scrollFunc);