// 1번
let num = new Array(100).fill(0)

for(let i=0; i<num.length; i++){
    if((i+1)%3 == 0){
    num[i] = i+1    
    }
}
console.log(num)

// 2번
//const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
let pr="";
function jj(){
    for(var j=26; j>i; j--) pr+="";};
function kk(){
    for(var k=0; k<=i; k++) pr+=String.fromCharCode(k+65)+"";}
    for(i=0; i<26; i++) {pr+="", jj(), kk(), jj(), pr+="<br>"};
    document.write(pr);
console.log(pr)

//3번

var uu = 1;

while(uu<=100){		
    if( uu % 3 == 0 ){
        document.write("<span style='color:blue'>" + uu);
    } else {
        document.write("<span style='color:red'>" + uu);
    }
    uu++;
}
console.log(uu)




// 4번

const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function randomStr(n){
    
}
function randomStr(n){
    
}
function randomStr(n){
    
}
console.log(randomStr(3))
console.log(randomStr(5))
console.log(randomStr(7))



// 5번


// 6번
const movies = [
    {title: 'Harry Potter', release: '2003-02-22'}, 
    {title: 'Indiana Jhones', release: '2009-01-09'}, 
    {title: 'Jurassic Park', release: '2007-04-13'},
    {title: 'Iron man', release: '2012-12-18'},
    {title: 'Spider man', release: '2017-03-07'}
]

//const movies_copied = [...movies]
//movies[1] = {title:'ABCDEFG', release: '2009-01-09'} // 원본배열 변경

const movies_copied = []

for(let movie in movies){
    movies_copied[movie] = [movies[movie].title, movies[movie].release]
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
const words = [
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
function isPalindrome(word) {
    let count = 0
    for(let wordc of word){
        let word_count=0;
        for(let i=0; i<wordc.length; i++){
            if(wordc.charCodeAt(i) == wordc.charCodeAt(wordc.length)){
                word_count++
            }
            if(word_count == word_length){
                count++
                console.log()
            }

        }
    }
	// 구현하기
}

const str = 'abcde';

const newStr = 
      str.split('').reverse().join('');
console.log(isPalindrome(words))