const _2dArray = []
const rows = 5
const columns = 2

for (let i = 0; i < rows; i++) {
    const element = []
    for (let j =columns * i; j < columns * i + columns; j++) {
        element.push(j+1)
    }
    _2dArray.push(element)
}
console.log(_2dArray)

const fruits = [['apple', 570], ['orange', 270], ['strawberry', 30]]

for(let fruit of fruits){
    for(let i in fruit){
        switch(i){
            case '0':
                console.log('name', fruit[i])
                break;
            case '1': 
                console.log('price', fruit[i])
                break;
        }
    }
}

console.table(fruits)

const persons = [
    "sunrise",
    23,
    "victoria",
    19,
    "daniel",
    28,
    "ammy",
    21,
    "smith",
    32
]


const columns2 = 2
const rows2 = persons.length / columns2
const _2dArray2 = new Array(rows2).fill(0)

for(let i=0; i<rows; i++){
    const person = new Array(columns2).fill(0)
    for(let j=0; j<columns2; j++){
        person[j] = persons[columns2*i+j] 
    }
    _2dArray[i] = person
}

console.table(_2dArray)