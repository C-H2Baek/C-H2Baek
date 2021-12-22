const colorBox = document.querySelector('.color-box')
const colorList = document.querySelector('.color-list')
const colorInput = document.getElementById('color-input')

const colors = ['#FFFFFF' , 'orange', 'blue', 'brown', 'green', 'red', 'skyblue', 'white' , 'black']

function addColors(colors){
    for(let color of colors){
        const item = `<div class='color-item'>${color}</div>`
        colorList.innerHTML += item
    }
}

function typeColor(e){
    console.log(e.target.value) // 사용자가 입력한 문자열

    if(e.target.value !== ''){  // 사용자가 뭔가를 입력했을때
        console.log('you typed something')
        colorList.classList.add('show')
    }else{
        console.log('you didn\'t type anything')
        colorList.classList.remove('show')
    }
}

function setColor(e){
    console.log(e.target)

    if(e.target.className === 'color-item'){
        const pickedColor = e.target.innerText
        console.log('you picked color !', pickedColor)
        colorInput.value = pickedColor
        colorList.classList.remove('show')
        colorBox.style.background = pickedColor
    }
}

addColors(colors)
colorInput.addEventListener('input', typeColor)
colorList.addEventListener('click', setColor)