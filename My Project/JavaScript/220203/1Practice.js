/// 1번

function pickRandomNumber(min, max){
    return Math.floor(Math.random() * (max-min+1)) + min
}
function createTesters(len){
    const group = []
    for(let i=0; i<len; i++){
        group.push(new Tester(
            pickRandomNumber(1, 10),
            pickRandomNumber(1, 10),
            pickRandomNumber(1, 5),
            pickRandomNumber(1, 10),
            pickRandomNumber(0, 50)
        ))
    }
    return group
}
function isQualityOfSleep(qos){
    return qos >= 0.37 && qos <= 50
}
function countQualityOfSleep(group){
    let cnt = 0
    group.forEach(tester => {
        tester.calQualityOfSleep()
        //console.log('----------------------')
        //console.log(tester.timeToAsleep)
        //console.log(tester.timeToWakeup)
        //console.log(tester.numsOfWakeup)
        //console.log(tester.numsOfMove)
        //console.log(tester.portionOfdelta)
        //console.log(tester.qualityOfSleep)
        //console.log('----------------------')
        if(isQualityOfSleep(tester.getQuilityOfSleep)) cnt++
    })
    return cnt
}
function chooseBestBed(a, b, c){
    const counts = [
        {group: 'A', cnt : a},
        {group: 'B', cnt : b},
        {group: 'C', cnt : c}
    ]
    counts.sort( ( c1, c2) => c2.cnt - c1.cnt)
    //alert(`${counts[0].group} bed is choosen to a new bed this year!`)
}

function Tester(timeToAsleep, timeToWakeup, numsOfWakeup, numsOfMove, portionOfdelta){
    this.timeToAsleep = timeToAsleep
    this.timeToWakeup = timeToWakeup
    this.numsOfWakeup = numsOfWakeup
    this.numsOfMove = numsOfMove
    this.portionOfdelta = portionOfdelta
    this.qualityOfSleep = 0
}
Tester.prototype = {
    calQualityOfSleep(){
        this.qualityOfSleep = this.portionOfdelta / (this.timeToAsleep * this.timeToWakeup * this.numsOfWakeup * this.numsOfMove)
    },
    get getQuilityOfSleep(){
        return this.qualityOfSleep
    }
}

const aGroup = createTesters(100), bGroup = createTesters(100), cGroup = createTesters(100)

//console.log(aGroup)
//console.log(bGroup)
//console.log(cGroup)

console.log('A group cnt', countQualityOfSleep(aGroup))
console.log('B group cnt', countQualityOfSleep(bGroup))
console.log('C group cnt', countQualityOfSleep(cGroup))

chooseBestBed(
    countQualityOfSleep(aGroup),
    countQualityOfSleep(bGroup),
    countQualityOfSleep(cGroup)
)

/// 2번

function Station(name, lat, lon){
    this.name = name
    this.lat = lat
    this.lon = lon
}

Station.prototype.calDistance = function(dest){
    
    const R = 6371e3; // 지구의 반지름 (meter) 
    // 좌표를 라디안 단위로 변환 
    const φ1 = this.lat * Math.PI / 180; 
    const φ2 = dest.lat * Math.PI / 180; 
    const Δφ = (dest.lat - this.lat) * Math.PI / 180; 
    const Δλ = (dest.lon - this.lon) * Math.PI / 180; 
    const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2); 
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)); 
    const d = R * c; // meter // d = 11052555.850341197
    return d
}

const seoul = new Station('서울역', 37.55620110026294, 126.97223116703012)
const daejeon = new Station('대전역', 36.332516127741, 127.43421099777726)
const daegu = new Station('동대구역', 35.88049128950934, 128.62837657353532)
const busan = new Station('부산역', 35.116613680508806, 129.04009077373016)

const stations = [seoul, daejeon, daegu, busan]
const priceTable = []

for(let i=0; i<stations.length-1; i++){
    const d = stations[i].calDistance(stations[i+1]) // 요금 계산
    priceTable[`${stations[i].name}-${stations[i+1].name}`] = parseInt(d / 1000) * 100
}
console.table(priceTable)

const prices = Object.values(priceTable)
const stationNames = Object.keys(priceTable)

function sum(start, end){
    let sum = 0
    for(let i=start; i<end; i++){
        sum += prices[i]
    }
    return sum
}
for(let i=0; i<prices.length-1; i++){
    for(let j=i+1; j<prices.length; j++){
        priceTable[`${stationNames[i].split('-')[0]}-${stationNames[j].split('-')[1]}`] = sum(i ,j)
        // 여러 지점간 요금은 i부터 j까지 요금을 합산함
    }
}
console.table(priceTable)
 
// 3

const hairColors = ['black', 'brown', 'yellow', 'white', 'gold']
const hairTypes = ['curly', 'straight', 'wavy', 'coily']
const glasses = [true, false]
const heights = [150, 160, 170, 180, 190, 200]
const weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

const personNum = 10000
const persons = []
const classifiedFeatures = []

function pickFeature(feature){
    return feature[Math.floor(Math.random()*feature.length)]
}

function displayFeatures(features){
    const canvas = document.getElementById('canvas')
    for(let feature in features){
        const featureEl = document.createElement('div')
        featureEl.className = 'circle'
        featureEl.innerHTML = `
            <h1>${features[feature]}</h1>
            <div>${feature}</div>
            `
            canvas.appendChild(featureEl)
    }
}

function classify(person){
    for(let feat in person){
        let featValue = person[feat]
        switch(feat){
            case 'glasses':
                featValue = featValue ? 'put on glasses' : 'no glasses'
                break
            case 'height':
                featValue = featValue + 'cm'
                break
            case 'weight':
                featValue = featValue + 'kg'
        }
        if(!classifiedFeatures[featValue]) classifiedFeatures[featValue] = 0
        classifiedFeatures[featValue]++
    }
}

function Person(hairColor, hairType, glasses, height, weight){
    this.hairColor = hairColor
    this.hairType = hairType
    this.glasses = glasses
    this.height = height
    this.weight = weight
}

for(let i=0; i<personNum; i++){
    persons.push(new Person(
        pickFeature(hairColors),
        pickFeature(hairTypes),
        pickFeature(glasses),
        pickFeature(heights),
        pickFeature(weights)
    ))
}

console.log(persons)
persons.forEach(classify)
console.log(classifiedFeatures)
displayFeatures(classifiedFeatures)

