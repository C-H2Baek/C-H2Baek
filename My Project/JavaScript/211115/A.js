const li_collection = document.getElementsByTagName('li') 
Array.from(li_collection).forEach(li => {
     li.addEventListener('click', function() {
          alert(this.firstElementChild.alt)
    }) 
});
