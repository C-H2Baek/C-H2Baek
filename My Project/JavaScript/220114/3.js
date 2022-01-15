const mapObj = L.map('map')

const coordinates = [
    {
        "name": "조선 팰리스 럭셔리 컬렉션 호텔, 서울 강남 (Josun Palace, a Luxury Collection Hotel, Seoul Gangnam)",
        "coordinate": [
            37.502642,
            127.041787
        ]
    },
    {
        "name": "그랜드 인터컨티넨탈 서울 파르나스 (Grand InterContinental Seoul Parnas, an IHG Hotel)",
        "coordinate": [
            37.50846,
            127.061036
        ]
    },
    {
        "name": "인터컨티넨탈 서울 코엑스 (InterContinental Seoul COEX, an IHG Hotel)",
        "coordinate": [
            37.513481,
            127.057276
        ]
    },
    {
        "name": "파크 하얏트 서울 (Park Hyatt Seoul)",
        "coordinate": [
            37.50845,
            127.06335
        ]
    },
    {
        "name": "안다즈 서울 강남 (Andaz Seoul Gangnam)",
        "coordinate": [
            37.525265,
            127.028627
        ]
    },
    {
        "name": "글래드 라이브 강남 (Glad Live Gangnam)",
        "coordinate": [
            37.528184,
            127.036514
        ]
    }
]

function displayLocation(lat, lon, msg){
    const map = mapObj.setView([lat, lon], 13)

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map)

    L.marker([lat, lon]).addTo(map)
        .bindPopup(msg)
        .openPopup()
}

coordinates.forEach(coord => {
    displayLocation(coord.coordinate[0], coord.coordinate[1], coord.name)
})