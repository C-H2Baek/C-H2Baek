function popup(){
    alert('팝업창')
}
function setBtnColor(){
    popupBtn.style.background = 'skyblue'
}
function unsetBtnColor(){
    popupBtn.style.background = ''
}

const popupBtn = document.getElementById('popup')
popupBtn.addEventListener('click', popup)
popupBtn.addEventListener('mouseover', setBtnColor)
popupBtn.addEventListener('mouseout', unsetBtnColor)