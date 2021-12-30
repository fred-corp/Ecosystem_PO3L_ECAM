window.onload = loadView('')

function loadView (responseLogText = 'No Text specified !') {
  document.getElementById('response-log').innerHTML = responseLogText
}

let ecoSymDict = {}

document.getElementById('load-example').addEventListener('click', function () { loadExample() })
document.getElementById('simulate').addEventListener('click', function () { simulate() })
document.getElementById('start-auto').addEventListener('click', function () { startAutoSimulate() })
document.getElementById('pause-auto').addEventListener('click', function () { pauseAutoSimulate() })

// Load example ecosystem
function loadExample () {
  window.fetch('/API/load')
    .then(function (res) { return res.json() })
    .then(function (data) {
      ecoSymDict = data
      displayGrid(ecoSymDict)
      displayList(ecoSymDict)
      pauseAutoSimulate()
    })
}

const gridContainer = document.getElementById('simulation-grid')

function displayGrid (_data) {
  gridContainer.innerHTML = ''
  const rows = _data.fieldSize[1]
  const cols = _data.fieldSize[0]
  const population = _data.rounds[_data.rounds.length - 1]
  gridContainer.style.setProperty('--grid-rows', rows)
  gridContainer.style.setProperty('--grid-cols', cols)
  for (let y = rows-1; y >= 0; y--) {
    for (let x = 0; x < cols; x++) {
      const cell = document.createElement('div')
      for (let i = 0; i < population.length; i++) {
        if (population[i].posX === x && population[i].posY === y) {
          if (cell.innerText === '' || _data.lifeFormDefaults[population[i].lifeform].type < 3) {
            cell.innerText = _data.lifeFormDefaults[population[i].lifeform].symbol
            cell.style.cssText = 'background-color: ' + _data.lifeFormDefaults[population[i].lifeform].color + ';'
            cell.id = population[i].UUID
            cell.onclick = (function (entity) {
              return function () {
                let text = ''
                text = 'UUID : ' + entity.UUID + '\n'
                text += 'Symbol : ' + _data.lifeFormDefaults[entity.lifeform].symbol + '\n'
                text += 'Lifeform : ' + entity.lifeform + '\n'
                text += "Position X : " + entity.posX + '\n'
                text += "Position Y : " + entity.posY + '\n'
                if (typeof _data.genders[entity.gender] !== 'undefined') {
                  text += 'Gender : ' + _data.genders[entity.gender] + '\n'
                  if (entity.gender === _data.lifeFormDefaults[entity.lifeform].getsPregnant && entity.age >= _data.lifeFormDefaults[entity.lifeform].adultAt) {
                    text += 'Pregnant : ' + entity.isPregnant + '\n'
                    text += 'UntilBirth : ' + entity.gestationCooldown + '\n'
                  }
                }
                if (typeof entity.age !== 'undefined') { text += 'Age : ' + entity.age + '\n' }
                if (typeof entity.seedCooldown !== 'undefined' && entity.age >= _data.lifeFormDefaults[entity.lifeform].adultAt) { text += 'Seed cooldown left : ' + entity.seedCooldown + '\n' }
                if (typeof entity.HP !== 'undefined') { text += 'HP : ' + entity.HP + '\n' }
                text += 'FP : ' + entity.FP
                window.alert(text)
              }
            })(population[i])
          }
        }
      }
      gridContainer.appendChild(cell).className = 'grid-item'
    }
  }
}

const listContainer = document.getElementById('simulation-list')

function displayList(_data){
  let list = {}
  _data.types.forEach(element => {
    list[element] = []
  })
  const population = _data.rounds[_data.rounds.length - 1]
  population.forEach(entity => {
    list[_data.types[_data.lifeFormDefaults[entity.lifeform].type]].push(entity)
  })

  listContainer.innerHTML = ''
  var mainList = document.createElement('ul')
  mainList.id = 'entityUL'
  var mainListContainer = document.createElement('li')
  var mainListNameSpan = document.createElement('span')
  mainListNameSpan.className = 'caret'
  mainListNameSpan.appendChild(document.createTextNode('Entities'))
  mainListContainer.appendChild(mainListNameSpan)
  
  var subList = document.createElement('ul')
  subList.className = 'nested'
  _data.types.forEach(element => {
    var subListContainer = document.createElement('li')
    var subListNameSpan = document.createElement('span')
    subListNameSpan.className = 'caret'
    subListNameSpan.appendChild(document.createTextNode(element))
    subListContainer.appendChild(subListNameSpan)
  
    let entityList = document.createElement('ul')
    entityList.className = 'nested'
    list[element].forEach(entity => {
      let entityListName = document.createElement('li')
      entityListName.appendChild(document.createTextNode(entity.UUID))
      entityList.appendChild(entityListName)
    })

    subListContainer.appendChild(entityList)
    subList.appendChild(subListContainer)
  })
  
  mainListContainer.appendChild(subList)
  mainList.appendChild(mainListContainer)
  listContainer.appendChild(mainList)
  updateCollapsableList()
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

var autoPlayID

function startAutoSimulate() {
  if(autoPlayID == null){
    autoPlayID = setInterval(simulate, 2000)
  }
}

function pauseAutoSimulate() {
  clearInterval(autoPlayID)
  autoPlayID = null
}


// Collapsable entity list handler
function updateCollapsableList () {
const toggler = document.getElementsByClassName('caret')
  for (var i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener('click', function() {
      console.log('aaa')
      this.parentElement.querySelector('.nested').classList.toggle('active')
      this.classList.toggle('caret-down')
    })
  }
}
