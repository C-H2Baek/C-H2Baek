const box = document.getElementById('box')
const moves = [
    {pos: 'left', length: 100},
    {pos: 'top', length: 100},
    {pos: 'left', length: 0},
    {pos: 'top', length: 0}
] // 움직임을 미리 정의해둔다
let select = 0

function moveBox(){
    const pos = moves[select].pos
    const length = moves[select].length
    box.style[pos] = length + 'px' // box 가 움직임
    select++
    if(select > moves.length -1){
        select = 0
    }
}
function startMove(){
    setInterval(moveBox, 1000)
}
window.addEventListener('load', startMove)