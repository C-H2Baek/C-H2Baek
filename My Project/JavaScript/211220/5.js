const prev = document.getElementById('prev')
const next = document.getElementById('next')
const cardContainer = document.getElementById('card-container')

function moveToRight(){
    console.log('right')
    const cards = document.querySelectorAll('.card')
    cardContainer.removeChild(cards[cards.length-1])
    cardContainer.insertBefore(cards[cards.length-1], cardContainer.childNodes[0])
}

function moveToLeft(){
    console.log('left')
    const cards = document.querySelectorAll('.card')
    cardContainer.removeChild(cards[0])
    cardContainer.appendChild(cards[0])
}
prev.addEventListener('click', moveToLeft)
next.addEventListener('click', moveToRight)