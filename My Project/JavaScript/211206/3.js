const menuContainer = document.getElementById('menu-container')
let prevTarget = null 

function openMenu(e){
    const target = e.target
    
    if(prevTarget !== null){
        prevTarget.nextElementSibling.classList.remove('open')
    }

    if(target.className == 'title'){
        console.log(target.nextElementSibling)
        const infoDiv = target.nextElementSibling
        infoDiv.classList.add('open')
        prevTarget = target
    }
}

menuContainer.addEventListener('click', openMenu)