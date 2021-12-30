window.onload = loadView('')

function loadView (responseLogText = 'No Text specified !') {
  document.getElementById('response-log').innerHTML = responseLogText
}

document.getElementById('load-example').addEventListener('click', function () { loadExample() })
document.getElementById('simulate').addEventListener('click', function () { simulate() })

let ecoSymDict = {}

// Load example ecosystem
function loadExample () {
  window.fetch('/API/load')
    .then(function (res) { return res.json() })
    .then(function (data) {
      ecoSymDict = data
      displayGrid(ecoSymDict)
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
        if (population[i].posX === x && population[i].posY === y) {
          if (cell.innerText === '' || _data.lifeFormDefaults[population[i].lifeform].type < 3) {
            cell.innerText = _data.lifeFormDefaults[population[i].lifeform].symbol
            cell.style.cssText = 'background-color: ' + _data.lifeFormDefaults[population[i].lifeform].color + ';'
            cell.onclick = (function (entity) {
              return function () {
                let text = ''
                text = 'UUID : ' + entity.UUID + '\n'
                text += 'Symbol : ' + _data.lifeFormDefaults[entity.lifeform].symbol + '\n'
                text += 'Lifeform : ' + entity.lifeform + '\n'
                if (typeof _data.genders[entity.gender] !== 'undefined') {
                  text += 'Gender : ' + _data.genders[entity.gender] + '\n'
                  if (entity.gender === _data.lifeFormDefaults[entity.lifeform].getsPregnant) {
                    text += 'Pregnant : ' + entity.isPregnant + '\n'
                    text += 'UntilBirth : ' + entity.gestationCooldown + '\n'
                  }
                }
                if (typeof entity.age !== 'undefined') { text += 'Age : ' + entity.age + '\n' }
                if (typeof entity.HP !== 'undefined') { text += 'HP : ' + entity.HP + '\n' }
                text += 'FP : ' + entity.FP
                window.alert(text)
              }
            })(population[i])
          }
        }
      }
      container.appendChild(cell).className = 'grid-item'
    }
  }
}

// Simulate the next step of the ecosystem
const simulate = async() => {
  if (!Object.keys(ecoSymDict).length) {
    loadView('Load an example first !')
  } else {
    const payload = ecoSymDict
    const data = new FormData()
    data.append('json', JSON.stringify(payload))
    await fetch('/API/simulate',
      {
        method: 'POST',
        body: data
      })
      .then(function (res) { return res.json() })
      .then(function (data) {
        ecoSymDict = data
        loadView('')
        displayGrid(ecoSymDict)
      })
  }
}
