let setting = {
    "number": true,
    "symbol": false,
    "capital": true,
    "small": true,
    "removeSimilar": false,
    "autoCopy": true,
    "length": 20
};
const pwoutput = document.getElementById("password");
let chars;

function init() {
    const storage = localStorage.getItem("pw-setting");

    storage && (
        setting = JSON.parse(storage)
    ),

    [...document.querySelectorAll("input[type=checkbox]")].forEach(input => {
        input.checked = setting[input.id]
    }),

    document.getElementById("pwlength").value = setting.length,

    updateChars()
}

function createChars() {
    let tmp = "";

    if (setting.number) {
        tmp = tmp + "0123456789"
    }
    if (setting.symbol) {
        tmp = tmp + "!@#$%^&*()-_=+"
    }
    if (setting.capital) {
        tmp = tmp + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
    if (setting.small) {
        tmp = tmp + "abcdefghijklmnopqrstuvwxyz"
    }
    if (setting.removeSimilar) {
        tmp = tmp.replace(/01|i|I|O/g, "")
    }

    return tmp;
}

function updateChars() {
    chars = createChars()
}

function saveSetting() {
    localStorage.setItem("pw-setting", JSON.stringify(setting))
}

init(),

document.getElementById("psbtn").addEventListener("click", () => {
    const length = chars.length;
    let password = "",
        tmp;

    for (let i = 0; i < setting.length; i++) {
        const random = Math.floor(Math.random() * length);
        tmp = chars.charAt(random);
        password = password + tmp
    }

    pwoutput.innerText = password;

    if (setting.autoCopy) {
        const select = document.createRange()
        select.selectNode(pwoutput),
        window.getSelection().removeAllRanges(),
        window.getSelection().addRange(select),
        document.execCommand("copy");
    }
}),

[...document.querySelectorAll(".settings")].forEach(a => {
    a.addEventListener("click", () => {
        const target = a.querySelector("input");

        setting[target.id] = target.checked,
        saveSetting(),
        updateChars()
    })
}),

document.getElementById("pwlength").addEventListener("change", function() {
    setting.length = this.value,
    saveSetting()
});