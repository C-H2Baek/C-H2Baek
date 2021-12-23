const fileInput = document.getElementById('file-input')
const imgBox = document.getElementById('img-box')

function isValid(type){
    return type.split('/')[0] === 'image'
}

function displayImg(src){
    console.log(src.split(':')[0])
    const srcPrefix = src.split(':')[0]
    if(srcPrefix === 'blob' ){
        imgBox.innerHTML += `<div class='img-item'><img src='${src}'/></div>`
    }else{
        imgBox.innerHTML += `<div class='img-item'><img src=${src}/></div>`
    }
    
}
function upload(file){
    const reader = new FileReader() // 사용자가 업로로드한 파일 데이터를 읽어오기 위한 파일 객체

    if(!isValid(file.type)){
        imgBox.innerHTML = 'File type is not valid !'
        return;
    }

    const src = URL.createObjectURL(file)
    displayImg(src) // 화면에 이미지를 보여주기

    reader.onload = rememberImg // 파일 읽기가 끝나면 rememberImg 를 실행함
    reader.readAsDataURL(file) // reader 객체가 파일을 읽어오기
}

function rememberImg(e){
    console.log(e.target.result) // reader 객체로 읽어온 데이터  (이미지 경로)
    const files = JSON.parse(localStorage.getItem('files')) || []
    if(files){
        const file = JSON.stringify(e.target.result)
        files.push(file)
    }
    localStorage.setItem('files', JSON.stringify(files))
}

function uploadImg(e){
    const files = e.target.files
    for(let file of files){
        upload(file)
    }
}

// 화면이 처음 로딩될때 로컬스토리지에 저장된 이미지를 보여주기
function renderImg(){
    imgBox.innerHTML = ''
    const files = JSON.parse(localStorage.getItem('files')) || []
  
    if(files.length > 0){
        for(let file of files){
            displayImg(file)
        }
    }
}

fileInput.addEventListener('change', uploadImg)
window.addEventListener('load', renderImg)