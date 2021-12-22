const fileInput = document.getElementById('file-input')
const imgBox = document.getElementById('img-box')
const uploadBtn = document.getElementById('upload')

function isValid(type){
    console.log(type.split('/')[0])
    return type.split('/')[0] === 'image'
}

function displayImg(e){
    console.log(e.target.files)
    const files = e.target.files

    for(let file of files){
        // file.type : 'image/jpeg'
        // 이미지가 아닌 경우
        if(!isValid(file.type)){
            imgBox.innerHTML = 'File is not valid !'
            return;
        }

        const img = document.createElement('img')
        img.src = URL.createObjectURL(file) // 이미지 경로를 생성해줌
        img.alt = file.name
        img.className = 'photo-uploaded'
        imgBox.appendChild(img)
    }
}
function openFileWindow(){
    fileInput.click()
}

fileInput.addEventListener('change', displayImg)
uploadBtn.addEventListener('click', openFileWindow)