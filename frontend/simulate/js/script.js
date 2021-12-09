window.onload = loadView('')

function loadView (responseLogText = 'No Text specified !') {
  document.getElementById('response-log').innerHTML = responseLogText
}

document.getElementById('load-example').addEventListener('click', function () { loadExample() })
document.getElementById('simulate').addEventListener('click', function () { simulate() })
document.getElementById('post-json').addEventListener('click', function () { postJson() })
document.getElementById('test-backend').addEventListener('click', function () { testBackend() })

// Test the connection with backend/API
function testBackend () {
  fetch('/pingAPI')
    .then(function (response) {
      return response.text().then(function (text) {
        loadView(text)
      })
    })
    .catch(function (err) {
      console.log(err)
    })
}

// Load example ecosystem
function loadExample () {
  loadView('Load example is not implemented yet..')
}

// Simulate the next step of the ecosystem
function simulate () {
  loadView('Simulate is not implemented yet..')
}

// Test function to see how a JSON object can get sent to and from a backend
function postJson () {
  const payload = {
    message: 'A simple payload',
    response: ''
  }

  const data = new FormData()
  data.append('json', JSON.stringify(payload))
  console.log(data)

  fetch('/API',
    {
      method: 'POST',
      body: data
    })
    .then(function (res) { return res.json() })
    .then(function (data) { alert(JSON.stringify(data)) })
}
