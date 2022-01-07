const rootDiv = document.getElementById('root') // 화면에 리스트를 보여줄 위치
const priceBtn = document.getElementById('price-btn') // 가격 정렬 버튼
const searchInput = document.getElementById('search-input') // 사용자 상품 검색창
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline' // API 주소

let shouldSort = false // 정렬여부 판단
let shouldFilter = false // 검색여부 판단
let originalProducts = null
let keyword = ''


function buildElement(product) {
    const item = document.createElement('div')
    item.className = 'product'
    item.innerHTML = `
        <div class='product-img'><img src=${product.image_link} alt=${product.name}/></div>
        <div class='product-name'>${product.name} ($${product.price})</div>
        <div class='product-description'>${product.description}</div>
        <div class='product-type'>${product.product_type}</div>
    `
    return item
}
function displayProducts(products) {
    rootDiv.innerHTML = '' // 리스트 초기화
    products.forEach(product => {
        rootDiv.appendChild(buildElement(product))
    })
}

function updateProducts(products, keyword) {
    // 조건 쿼리 (conditional query)
    let newProducts = [...products] // 원본배열을 함수 내부에서 지역변수에 복사
    if (shouldFilter) {
        newProducts = newProducts.filter(product => product.product_type.toLowerCase().includes(keyword.toLowerCase()))
    }
    if (shouldSort) {
        newProducts.sort((p1, p2) => parseFloat(p1.price) - parseFloat(p2.price))
    }
    return newProducts
}

function sortByPrice() {
    shouldSort = !shouldSort

    const newProducts = updateProducts(originalProducts, keyword) // 정렬 및 검색
    displayProducts(newProducts) // 정렬 및 검색된 새로운 배열을 화면에 보여주기
}

function searchProducts(e) {
    shouldFilter = e.target.value !== ''
    keyword = e.target.value

    const newProducts = updateProducts(originalProducts, keyword) // 정렬 및 검색
    displayProducts(newProducts) // 정렬 및 검색된 새로운 배열을 화면에 보여주기
}

// 서버에서 데이터 가져오기
fetch(API_URL)
    .then(function (res) {
        return res.json()
    })
    .then(function (products) {
        originalProducts = products // 원본 데이터 저장
        displayProducts(products) // 상품 정보 디스플레이하기 (초기 렌더링)

        priceBtn.addEventListener('click', sortByPrice)
        searchInput.addEventListener('input', searchProducts)
    })


