/*
// 생성한 DOM 객체
const div = document.createElement('div')
div.className = 'parent'
div.innerText = 'Hello World !'

// 생성한 DOM 에 자식 요소 추가하기
const img = document.createElement('img')
img.id = "photo" // id 값으로 가능위한 id 속성부여
img.src = "http://127.0.0.1:5500"
img.alt = "photo"

const p = document.createElement('p')
p.className = 'summary'
p.innerText = 'this is summary!'

// div에 자식요소가 추가
div.appendChild(img, p)

// HTML문서에 DOM객체를 마운트 하기 전
const photo = document.getElementById('photo')
console.log(photo)

// id 값이 root인 div 요소에 방금 생성한 dom 객체를 마운트
const root = document.getElementById('root')
root.appendChild(div)

// HTML문서에 DOM객체를 마운트 하기 후
const photo2 = document.getElementById('photo')
console.log(photo2)
*/

/*
// 사진리스트의 div 요소 검색하기
const photos = document.querySelectorAll('.photo-item')
console.log(photos)

// 사진리스트의 img 요소 검색하기
const imgs = document.querySelectorAll('.photo-item img')

for(let img of imgs){
    console.log(img)
}

const photos = document.getElementsByClassName('photo-item')

for(let photo of photos){
    console.log(photo)
}

// 사진리스트의 img 요소 검색하기
const imgs = document.getElementsByTagName('img')

// 배열을 이용한 각각의 DOM 객체 조회하기
for(let img of imgs){
    console.log(img)
}

// 부모 요소에 접근하기
const photos = document.querySelectorAll('.photo-item')
console.log(photos[0].parentElement.parentElement)
*/

// img 요소의 속성 조회하기
const img = document.getElementById('photo-container')
console.log(img)
console.log(img.firstElementChild)
console.log(img.alt)

