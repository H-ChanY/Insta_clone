

const header = document.querySelector("#header");
const sidebox = document.querySelector(".side_box");
const variableWidth = document.querySelectorAll('.contents_box .contents');
const delegation = document.querySelector('.contents_box');




heart.addEventListener('click',function(){
    console.log('hit');
    heart.classList.toggle('on');
});

function delegationFunc(e){
    
    let elem =e.target;
    console.log(elem); // target이면 

    while(!elem.getAttribute('data-name')){
        elem=elem.parentNode;

        if(elem.nodeName ==='BODY'){
            elem= null;
            return;
        }
    }

    if(elem.matches('[data-name="heartbeat"]')){

        console.log('하트');
    }else if(elem.matches('[data-name="bookmark"]')){

        console.log('북마크!');
    }else if(elem.matches('[data-name="share"]')){

        console.log('공유!');
    }else if(elem.matches('[data-name="more"]')){

        console.log('더보기!');
    }

    elem.classList.toggle('on');
}



function resizeFunc(){

    console.log('resize!!');
    if(pageYOffset>=10){

        // innerWidth 화면의 좌우값 확인
        let calcWidth =(window.innerWidth*0.5)+167;
        console.log(window.innerWidth*0.5);

        sidebox.style.left= calcWidth+'px';
    }

    if(matchMedia('screen and (max-width : 960px)').matches){

        for(let i=0; i<variableWidth.length;i++){
            variableWidth[i].style.width = window.innerWidth -20 +'px';
        }
    }else{
        for(let i=0; i<variableWidth.length;i++){
            if(window.innerWidth>600){
                variableWidth[i].removeAttribute('style');

            }
        }
    }
}

function scrollFunc(){

    console.log(pageYOffset);
    
    if(pageYOffset>=10){
        header.classList.add("on");

        if(sidebox){
            sideboxbox.classList.add('on');
        }
        resizeFunc();
    }
    else{
        header.classList.remove("on");
        if(sidebox){
            sidebox.classList.remove("on");
            sidebox.removeAttribute('style');
        }
        }

}



setTimeout(function() {
    scrollTo(0,0);
}, 100);

if(delegation){
    delegation.addEventListener('click',delegationFunc)
}

window.addEventListener('resize',resizeFunc);
window.addEventListener('scroll',scrollFunc);