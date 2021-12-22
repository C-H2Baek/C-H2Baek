const colorBox = document.querySelector('.color-box')
const colorInput = document.getElementById('color-input')
const colorList = document.querySelector('.color-list') // 동적으로 색상 목록을 표시를 하고, 클릭 이벤트 연결

const colors = ['#FFFFFF' , '#000000' , 'orange', 'blue', 'brown', 'green', 'red', 'skyblue']
let index = -1
let prevIndex = -1

function displayColor(colors){
    for(let color of colors){
        const item = `<div class='color-item'>${color}</div>`
        colorList.innerHTML += item
    }
}

function typeColor(e){
    console.log(e.target.value) // 사용자 입력한 문자열

    if(e.target.value !== ''){ // 사용자가 뭔가를 입력했을때
        console.log('you typed something')
        colorList.classList.add('show') // 색상 목록을 디스플레이함
        colorInput.addEventListener('keyup', selectColor)
    }else{ // 아무것도 입력하지 않았을때
        console.log('you didn\'t type anything')
        colorList.classList.remove('show') // 색상 목록을 사라지게 함
        colorInput.removeEventListener('keyup', selectColor)
    }
    
}

function setBackground(color){
    colorInput.value = color // 입력창의 글자가 사용자가 선택한 색상으로 변경됨
    colorList.classList.remove('show') // 자동완성 목록이 사라짐
    colorBox.style.background = color // 배경색 변경
    colorInput.removeEventListener('keyup', selectColor) // 이벤트 제거
}

function setColor(e){
    console.log(e.target)

    if(e.target.className === 'color-item'){
        const pickedColor = e.target.innerText // brown, red
        setBackground(pickedColor) // 배경색 변경
    }
}

function changeHighLightItem(key){
    prevIndex = index // 현재 사용자가 선택한 색상에 대한 인덱스값을 기억(저장)

    if(key === 40){
        index++
        if(index > colors.length -1){
            index = 0
        }
    }else if(key === 38){
        index--
        if(index < 0){
            index = colors.length -1
        }
    }else if(key === 13){
        // TODO :: 배경색 변경 (사용자가 배경색을 선택하면)
        const colorItem = document.querySelectorAll('.color-item')[index]
        setBackground(colorItem.innerText) // 색상이름
    }
}

function unsetHightLightItem(){
    if(prevIndex >= 0){
        const colorItem = document.querySelectorAll('.color-item')[prevIndex]
        colorItem.classList.remove('highlight')
    }
}

function highLightColorItem(){
    if(index >= 0){
        const colorItem = document.querySelectorAll('.color-item')[index]
        colorItem.classList.add('highlight')
    }
}

function selectColor(e){
    console.log(e.keyCode) // 키보기 키에 대한 id 값 

    if(e.keyCode){
        changeHighLightItem(e.keyCode) // 사용자가 선택한 색상에 대한 인덱스 값 변경
        unsetHightLightItem() // 이전 하이라이트 제거
        highLightColorItem() // 사용자가 키로 선택한 색상에 대한 하이라이트 적용
    }
}

displayColor(colors) // 화면에 색상 목록이 나타남

colorInput.addEventListener('input', typeColor)
colorList.addEventListener('click', setColor)