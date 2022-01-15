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
const points = []
const dx = 1 // degree
let x = 0 // degree
let y = 0
let radx = 0 // radian
// 다음 (X,Y) 포인트 값 계산
function getNextPoint(){
    radx = x * (Math.PI / 180)
    y = Math.sin(radx)
    points.push([x, y])
    x += dx
    // console.log(points)
}
// (X,Y) 포인트 값으로부터 DOM 객체 생성 및 화면에 표시
function displayPoint(point){
    const pointEl = document.createElement('div')
    pointEl.className = 'dot'
    pointEl.style.left = `${point[0] * 2}px` // x-scale: 2배
    pointEl.style.top = `${point[1]* 100 * -1 + 100}px` // y-scale : 100배 (반전 + 좌표이동)
    graph.appendChild(pointEl)
}
function redraw(){
    
}
// (X,Y) 포인트 값을 요소로 가지는 2차원 배열 생성
for(let i=0; i<360; i++){
    getNextPoint()
}
console.log(points)
setInterval(redraw,1000)
points.forEach(displayPoint)







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

