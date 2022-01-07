const movies = [
    {title: 'Harry Potter', release: '2003-02-22'}, 
    {title: 'Indiana Jhones', release: '2009-01-09'}, 
    {title: 'Jurassic Park', release: '2007-04-13'},
    {title: 'Iron man', release: '2012-12-18'},
    {title: 'Spider man', release: '2017-03-07'}
]

const slicedWords = movies.slice(1, 3) // 부분배열 추출

movies[1].title = 'syleemomo' // 원본배열에서 배열요소(객체)의 프로퍼티 변경

console.log(movies)
console.log(slicedWords)

const fruits = ['apple', 'banana', 'orange', 'lemon', 'watermelon']
const [,,thirdFruit] = fruits
console.log(thirdFruit)

const words = ['car', 'mobile', 'sun', 'foot', 'pen']
const numbers = [1, 2, 3]

const unitedArr = words.concat(numbers)
const unitedArr2 = [...words, ...numbers]
console.log(unitedArr)
console.log(unitedArr2)


const fruitsStr = fruits.join(' & ')
console.log(fruitsStr)

const str = ''
const strSeprated = str.split()
console.log(strSeprated)

const sentence = 'I joined swimming club in my highschool'
const splitedSentence = sentence.split()
const splitedSentence2 = sentence.split('')
const splitedSentence3 = sentence.split(' ')
const splitedSentence4 = sentence.split(' ', 3)
console.log(splitedSentence)
console.log(splitedSentence2)
console.log(splitedSentence3)
console.log(splitedSentence4)

const sentence2 = 'I (joined) swimming <club> in my highschool'
const sentence3 = 'I^,^joined^,^swimming^,^club^,^in^,^my^,^highschool'
const splitedSentence5 = sentence2.split(/[()<>]/)
const splitedSentence6 = sentence3.split(['^', '^'])
console.log(splitedSentence5)
console.log(splitedSentence6)

const sentence4 = 'I joined swimming club in my highschool. that club was awsome !'
const foundedKeyword = sentence4.split(' ').filter(word => word === 'club')
console.log(foundedKeyword.length)

const sentence5 = '?죠밌재 트립크스바자'
const splitedSentence7 = sentence5.split('').reverse().join('')
console.log(splitedSentence7)

const modifiedSentence = sentence4.split(' ').map(word => {
                            return word = word === 'club' ? `${word} 🏊` : word
                        })
                        .join(' ')
console.log(modifiedSentence)