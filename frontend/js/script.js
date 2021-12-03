window.onload = loadView('')

function loadView (responseLogText = "No Text specified !") {
  document.getElementById('response-log').innerHTML = responseLogText
}

function testBackend () {
  fetch('/API')
    .then(function (response) {
      return response.text().then(function (text) {
        console.log(text)
        loadView(text)
      })
    })
    .catch(function (err) {
      // Une erreur est survenue
      console.log(err)
    })
}

function loadExample () {
  loadView("Load example is not implemented yet..")
}

function simulate () {
  loadView("Simulate is not implemented yet..")
}
