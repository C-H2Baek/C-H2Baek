const photoContainer = document.querySelector('.photo-container')

function hideImg(){
    photoContainer.classList.remove('show')
}

function showImg(){
    photoContainer.classList.add('show')
    setTimeout(hideImg, 3000)
}

function startEffect(){
    setTimeout(showImg, 1000)
}


window.addEventListener('load', startEffect)