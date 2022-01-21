// 1
console.log("\t\tSolve 1\n\n")
const SecondArray = []
for(let i=0; i<5; i++){
    const num = 2
    SecondArray.push([(num*i+1),(num*i+2)])
}
console.log(SecondArray)

// 2
console.log("\t\tSolve 2\n\n")
function Create2DArray(rows, columns){
    const Create = new Array(rows)
    for (let i = 0; i < rows; i++) {
        Create[i] = new Array(columns).fill(0)
    }
    return Create
}
console.log(Create2DArray(7,3))




// 3
console.log("\t\tSolve 3\n\n")
const fruits = [['apple', 570], ['orange', 270], ['strawberry', 30]]

for (let fruit in fruits){
    fruits[fruit] = {name: fruits[fruit][0] , price: fruits[fruit][1]}
}
console.log(fruits)

// 4
console.log("\t\tSolve 4\n\n")
const fruitsT = [['apple', 570, 32], ['orange', 270, 65], ['strawberry', 30, 120]]
for (let fruit in fruitsT){
    fruitsT[fruit] = {name: fruitsT[fruit][0] , totalprice: (fruitsT[fruit][1]*fruitsT[fruit][2])}
}
console.log(fruitsT)


// 5
console.log("\t\tSolve 5\n\n")

const graph = document.getElementById('graph')

let points = [] // 포인트 배열
let x = 0 // degree
let offset = 0 // 추출 시작점

function degreeToRad(x){
    return x * (Math.PI / 180)
}
function calSinVal(x){
    return Math.sin(x)
}
function clearWindow(el){
    el.innerHTML = ''
}
function getPoint(x){
    return [x, calSinVal(degreeToRad(x))]
}
function isArrayFull(len){
    return len > 360
}

function displayPoint(point){
    const [x, y] = point
    const xScale = 2, yScale = 100, yShift = 100

    const pointEl = document.createElement('div')
    pointEl.className = 'dot'
    pointEl.style.left = `${(x - offset) * xScale}px` // x-scale: 2배 (offset 만큼 좌표이동)
    pointEl.style.top = `${(y* yScale) * -1 + yShift}px` // y-scale : 100배 (반전 + 좌표이동)
    graph.appendChild(pointEl)
}

function redraw(){
    clearWindow(graph)
    
    points.push(getPoint(x)) // 포인트 추가
    x++ // x 좌표 변경

    if(isArrayFull(points.length)){
        points.shift() // 첫번째 요소를 제거함으로써 360개 유지
        offset++ //  offset 증가
    }
    points.forEach(displayPoint) // 화면에 그래프 그리기
  
}

setInterval(redraw, 1000)







// 6
console.log("\t\tSolve 6\n\n")

const signDiv = document.getElementById('sign')
const sign1 = [
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
const sign2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
]
const sign3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
const sign4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
const sign5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
]

const signs = [sign1, sign2, sign3, sign4, sign5]
let index = 0

function displayCell(value){
    const cellEl = document.createElement('div')
    cellEl.className = value === 0 ? 'cell' : 'cell bright'
    signDiv.appendChild(cellEl)
}

function displaySign(sign){
    const rows = sign.length
    const columns = sign[0].length

    for(let i=0; i<rows; i++){
        for(let j=0; j<columns; j++){
            displayCell(sign[i][j])
        }
    }
}

function redraw2(){
    const sign = signs[index % signs.length]
    signDiv.innerHTML = '' // 화면 초기화
    displaySign(sign)
    index++
}

setInterval(redraw2, 10000)