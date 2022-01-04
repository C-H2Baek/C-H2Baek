
// 1번 . 가사
const lyrics = `
Sorry Sorry Sorry Sorry
내가 내가 내가 먼저
네게 네게 네게 빠져
빠져 빠져 버려 baby
Shawty Shawty Shawty Shawty
눈이 부셔 부셔 부셔
숨이 막혀 막혀 막혀
내가 미쳐 미쳐 baby
바라보는 눈빛 속에
눈빛 속에 나는 마치
나는 마치 뭐에 홀린 놈
이젠 벗어나지도 못해
걸어오는 너의 모습
너의 모습 너는 마치
내 심장을 밟고 왔나봐
이젠 벗어나지도 못해
어딜 가나 당당하게
웃는 너는 매력적
착한 여자 일색이란
생각들은 보편적
도도하게 거침 없게
정말 너는 환상적
돌이킬 수 없을만큼
네게 빠져 버렸어
Sorry Sorry Sorry Sorry
내가 내가 내가 먼저
네게 네게 네게 빠져
빠져 빠져 버려 baby
Shawty Shawty Shawty Shawty
눈이 부셔 부셔 부셔
숨이 막혀 막혀 막혀
내가 미쳐 미쳐 baby
딴딴 딴따다 따 따란딴
딴딴 딴따다 따
네게 반해버렸어 baby
딴딴 딴따다 따 따란딴
딴딴 딴따다 따 따라빠빠라
Hey girl gir gir gir gir girl i
눈만뜨면 니 생각 Hey girl
자나깨나 사실 너 하나 밖에 안보여
말해봐 니 맘에 내가
말해봐 자리 잡았는지
말해줘 내게 말해줘
나는 바보 바보 바보
주변 사람들은 말해
내가 너무 적극적
이 세상에 그런 사람
어디 한둘이냐고
그걸 몰라 그녈 몰라
시기하며 하는 말
내가 부럽다면 그건
그대들이 지는 거
Sorry Sorry Sorry Sorry
내가 내가 내가 먼저
네게 네게 네게 빠져
빠져 빠져 버려 baby
Shawty Shawty Shawty Shawty
눈이 부셔 부셔 부셔
숨이 막혀 막혀 막혀
내가 미쳐 미쳐 baby
딴딴 딴따다 따 따란딴
딴딴 딴따다 따
네게 반해버렸어 baby
딴딴 딴따다 따 따라라라
딴딴 딴따다 따 따라빠빠라
Lets dance dance dance dance
Lets dance dance dance dance
Lets dance dance dance dance dance dance
Hey 이제 그만 내게 와줄래
정말 미칠 것만 같아 yeah
난 너만 사랑하고 싶어
절대 다시 한눈 팔 생각 없어 hey hey hey.
애인이라기보다 친구같은
내가 되고 싶어
너의 모든 고민 슬픔
함께 간직하고파
다시 없을 만큼 만큼
너를 너무 사랑해
내가 바란 사람 니가 바로 그
That that that girl
Sorry Sorry Sorry Sorry
내가 내가 내가 먼저
네게 네게 네게 빠져
빠져 빠져 버려 baby
Shawty Shawty Shawty Shawty
눈이 부셔 부셔 부셔
숨이 막혀 막혀 막혀
내가 미쳐 미쳐 baby
`
const keyword1 = 'Sorry'
const keyword2 = '부셔'

function searchWord(keyword, n){
    const searchDIndexes = []
    let foundIndex = lyrics.indexOf(keyword)

    while(foundIndex != -1){
        searchDIndexes.push(foundIndex)
        foundIndex = lyrics.indexOf(keyword, foundIndex+n)
    }
    return searchDIndexes.length
	
}

console.log(searchWord(keyword1, keyword1.length))
console.log(searchWord(keyword2, keyword2.length))
//


// 2. release 가 2005와 2010년 사이 movie중 첫번째로 검색 되는 영화 find사용, return 객체
const movies = [
    {title: 'Harry Potter', release: '2003-02-22'}, 
    {title: 'Indiana Jhones', release: '2009-01-09'}, 
    {title: 'Jurassic Park', release: '2007-04-13'},
    {title: 'Iron man', release: '2012-12-18'},
    {title: 'Spider man', release: '2017-03-07'}
]
function hasSomeWord2(element){
    return element.release.split('-')[0] < 2010 && element.release.split('-')[0] > 2005
}
const found2 = movies.find(hasSomeWord2)
console.log(found2)

