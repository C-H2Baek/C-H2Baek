function si() {
    var a = document.body.scrollTop || document.documentElement.scrollTop,
        b = document.documentElement.scrollHeight - document.documentElement.clientHeight,
        c = 100 * (a / b);
    document.getElementById("scroll").style.transform = `translateX(${c - 100}%)`,
    document.getElementById("percent").innerText = `${Math.floor(c)}%`
  }