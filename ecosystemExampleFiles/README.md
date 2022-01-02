# Example ecosystems

> See ```reference.md``` for exact syntax of the JSON files.

Use these examples to run simulations of ecosystems, or use the examples to create your own.

An ecosystem file must have at least those parameters (values can be changed):

```javascript
{
 "seed" : -85393517611233,
 "fieldSize" : [50, 50],
 "defaultHP" : 20,
 "defaultFP" : 20,
 "HPFPEquivalence" : 20,
 "organicwasteDropChance" : 20,
 "meatCompostAfter" : 10,
 "foodRestoreAmount" : 2,
 "defaultVisionRadius" : 12,
 "defaultContactRadius" : 3,
 "defaultRootRadius" : 10,
 "defaultSeedRadius" : 8,
 "startRandom" : false,
 "keepHistory" : false,
 "genders" : ["female", "male", "hermaphrodite"],
 "types" : ["carnivore", "herbivore", "plant", "meat", "organicwaste"], // Imposed, can't be changed without modifying simulation code
 "lifeFormDefaults" : {},
 "rounds" : []
}
```

```"lifeFormDefaults"``` must have at least those parameters (values can be changed):

```javascript
  "meat" : {
   "type" : 3,
   "color" : "#aa1111",
   "symbol" : "🥩",
   "FP" : 10
  },
  "organicwaste" : {
   "type" : 4,
   "color" : "#f0f0f0",
   "symbol" : "♻️",
   "FP" : 15
  }
```

```rounds``` must have the starting configuration of the ecosystem (see [example1.json](example1.json)) (at least until ```startRandom``` gets implemented).  
An example may look like this :

```javascript
  [
   {"UUID" : "7f973152-f44a-4f85-99d4-d9ebd1d127f3", "lifeform" : "oak", "posX" : 5, "posY" : 46, "age" : 0, "HP" : 20, "FP" : 20, "seedCooldown" : 0},
   {"UUID" : "a04a8da4-8946-4dbe-a378-6e897e4584bb", "lifeform" : "carrot", "posX" : 45, "posY" : 46, "age" : 0, "HP" : 20, "FP" : 20, "seedCooldown" : 0},
  ]
```

> Note : each lifeform should have its defaults set in ```lifeFormDefauls``` as can be seen in the [example1.json](example1.json) ecosystem
