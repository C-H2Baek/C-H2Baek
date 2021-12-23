const box = document.getElementById('box')
const gravity = 3
const FPS = 30 // 초당 프레임 수
const limitBottom = 500 // 지면
const limitLeft = 700
const limitTop = 200 // 점프 높이 제한

let vx = 100
let vy = 0
let isJumping = true
let isDead = false

function down(){
    const topStyle = window.getComputedStyle(box).top // 캐릭터의 y방향
    let top = parseInt(topStyle)

    // 중력에 의해서 캐릭터가 아래로 내려옴
    vy += gravity
    top += vy

    if(!isDead && top >= limitBottom){
        top = limitBottom // 지면 안착
        isJumping = true // 점프 가능여부
    }

    // 실제 화면에서 캐릭터의 y방향 위치가 업데이트
    box.style.top = `${top.toString()}px`
}

const timerId = setInterval(down, 1000/FPS)

function move(e){
    const leftstyle = window.getComputedStyle(box).left
    const topStyle = window.getComputedStyle(box).top
    let left = parseInt(leftstyle)
    let top = parseInt(topStyle)

    if(isDead === true && 700 >= limitBottom){
        alert('문구 게임 종료')
        gravity = 0
        return
    }

    if(e.keyCode === 39){
        box.style.backgroundImage = "url('../../../Images/character_right.png')"
        left += vx // 등속 운동
        if(left > limitLeft){
            isDead = true
            
        }
        //화살표 좌측
    }else if(e.keyCode === 37){
        box.style.backgroundImage = "url('../../../Images/character_left.png')"
        if(left > 0){
            left -= vx
        }
        //캐릭터 점프
    }else if(e.keyCode === 32 || e.keyCode === 38){
        if(isJumping && top >= limitTop){
            vy -= gravity
            top -= vy
        }
        if(vy <= 0){
            isJumping = false
        }
    }
    box.style.left = `${left.toString()}px`
    box.style.top = `${top.toString()}px`
}

window.addEventListener('keydown' , move)