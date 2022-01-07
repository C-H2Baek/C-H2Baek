///// 2번

const companies = ['Samsung', 'LG', 'Google', 'Facebook', 'Amazon']
const companiesReversed = []

var popped = companies.pop()
while (popped !== undefined){
    companiesReversed.push(popped)
    popped = companies.pop()
}
console.log(companiesReversed)
///// 3번

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
const newFriends = [
    {name: 'Ami', aage: 27, city: 'ulsan'},
    {name: 'gracias', aage: 21, city: 'ulsan'},
]
console.log(friends)

const addfriends = friends.splice(2,0,...newFriends)
console.log(addfriends)

///// 4번 friends 에서 hannah 와 shara 를 제거

const removedfriends = friends.splice(4, 2)
console.log(removedfriends)

///// 5번 city가 seoul인 친구 제거

const removeseoul = friends.filter(friend => friend.city !=='seoul')
console.log(removeseoul)

///// 6번 나이 정렬

const sortedage = friends.sort((a, b) => a.age - b.age).filter(friend => friend.age <30)
console.log(sortedage)

///// 7번 이름 알파벳순

const sortedname = friends.sort((a,b) => {
    const aName = a.name.toLowerCase()
    const bName = b.name.toLowerCase()
    if(aName > bName) return 1
    if(aName > bName) return -1
    return 0
})
console.log(sortedname)

///// 8번 날짜순

const movies = [
    {title: 'Harry Potter', release: '2003-02-22'}, 
    {title: 'Indiana Jhones', release: '2009-01-09'}, 
    {title: 'Terminator', release: '2007-04-11'},
    {title: 'Dracula', release: '2007-04-13'},
    {title: 'Jurassic Park', release: '2007-05-13'},
    {title: 'Iron man', release: '2012-12-18'},
    {title: 'Spider man', release: '2017-03-07'}
]

movies.sort((a,b) => {
    const aRelease = a.release.split('-') // 2003-02-22 => ['2003', '02', '22']
    const bRelease = b.release.split('-') 
    const yearA = aRelease[0], monthA = aRelease[1], dayA = aRelease[2]
    const yearB = bRelease[0], monthB = bRelease[1], dayB = bRelease[2]
    // 년도 비교하기
    if(yearA < yearB) return 1
    if(yearA > yearB) return -1
    // 년도가 같으면 월을 비교
    if(monthA < monthB) return 1
    if(monthA > monthB) return -1
    //년도와 월이 같으면 일을 비교
    if(dayA < dayB) return 1
    if(dayA > dayB) return -1

    return 0
})
console.log(movies)

