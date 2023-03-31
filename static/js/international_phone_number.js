function getIp(callback) {
    fetch('https://ipinfo.io/json?token=23ad0afe5b81f9', { headers: { 'Accept': 'application/json' } })
        .then((resp) => resp.json())
        .catch(() => {
            return {
                country: 'BJ',
            };
        })
        .then((resp) => callback(resp.country));
}

const phoneInputField = document.querySelector("#id_tel");
const phoneInput = window.intlTelInput(phoneInputField, {
    preferredCountries: ["BJ", "CM", "CI", "TD"],
    initialCountry: "auto",
    geoIpLookup: getIp,
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

const info = document.querySelector(".alert-info");

function process(event) {
    event.preventDefault();

    const phoneNumber = phoneInput.getNumber();

    info.style.display = "";
    info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber}</strong>`;
}
