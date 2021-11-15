const a_collection = document.getElementsByTagName('a')
Array.from(a_collection).forEach(a => {
    a.addEventListener('click', function() {
        alert(this.firstElementChild.alt)
    })
});