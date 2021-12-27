const box = document.getElementById('box') // 캐릭터
const gravity = 1 // 중력가속도
const FPS = 60 // 프레임수
const limitBottom = 500 // 그라운드(땅) 위치
const limitLeft = 700 // 낭떠러지 위치
const jumpHeight = 30 // 점프 높이


let vx = 20 // x 방향 속도
let vy = 0 // y 방향 속도
let isJumping = false // 점프가능 여부
let isDead = false // 캐릭터 죽음 여부
let jumpKey = false // 점프키 활성화 여부

// 점프하다가 vy 가 jumpHeight 보다 커지면 jumpKey 가 false 가 되면서 더이상 아래로 떨어지지 않고 그라운드(땅)에 정지함
// 중력은 계속 작용하니까 중력에 의해서 아래로 내려오다가 limitBottom 에 닿으면 isJumping 이 true 가 되면서 점핑이 가능하게 됨
// 슈퍼 마리오가 limitLeft 값을 넘어가면, 즉, 땅을 벗어나면 죽었으므로 isDead 가 true 가 되고 isDead 가 true 이면 계속 아래로 떨어짐

// 점프 높이에 영향을 주는 요소 : transition duration, jumpHeight, FPS

function down(){
    // 캐릭터 y 방향 위치 조회
    const topStyle = window.getComputedStyle(box).top
    let top = parseInt(topStyle)


    // 캐릭터 아래로 내려오게 하기 (중력가속도에 의한 가속도 운동)
    vy += gravity
    top += vy

    // 점프했다가 그라운드(땅)에 다시 내려오는 순간 그라운드(땅)에 정지시키기
    if(vy >= jumpHeight){
        jumpKey = false
    }
    
    // 게임 종료
    if(isDead && top > limitBottom + 700){
        alert('Game over !')
        clearInterval(timerId)
    }

    console.log('속도', vy)

    // 그라운드(땅)에 정지시키기
    if(!isDead && !jumpKey && top >= limitBottom){
        top = limitBottom // 캐릭터 위치 고정하기
        isJumping = true // 점프 활성화
        vy = 0 // y 방향 속도 초기화
    }

    // 화면에서 캐릭터 y 방향 위치 변경
    box.style.top = `${top.toString()}px`
}

// 지속적인 애니메이션 실행
const timerId = setInterval(down ,1000/FPS)


// 캐릭터 이동시키기
function move(e){
   
    // 캐릭터 x 방향 위치 조회
    const leftStyle = window.getComputedStyle(box).left
    let left = parseInt(leftStyle)

    // 캐릭터 y 방향 위치 조회
    const topStyle = window.getComputedStyle(box).top
    let top = parseInt(topStyle)

    // 화살표 우측키를 누른 경우
    if(e.keyCode === 39){
        box.style.backgroundImage = "url('super-mario-right.jpg')"; // 캐릭터 이미지 변경
        left += vx // 캐릭터 우측으로 이동
        if(left > limitLeft){ // 그라운드(땅)을 벗어난 경우
            isDead = true // 캐릭터 사망
        }
    }
    // 화살표 좌측키를 누른 경우
    else if(e.keyCode === 37){
        box.style.backgroundImage = "url('super-mario-left.jpg')"; // 캐릭터 이미지 변경
        if(left > 0){ // 윈도우 화면의 좌측 경계를 벗어나지 않은 경우
            left -= vx // 캐릭터 좌측으로 이동
        }
    }
    // 스페이스바나 화살표 위쪽키를 누른 경우
    else if(e.keyCode === 32 || e.keyCode === 38){
        if(isJumping){ // 그라운드(땅) 위에 있는 경우
            vy = -jumpHeight // 점프 가능하도록 y 방향 속도의 방향을 변경함
            isJumping = false // 점프 비활성화
            jumpKey = true // 그라운드(땅)에서 점프함
        }
    }

    box.style.left = `${left.toString()}px` // 캐릭터 x 방향 위치 변경
    box.style.top = `${top.toString()}px` // 캐릭터 y 방향 위치 변경
}
window.addEventListener('keydown', move)