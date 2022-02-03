class Satisfaction {
    constructor(A, B, C, D, E) {
        this.A = "A"
        this.B = "B"
        this.C = "C"
        this.D = "D"
        this.E = "E"

        this.getInfo = function () {
            console.log('----- 수면 만족도 -----')
            console.log('In Time: ', this.A)
            console.log('Out Time: ', this.B)
            console.log('Awake: ', this.C)
            console.log('Back: ', this.D)
            console.log('Delta: ', this.E)
            console.log('Satisfaction: ', this.authors.join(' '))
        }
    }
}



function pickRandomNumber(min, max){
    return Math.floor( Math.random() * (max-min+1) ) + min 
}



//Satisfaction.getInfo()


/// 2번
const seoul = ["서울역" , 37.55620110026294, 126.97223116703012]
const daejeon = ["대전역" , 36.332516127741, 127.43421099777726]
const daegu = ["대구역" , 35.88049128950934, 128.62837657353532]
const busan = ["부산역", 35.116613680508806, 129.04009077373016]

// 출발지 (서울) 
const lat1 = 37.56654; 
const lon1 = 126.97796; 
// 목적지 (뉴욕) 
const lat2 = 40.71295; 
const lon2 = -74.00607; 
const R = 6371e3; // 지구의 반지름 (meter) 
// 좌표를 라디안 단위로 변환 
const φ1 = lat1 * Math.PI / 180; 
const φ2 = lat2 * Math.PI / 180; 
const Δφ = (lat2 - lat1) * Math.PI / 180; 
const Δλ = (lon2 - lon1) * Math.PI / 180; 
const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2); 
const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)); 
const d = R * c; // meter // d = 11052555.850341197







// 3

const hairColors = ['black', 'brown', 'yellow', 'white', 'gold']
const hairTypes = ['curly', 'straight', 'wavy', 'coily']
const glasses = [true, false]
const heights = [150, 160, 170, 180, 190, 200]
const weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

const person = []

const cPick = Math.floor(Math.random() * hairColors.length);
const cValue = hairColors[cPick]
const tPick = Math.floor(Math.random() * hairTypes.length);
const tValue = hairTypes[tPick]
const gPick = Math.floor(Math.random() * glasses.length);
const gValue = glasses[gPick]
const hPick = Math.floor(Math.random() * heights.length);
const hValue = heights[hPick]
const wPick = Math.floor(Math.random() * weights.length);
const wValue = weights[wPick]

while(hairColors.length > 0) {
    var inColors = hairColors.splice(Math.floor(Math.random() * hairColors.length),1)[0]
    person.push(inColors)
}

console.log(person)
console.log(`Hair Color: ${cValue}\nHair Types: ${tValue}\nWear Glasses: ${gValue}\nWeights: ${wValue}\nHeights: ${hValue}`)


