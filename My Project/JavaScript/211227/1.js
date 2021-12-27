// 1번
let num = new Array(100).fill(0)

for (let i = 0; i < num.length; i++) {
    //if ((i + 1) % 3 == 0) {
    if (i % 3 == 2) {
        num[i] = i + 1
    }
}
console.log(num)

// 2번
const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
const words = []

for(let i=0;i<alphabet.length; i++){
    if(i === 0){
        words[i] = alphabet[i]
    }else{
        words[i] = words[i-1] + alphabet[i]
    }
}
console.log(words)

// let pr = "";
// function jj() {
//     for (var j = 26; j > i; j--) pr += "";
// };
// function kk() {
//     for (var k = 0; k <= i; k++) pr += String.fromCharCode(k + 65) + "";
// }
// for (i = 0; i < 26; i++) { pr += "", jj(), kk(), jj(), pr += "<br>" };
// document.write(pr);
// console.log(pr)

//3번

const numb = []
for(let i=0; i<100; i++){
    numb[i] = 3 * (i + 1)
}
console.log(numb)

var uu = 1;
while (uu <= 100) {
    if (uu % 3 == 0) {
        document.write("<span style='color:blue'>" + uu);
    } else {
        document.write("<span style='color:red'>" + uu);
    }
    uu++;
}
console.log(uu)




// 4번

const alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function pickRandomIndex(n) {
    return Math.floor(Math.random() * n)
}
function randomStr(n) {
    const w = new Array(n).fill('O')
    for(let i in w){
        w[i] = alphabet2[pickRandomIndex(alphabet2.length)]
    }
    return w
}
console.log(randomStr(3))
console.log(randomStr(5))
console.log(randomStr(7))



// 5번
// const numb2 = []
// for(let i=0; i<100; i++){
//     numb[i] = 3 * (i + 1)
// }
// for(let i = 0 ; i< 100; i++){
//     if(numb2[i] % 6 ===0) numb2[i]=null
// }
// console.log(numb2)

// 6번
const movies = [
    { title: 'Harry Potter', release: '2003-02-22' },
    { title: 'Indiana Jhones', release: '2009-01-09' },
    { title: 'Jurassic Park', release: '2007-04-13' },
    { title: 'Iron man', release: '2012-12-18' },
    { title: 'Spider man', release: '2017-03-07' }
]

//const movies_copied = [...movies]
//movies[1] = {title:'ABCDEFG', release: '2009-01-09'} // 원본배열 변경

const movies_copied = []

for (let movie in movies) {
    movies_copied[movie] = {title: movies[movie].title, release: movies[movie].release}
}

movies[1].title = 'syleemomo'

console.log(movies)
console.log(movies_copied)

// const movies = ['Harry Potter', 'Indiana Jhones', 'Jurassic Park', 'Iron man', 'Spider man']
// const movies_copied = [...movies]

// movies[2] = null

// console.log(movies)
// console.log(movies_copied)

// 7번
const words2 = [
    'abc',
    'animal',
    'fruit',
    'abba',
    'abcba',
    'location',
    'radar',
    'madam',
    'mario',
    'level'
]
function isPalindrome(words2) {
//     let isRight = true
//     for(let i=0; i<words2.length/2-1; i++){
//         if(words2[i] === words2[words2.length-1-i]){
//             continue
//         }else{
//             return false
//         }
//     }
//     return isRight
// }

// let cnt = 0
// for (let word of words){
//     if (isPalindrome(word)) cnt++
// }
// console.log(cnt)
    let count = 0
    for (let wordc of words2) {
        let word_count = 0;
        for (let i = 0; i < wordc.length; i++) {
            if (wordc.charCodeAt(i) == wordc.charCodeAt(wordc.length - (i + 1))) {
                word_count++
            }
        }
        if (word_count == wordc.length) {
            count++
            console.log(wordc)
        }
    }
    return count
    // 구현하기
}
console.log(isPalindrome(words2))