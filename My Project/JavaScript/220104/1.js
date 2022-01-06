const seasons = ['spring', 'summer', 'autumn']

const arrLength = seasons.push('winter')

console.log(seasons) //  변경된 원본배열 출력
console.log(arrLength) // 변경된 배열 길이 출력

/////

const multiplyBySix = []

for(let i=1; i<100; i++){
    multiplyBySix.push( 6 * i )
}

console.log(multiplyBySix) //  6의 배수로 이루어진 배열

/////

const movies = ['Haprry potter', 'Doctor stranger', 'Iron man', 'Spider man', 'Widow']
const moviesInfo = []

function addMovieInfo(movie, index, movies){
    moviesInfo.push( {title: movie, id: index} )
}
movies.forEach(addMovieInfo)

console.log(moviesInfo) //  무비 ID 가 추가된 영화 목록 생성

/////

const cities = ['seoul', 'busan', 'daegu']

cities.push('deajeon', 'ulsan')

console.log(cities)

/////

const cities2 = ['seoul', 'busan', 'daegu']
const citiesToAdd = ['deajeon', 'ulsan']

cities2.push(...citiesToAdd)

console.log(cities)

/////

const companies = ['Samsung', 'LG', 'Google', 'Facebook', 'Amazon']

console.log(companies.pop())
console.log(companies)

/////

const fruits = ['apple', 'orange', 'watermelon']

const removedFruits = fruits.splice(1, 0, 'banana')

console.log(fruits)
console.log(removedFruits)

/////

const fruits2 = ['apple', 'banana', 'strawberry', 'orange', 'watermelon']

const removedFruits2 = fruits2.splice(2, 1, 'strawberry가 제거 되고 이것이 추가1' , '이것이 추가2')

console.log(fruits2)
console.log(removedFruits2)

/////

const fruits3 = ['apple', 'banana', 'strawberry', 'orange', 'watermelon']

const removedFruits3 = fruits3.splice(fruits3.length - 4, 2)

console.log(fruits3)
console.log(removedFruits3)

///// sort 오름차순

const words = ['car', 'paper', 'mobile', 'computer', 'school', 'sun', 'house']

words.sort()

console.log(words)

///// reverse 내림차순

const words2 = ['car', 'paper', 'mobile', 'computer', 'school', 'sun', 'house']

words2.sort()

console.log(words2.reverse())

///// number 정렬 안됨

const numbers = [100, 3, 394, 27, 4, 82, 6, 5, 94]

numbers.sort()

console.log(numbers)

///// number 정렬

const numbers2 = [100, 3, 394, 27, 4, 82, 6, 5, 94]

///// 숫자 오름차순 정렬하기
function compareNumbers2(a, b){
    if(a > b) return 1 // 앞의 숫자(a)가 뒤의 숫자(b)보다 크면 순서를 변경함 (1을 반환하면 순서를 변경함)
    if(a < b) return -1 // 앞의 숫자(a)가 뒤의 숫자(b)보다 작으면 순서를 변경하지 않음 (-1을 반환하면 순서를 변경하지 않음)
    return 0 // 두 숫자가 동일하면 순서를 변경하지 않음
}
numbers2.sort(compareNumbers2)

console.log(numbers2)

/////

const numbers3 = [100, 3, 394, 27, 4, 82, 6, 5, 94]

// 숫자 오름차순 정렬하기
function compareNumbers3(a, b){
    return a - b
}
numbers3.sort(compareNumbers3)

console.log(numbers3)

/////

const numbers4 = [100, 3, 394, 27, 4, 82, 6, 5, 94]

// 숫자 내림차순 정렬하기
function compareNumbers4(a, b){
    return b - a
}
numbers4.sort(compareNumbers4)

console.log(numbers4)

/////

const numbers5 = [100, 3, 394, 27, 4, 82, 6, 5, 94]

// 숫자 내림차순 정렬하기
numbers5.sort( (a, b) => b - a) 

console.log(numbers5)