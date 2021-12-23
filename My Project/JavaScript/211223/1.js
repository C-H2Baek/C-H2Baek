const contents = document.querySelectorAll('.contents')
const up = document.getElementsByClassName('.contents up')
const down = document.getElementsByClassName('.contents down')
// const img = document.createElement("img")
// img.src = "../../../Images/main_img.jpg"
// const src = document.getElementById("section")
// src.appendChild(img)
// section.style.backgroundImage = "url('../../../Images/main_img.jpg')"

function startAnimation() {
    
    for (let content of contents) {
        console.log(content.getBoundingClientRect().top)
        if (!content.classList.contains('show') && content.getBoundingClientRect().top < 300) {
            content.classList.add('show')
            
        }
    }
}

window.addEventListener('scroll', startAnimation)