const ColorBtns = document.querySelectorAll('#button')
console.log(ColorBtns)
// const ColorBtn = document.getElementById('button')

function RandomColorChange(){
    const red = Math.floor(Math.random()*256)
    const green = Math.floor(Math.random()*256)
    const blue = Math.floor(Math.random()*256)
    return `rgb(${red},${green},${blue})`
}
function ChangeBackGround(e){
    console.log(e.target)
    e.target.style.background = RandomColorChange()
}
for(let ColorBtn of ColorBtns){
    ColorBtn.addEventListener('click', ChangeBackGround)
}

const openBtn = document.getElementById('open-btn')
const sidebar = document.querySelector('.sidebar')
function openSidebar(){
    sidebar.classList.add('show')
}
function closeSidebar(){
    sidebar.classList.remove('show')
}

openBtn.addEventListener('click', openSidebar)
sidebar.addEventListener('mouseleave', closeSidebar)

const clock = document.getElementsByClassName('background')

function changeFormat(t){
    return t < 10 ? `0${t}` : t
}
function getTime(){
    const time = new Date()
    const hours = time.getHours()
    const minutes = time.getMinutes()
    const seconds = time.getSeconds()

    clock.innerHTML = `${changeFormat(hours)}:${changeFormat(minutes)}:${changeFormat(seconds)}`
}

setInterval(getTime, 1000)