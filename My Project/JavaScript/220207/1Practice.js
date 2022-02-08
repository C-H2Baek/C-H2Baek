// 1
function findMaxValue(...args){
    let max = -Infinity
    for(let arg of args){
        if(max < parseFloat(arg)){ // 숫자가 아닌 값들은 NaN 이며 NaN 과 비교하면 모두 false 이므로 조건문을 건너뛴다
            max = parseFloat(arg)
        }
    }
    return max

}
console.log(findMaxValue(-3, 7, -345, 41, 9, 137, 69))
console.log(findMaxValue(-31, 8, null, -26, false, 92, {}, 284, 923, [], "2045.8", 'zip', 54, "1024"))

// 2
function Movie(title, author, release){
    this.title = title
    this.author = author
    this.release = release

    this.printMovieInfo = () => {
        const getInfo = () => {
            return `${this.title}-${this.author}(은)는 ${this.release}에 발매되었다.`
        }
        console.log(getInfo()) 
    }
}

const movie = new Movie("해리포터", "조앤K롤링", "2003 년 3월 23일")
movie.printMovieInfo()

// 3
function getDistance(a,b = {x: 0 , y:0}){
    return Math.sqrt(Math.pow(a.x + b.x,2) + (a.y + b.y)**2)
}
 console.log(getDistance({x: 3, y: 2}, {x: 8, y: 14}))
 console.log(getDistance({x: 3, y: 4}))

// 4
function countDuplication(...args){
    const fruits = []
    fruits.push(...args)
    console.log(fruits)
    const result = {}
    fruits.forEach((x) => {
        result[x] = (result[x] || 0) +1;
    });
    return result 
}
console.log(countDuplication('cat', 'apple', 'cat', 'tiger', 'cat', 'water', 'computer', 'cat', 'lion', 'pear', 'cat'))


// 5
function add(...args){
    
    
    
    let sum = 0
    for(let arg of args){
        sum += !isNaN(parseFloat(arg)) ? parseFloat(arg) : 0
    }
    return sum

}
console.log(add(3, null, 19, false, '9', [], 7, {}, '', 34, 'earth', '3.9')) // 75.9


// 6
function divider(denominator, ...args){
    if(denominator === 0) return args // 데이터 유효성 검증
    return args.map(arg => arg / denominator)
}
console.log(divider(2, 39, 4, 7, 28, 62, 28))
console.log(divider(0, 39, 4, 7, 28, 62, 28))

// 7

const numbers = [121, 23, 345, 43, 59]

function pickIndex(len){
    return Math.floor(Math.random() * len)
}
function shuffle(Array){
    let temp
    for(let i in Array){
        pIndex = pickIndex(Array.length)
        temp = Array[pIndex]
        Array[pIndex] = Array[i]
        Array[i] = temp
    }
    return Array
    
}

console.log(shuffle(numbers))
