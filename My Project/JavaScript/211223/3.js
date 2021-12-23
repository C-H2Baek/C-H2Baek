const fileInput = document.getElementById('file-input')
const imgBox = document.getElementById('img-box')

function isVaild(type){
    return type.split('/')[0] === 'image'
}

function displayImg(file){
    const img = document.createElement('img')

    // 로컬 스토리지로 저장한 파일을 읽어 온 경우
    if(typeof file === 'string'){
        img.src = file
    }
    // 사용자가 처음 업로드한 파일
    else{
        img.src = URL.createObjectURL(file)
    }
    imgBox.appendChild(img)
}

function rememberImg(e){
    console.log(JSON.stringify(e.target.result)) // reader 객체로 읽어온 데이터(이미지 경로)
    localStorage.setItem('file', JSON.stringify(e.target.result))
}

function uploadImg(e){
    const file = e.target.files[0]
    const reader = new FileReader() // 사용자가 업로드한 파일 데이터를 읽어오기 위한 파일 객체

    if(!isVaild(file.type)){
        imgBox.innerHTML = 'File type is not valid !'
        return;
    }

    displayImg(file) // 화면에 이미지를 보여주기

    reader.onload = rememberImg // 파일 읽기가 끝나면 rememberImg
    reader.readAsDataURL(file) // reader 객체가 파일을 읽어오기
}

function renderImg(){
    const fileStored = JSON.parse(sessionStorage.getItem('file'))

    if(fileStored){
        displayImg(fileStored)
    }
}


fileInput.addEventListener('change', uploadImg)
window.addEventListener('load', renderImg)