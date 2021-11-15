/*
const isLoading = true; 
const person = null; 
let city = 'seoul';
let age = 33;
console.log(typeof isLoading) 
console.log(typeof person) 
console.log(typeof city)
console.log(typeof age)
*/
/*
const fruits = ["apple", "banana", "orange"] 
const car = { 
    name: "Grandger", 
    year: 2016, 
    owner: 'C.H Baek' }

console.log(fruits instanceof Array) 
console.log(car instanceof Array)
*/
/*
function changeName() {}
console.log(typeof changeName)
const age = 30
const tempreture = 35.5

console.log(Number.isInteger(age))
console.log(Number.isInteger(tempreture))
console.log(typeof age)
console.log(typeof tempreture)
*/
/*
// 문자열형 타입 
const age = "32" 
const temparature = "37.6" 
const msg = "hello world 237" 
const msg2 = "237 hello world" 
// 숫자형으로 변환하기 
const age_casted = Number(age) 
const temp_casted = Number(temparature) 
const msg_casted = parseInt(Number(msg)) 
const msg2_casted = parseInt(msg2) 

console.log(typeof age) 
console.log(typeof age_casted) 
console.log(age_casted) 
console.log(typeof temparature) 
console.log(typeof temp_casted) 
console.log(temp_casted) 
console.log(typeof msg) 
console.log(typeof msg_casted) 
console.log(msg_casted)
console.log(msg2_casted)
*/
// 원시타입과 객체 타입 
/*
const age = 17 
const temp = 23.9 
const isLoading = false 
const numbers = [1, 2, 3, 4, 5] 
const person = { name: 'sunrise', city: 'seoul' } 
// 문자열형으로 변환하기 
const age_casted = age.toString() 
const temp_casted = temp.toString() 
const isLoading_casted = isLoading.toString() 
const numbers_casted = numbers.toString() 
const person_casted = person.toString() 
console.log(age_casted) 
console.log(typeof age_casted) 
console.log(temp_casted) 
console.log(typeof temp_casted) 
console.log(isLoading_casted) 
console.log(typeof isLoading_casted) 
console.log(numbers_casted) 
console.log(typeof numbers_casted) 
console.log(person_casted) 
console.log(typeof person_casted)
*/
/*
const result = 31 + "3"
const result2 = parseInt(result)
console.log(result)
console.log(typeof result)
console.log(result2)
console.log(typeof result2)

const result3 = 31 * "3"
console.log(result3)
console.log(typeof result3)
*/
/*
console.log(Boolean(0))
console.log(Boolean(NaN))
console.log(Boolean(false))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean(""))
console.log(Boolean(''))
console.log(Boolean(10))
console.log(Boolean('N1aN'))
console.log(Boolean('fa1lse'))
console.log(Boolean('nul1l'))
console.log(Boolean('unde1fined'))
console.log(Boolean("1"))
console.log(Boolean('1'))
*/

//1
let sofa = 360000
//2
let size
size = '275mm'
//3
const pi = 3.14
//4
const name = "sunrise"
const message = "Happy halloween, "
console.log(`${message}${name}`)
//5
const letter = `I guess u haven't\ sleep much last night \n\
                I hope to see you soon. Cya`
console.log(letter)
//6
const favoriteFoods = ["pizza", "pizza2", "pizza3"]
//7
const food = {
    name : 'pizza',
    price : 30000,
    kind : '양식'
}
//8
const hoursForDay = 24
const bookName = "Harry Potter"
const isChecked = true
console.log(typeof hoursForDay)
console.log(typeof bookName)
console.log(typeof isChecked)

//9
const cities = ['seoul' , 'deagu' , 'busan' ]
const bookInfo = {
    name : 'Harry Potter',
    price : 17000,
    author : 'J.K RoLLing'
}
// console.log(cities instanceof Array)
// console.log(bookInfo instanceof Array)
console.log(Array.isArray(cities))
console.log(Array.isArray(bookInfo))
console.log(cities instanceof Array)
console.log(bookInfo instanceof Array)

//10
const distanceSeoulToBusan = 370
const sizeOfYourHeight = 275.9

console.log(Number.isInteger(distanceSeoulToBusan))
console.log(Number.isInteger(sizeOfYourHeight))

//11
const speedOfCar = "37.5 m/s"
const heightOfYourFriend = "289 cm"
const speedOfCar_casted = parseFloat(speedOfCar)
const heightOfYourFriend_casted = parseFloat(heightOfYourFriend)
console.log(speedOfCar_casted)
console.log(heightOfYourFriend_casted)


//12
const heightOfYourFriend2 = 289
const temparature2 = 13.9
const fruits2 = ["apple" , "banana" , "orange"]
console.log(heightOfYourFriend2.toString())
console.log(temparature2.toString())
console.log(fruits2.toString())
console.log(typeof heightOfYourFriend2)
console.log(typeof temparature2)
console.log(typeof fruits2)
