const fruits = ['apple', 'banana', 'peach', 'strawberry', 'watermelon']
const icons = ['🍎', '🍌', '🍑', '🍓', '🍉']
const rootDiv = document.getElementById('root')

function addIcons(fruit, index){
    const item = document.createElement('div')
    item.innerText = `${icons[index]} ${fruit}`
    return item
}

function displayFruits(fruit){
    console.log(fruit)
    rootDiv.appendChild(fruit)
}
const fruitsRefined = fruits.map(addIcons)
fruitsRefined.forEach(displayFruits)