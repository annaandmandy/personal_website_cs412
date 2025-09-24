document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("toggleFormBtn");
    const form = document.getElementById("messageForm");

    if (btn && form) {
        btn.addEventListener("click", function() {
            form.classList.toggle("show")
        })
    }
})