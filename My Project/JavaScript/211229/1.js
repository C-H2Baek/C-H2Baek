//
const animals = ['lion' , 'tiger' , 'cat', 'dog' , 'pig' , 'cat']
const searchAnimal = animals.indexOf('cat')
const notexist = animals.indexOf('puppy')
console.log(searchAnimal)
console.log(notexist)
//

//
const animalToSearch = 'cat'
const searchedIndexes = []
let foundIndex = animals.indexOf(animalToSearch)
while(foundIndex != -1){
    searchedIndexes.push(foundIndex)
    foundIndex = animals.indexOf(animalToSearch, foundIndex+1)
}
console.log(searchedIndexes)
//

//
const fruits = ['apple' , 'banana' , 'orange' , 'watermelon']
function longest(fruit, index, fruits){
  return fruit.length >= 6
}
const found = fruits.find(longest)
console.log(found)
//
//
const words = ['car', 'paper', 'mobile', 'computer', 'school', 'sun', 'house']
const wordsFiltered = words.filter(word => word.length < 5)
console.log(wordsFiltered)
//

//
const currentTime = [3, 8, 23] // 시, 분, 초
const timeStr = []

function addZero(time){
    timeStr.push(`${time < 10 ? '0' + time : time}`)
}

currentTime.forEach(addZero)

console.log('********* CURRENT TIME *********')
console.log(timeStr.join(':'))
console.log('***********************************')
//
//
const userIDs = ['victoria', 'sun', 'johseb', 'syleemomo', 'hannah', 'shara', 'martin', 'gorgia', 'nana', 'dannel']

console.log('********* USER EMAIL LIST *********')
function addDotCom(userID){
    console.log(userID + '@gmail.com')
}

userIDs.forEach(addDotCom)
console.log('***********************************')
//

//
const numbers = [1, 2, 3, 4, 5]

function multiplyByThree(n){
    return n * 3
}

const numbersRefined = numbers.map(multiplyByThree)
console.log(numbersRefined)
//
//
const userEmails = [
  'victoria@gmail.com',
  'sun@gmail.com',
  'johseb@gmail.com',
  'syleemomo@gmail.com',
  'hannah@gmail.com',
  'shara@gmail.com',
  'martin@gmail.com',
  'gorgia@gmail.com',
  'nana@gmail.com',
  'dannel@gmail.com'
]
function removeDotCom(userEmail){
  return userEmail.split('@')[0]
}
function displayUserID(userID){
  console.log(userID)
}
const userIDs2 = userEmails.map(removeDotCom)
userIDs2.forEach(displayUserID)


//
//
//

