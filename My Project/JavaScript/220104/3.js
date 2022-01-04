///// 2번

const companies = ['Samsung', 'LG', 'Google', 'Facebook', 'Amazon']
const companiesReversed = []

console.log(companies.reverse())

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

friends.splice(2,0,...newFriends)
console.log(friends)

///// 4번 friends 에서 hannah 와 shara 를 제거

const removedfriends = friends.splice(4, 2)

console.log(friends)
console.log(removedfriends)

///// 5번 city가 seoul인 친구 제거

const removeseoul = friends.splice(friends.indexOf('seoul'),1)
console.log(removeseoul)