// 3. title에 man이 포함 movie중 첫번째
function hasSomeWord3(element){
    return element.title.includes('man')
}
const found3 = movies.find(hasSomeWord3)
console.log(found3)

// 4. realses 가 2010년 이전 title이 J로 시작. 문자열.startsWith(시작문자)

function hasSomeWord4(element){
    return element.release.split('-')[0] < 2010 && element.title.startsWith('J')
}
const found4 = movies.find(hasSomeWord4)
console.log(found4)

// 5. a가 한번 이상 들어가는 words
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

words.forEach(word => {
    if(word.indexOf('a') > -1) {
        console.log(word)
    }
})

// 6. 제품 유형이(product_type) 이 mascara, 가격(price) 이 10달러 미만인 모든 정보 
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline' 

fetch(API_URL)
    .then(function(res){
        return res.json()
    })
    .then(function(products){
        //console.log(products)

        // 조건에 맞는 상품을 검색하는 코드 구현하기
        products.forEach(product => {
            if (product.product_type === 'mascara' && parseInt(product.price) < 10) {
               // console.log(product)
        }
    })
})

// 7. 제품 유형이(product_type) 이 mascara, 평점(rating) 이 4점과 5점 사이인 모든 정보 

fetch(API_URL)
    .then(function(res){
        return res.json()
    })
    .then(function(products){
        //console.log(products)

        // 조건에 맞는 상품을 검색하는 코드 구현하기
        products.forEach(product => {
            if (product.product_type === 'lipstick' && parseFloat(product.rating) >= 4 && parseFloat(product.rating) <= 5) {
               //console.log(product)
        }
    })
})

// 8. 도시 seoul 나이 < 30
const friends = [
    {name: 'victoria', age: 13, city: 'seoul'},
    {name: 'sun', age: 34, city: 'busan'},
    {name: 'johseb', age: 25, city: 'busan'},
    {name: 'syleemomo', age: 9, city: 'seoul'},
    {name: 'hannah', age: 41, city: 'daegu'},
    {name: 'shara', age: 37, city: 'seoul'},
    {name: 'martin', age: 28, city: 'daegu'},
    {name: 'gorgia', age: 39, city: 'seoul'},
    {name: 'nana', age: 24, city: 'busan'},
    {name: 'dannel', age: 19, city: 'seoul'},
]
friends.forEach(element =>  {
    if(element.city === 'seoul' && element.age < 30)  {
      console.log(element)
    }
})


// 9. city 프로퍼티 기준을 분류
const ci = {}
function pro(params){
    if(ci[params.city] == undefined){
        ci[params.city] = 0
    }
    ci[params.city]++
}
friends.forEach(pro)
console.log(ci)
var citylength = Object.keys(friends);
console.log("결과 개수:" + citylength.length);

// 10. 
friends.some(friend => friend.age > 40)
friends.every(friend => friend.age > 40)







// 11.
const users = [
    {name: 'victoria', age: 13, city: 'seoul', email: 'victoria@gmail.com'},
    {name: 'sun', age: 34, city: 'busan', email: 'sun@gmail.com'},
    {name: 'johseb', age: 25, city: 'busan', email: 'johseb@gmail'},
    {name: 'syleemomo', age: 9.23, city: 'seoul', email: 'syleemomo@nate.com'},
    {name: 'hannah', age: 41, city: 'daegu', email: 'hannah0923*gmail.com'},
    {name: 'shara', age: 37, city: 'seoul', email: 'shara@gmail.com'},
    {name: 'martin', age: -34, city: 'daegu', email: 'martin@gmail.com'},
    {name: 'gorgia', age: 39, city: 'seoul',  email: 'gorgia@gmail.com'},
    {name: 'nana', age: 24, city: 'busan', email: 'nana@gmail.com'},
    {name: 'dannel', age: 19, city: 'seoul', email: 'dannel@gmail.com'},
]

let filteredUsers = null

function ageIsValid(user){
    return user.age > 0 && parseInt(user.age) === user.age
}
function emailIsValid(user){
    return user.email.indexOf('@') > -1 && user.email.includes('.com')
}
filteredUsers = users.filter(ageIsValid)
filteredUsers = filteredUsers.filter(emailIsValid)












