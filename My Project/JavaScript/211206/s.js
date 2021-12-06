const boxes = document.querySelectorAll('.box')
let index = 0
let preIndex = 0

function moveUp(){
    boxes[preIndex].style.marginTop = 0 +'px'
    boxes[index].style.marginTop = -50 +'px'
    preIndex = index

    index = index === boxes.length - 1 ? 0 : index + 1

}

function startMove(){
    setInterval(moveUp, 1000)
}

window.addEventListener('load', startMove)