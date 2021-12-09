window.onload = loadView('')

function loadView (responseLogText = 'No Text specified !') {
  document.getElementById('response-log').innerHTML = responseLogText
}

document.getElementById('load-example').addEventListener('click', function () { loadExample() })
document.getElementById('simulate').addEventListener('click', function () { simulate() })
// document.getElementById('post-json').addEventListener('click', function () { postJson() })
// document.getElementById('test-backend').addEventListener('click', function () { testBackend() })

// Test the connection with backend/API
/*
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
*/

// Load example ecosystem
function loadExample () {
  fetch('/API/load')
    .then(function (res) { return res.json() })
    .then(function (data) {
      displayGrid(data)
    })
}

const container = document.getElementById('simulation-grid')

function displayGrid (_data) {
  container.innerHTML = ''
  const rows = _data.fieldSize[1]
  const cols = _data.fieldSize[0]
  const population = _data.rounds[_data.rounds.length - 1]
  container.style.setProperty('--grid-rows', rows)
  container.style.setProperty('--grid-cols', cols)
  for (let y = cols - 1; y >= 0; y--) {
    for (let x = 0; x < rows; x++) {
      const cell = document.createElement('div')
      for (let i = 0; i < population.length; i++) {
        if (population[i][8] === x && population[i][9] === y) {
          cell.style.cssText = 'background-color: ' + _data.lifeDefaults[population[i][1]].color + ';'
          cell.onclick = (function (entity) {
            return function () {
              let text = ''
              text = 'UUID : ' + entity[0] + '\n'
              text += 'Lifeform : ' + entity[1] + '\n'
              text += 'Gender : ' + _data.genders[entity[2]] + '\n'
              if (entity[2] === _data.lifeDefaults[entity[1]].getsPregnant) {
                text += 'Pregnant : ' + entity[3] + '\n'
              }
              text += 'Age : ' + entity[5] + '\n'
              text += 'HP : ' + entity[6] + '\n'
              text += 'FP : ' + entity[7]
              alert(text)
            }
          })(population[i])
        }
      }
      cell.innerText = ''
      container.appendChild(cell).className = 'grid-item'
    }
  }
}

// Simulate the next step of the ecosystem
function simulate () {
  loadView('Simulate is not implemented yet..')
}

// Test function to see how a JSON object can get sent to and from a backend
/*
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
*/
