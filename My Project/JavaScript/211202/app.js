// 인라인 방식
// function popup(){
//     alert('팝업창')
// }

// 프로퍼티 방식 클릭 이벤트
// const popup = document.getElementById('popup')
// console.dir(popup)
// popup.onclick = function(){
//     alert('팝업창')
// }

// const popupBtn = document.getElementById('popup')
// popupBtn.addEventListener('click', function(){
//     alert('팝업창')
// })

// function popup(){
//     alert('팝업창')
// }
// const popupBtn = document.getElementById('popup')
// popupBtn.addEventListener('click', popup)

// function popup(){
//     alert('팝업창')
// }
// function setBtnColor(){
//     popupBtn.style.background = 'pink'
// }
// function unsetBtnColor(){
//     popupBtn.style.background = ''
// }
// const popupBtn = document.getElementById('popup')
// popupBtn.addEventListener('click', popup)
// popupBtn.addEventListener('mouseover', setBtnColor)
// popupBtn.addEventListener('mouseout', unsetBtnColor)

// function popup(){
//     alert('팝업창')
//     popupBtn.removeEventListener('click', popup)
// }
// const popupBtn = document.getElementById('popup')
// popupBtn.addEventListener('click', popup)

// function popup(evt){
//     console.log(evt) // 이벤트 객체
//     console.log(evt.target)
//     const targetStyle = evt.target.style
  
//     targetStyle.all = 'unset'
//     targetStyle.position = 'absolute'
//     targetStyle.left = '500px'
//     targetStyle.width = '200px'
//     targetStyle.height = '70px'
//     targetStyle.textalign = 'center'
//     targetStyle.background = 'skyblue'
//     targetStyle.borderRadius = '50%'
//     targetStyle.transition = 'all ease 2.5s'
    
// }
// const popupBtn = document.getElementById('popup')
// popupBtn.addEventListener('click', popup)

// function popup(e){
//     const target = e.target
//     target.classList.add('circle')
// }

// const popupBtn = document.querySelector('.popup')
// popupBtn.addEventListener('click', popup)

// const form = document.querySelector('form')
// const id = document.getElementById('user-id')
// const password = document.getElementById('user-password')
// const p = document.querySelector('p')

// function login(e){
//     console.log(id.value,password.value)
//     if(id.value === '' || password.value === ''){
//         e.preventDefault()
//         p.innerText = '입력되지 않음'
//     }else{
//         alert('login is processing ...')
//     }
// }

// form.addEventListener('submit', login)

// Show,hide
// const instantMsg = document.querySelector('.instant-msg')
// function showMsg(){
//     instantMsg.classList.add('show')
// }
// function hideMsg(){
//     instantMsg.classList.remove('show')
// }
// setTimeout(showMsg, 1000)
// setTimeout(hideMsg, 3000)

// Time
// const clock = document.getElementById('clock')
// function changeFormat(t){
//     return t < 10 ?`0${t}` : t
// }

// //getTime: 현재 시각을 가져옴
// function getTime(){
//     const time = new Date()
//     const hours = time.getHours()
//     const minutes = time.getMinutes()
//     const seconds = time.getSeconds()
//     clock.innerText = `${changeFormat(hours)}:${changeFormat(minutes)}:${changeFormat(seconds)}`
// }
// setInterval(getTime, 1000)
// ////
const circle = document.getElementById('circle')
function moveCircle(e){
    console.log(e.clientX, e.clientY)
    const mouseX = e.clientX
    const mouseY = e.clientY
    circle.style.left = mouseX + 'px'
    circle.style.top = mouseY + 'px'
}
window.addEventListener('mousemove', moveCircle)

// const ledContainer = document.getElementById('led-container')
// const leds = document.querySelectorAll('.led')
// function lighton(e){
//     // led 스타일 변경
//     console.log(e.target)
//     console.log(e.target.className)
//     if(e.target.className === 'led'){
//         e.target.classList.add('on')
//     }
// }
// function lightoff(e){
//     console.log(e.target.className)
//     if(e.target.className ==='led on'){
//         e.target.classList.remove('on')
//     }   
// }

// ledContainer.addEventListener('mouseover', lighton)

// for(let led of leds){
//     led.addEventListener('mouseleave', lightoff)
// }
// ////

// let index = 0

// function lightoff(){
//     const led = document.querySelectorAll('.led')[index]
//     led.classList.remove('on')
// }
// function lighton(){
//     const led = document.querySelectorAll('.led')[index]
//     led.classList.add('on')
//     index++

//     if (index > 2){
//         index = 0
//     }
//     setTimeout(lightoff, 1000)
// }
// function startEffect(){
//     console.log('load')
//     setInterval(lighton, 1000)
// }
// window.addEventListener('load', startEffect)

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