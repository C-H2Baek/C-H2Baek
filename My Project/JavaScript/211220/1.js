const colorBox = document.querySelector('.color-box')
const colorInput = document.getElementById('color-input')
console.log(colorInput)

function setColor(e){
    console.log(e.target.value)
    colorBox.style.backgroundColor = e.target.value
}

colorInput.addEventListener('input', setColor)