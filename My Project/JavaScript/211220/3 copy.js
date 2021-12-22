const colorBox = document.querySelector('.color-box')
const colorInput = document.getElementById('color-input')

function RandomColor(){
    return Math.floor(Math.ramdom()*256)
}

function setColor(e){
    colorBox.style.backgroundColor = `rgb(${RandomColor()}, ${RandomColor()}, ${RandomColor()})`    
}

colorInput.addEventListener('input', setColor)