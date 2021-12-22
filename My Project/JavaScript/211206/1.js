const photos = document.getElementById('photos')
const photoItems = photos.querySelectorAll('.photo')
const options = document.querySelectorAll('.options')
const selection = document.getElementById('selection')

let cnt = 0
let timerID = null
let prevOption = 0 // 이전에 늘어났던 동그라미의 인덱스 값





function changePosition(){
    const photoItems = document.querySelectorAll('.photo')
    console.log(photoItems)
    cnt = cnt === photoItems.length - 1 ? 0 : cnt + 1
    photos.style.marginLeft = cnt * -500 + 'px'

    //셀렉터 구현
    options[prevOption].style.width = 20 + 'px' //이전 인덱스값으로 동그라미의 길이를 초기화
    options[cnt].style.width = 50 + 'px'
    options[cnt].style.borderRadius = '5px'
    prevOption = cnt // 현재 인덱스값을 지정함
}

function startCarousel(){
    console.log('mouse entered!')
    timerID = setInterval(changePosition, 1000)
}
function stopCarousel(){
    clearInterval(timerID)
}
function changePhoto(e){
    console.log(e.target)
    const target = e.target
    if(target.className === 'options'){
        // 버튼 클릭한 경우
        console.log(target.id)
        cnt = parseInt(target.id) - 1
        changePosition()
    }
}
photos.addEventListener(setInterval(changePosition, 5000))
photos.addEventListener('mouseenter', startCarousel)
photos.addEventListener('mouseleave', stopCarousel)

selection.addEventListener('click', changePhoto)