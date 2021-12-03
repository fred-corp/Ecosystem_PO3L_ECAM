let APIResponse = ''

window.onload = loadView()

function loadView () {
  document.getElementById('response-log').innerHTML = APIResponse
}

const form = document.getElementById('signup')

form.addEventListener('submit', function (event) {
  // stop form submission
  event.preventDefault()
  fetch('/API')
    .then(function (response) {
      return response.text().then(function (text) {
        console.log(text)
        APIResponse = text
        loadView()
      })
    })
    .catch(function (err) {
      // Une erreur est survenue
      console.log(err)
    })
})
