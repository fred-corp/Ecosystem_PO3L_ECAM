# Refernce of JSON ecosystem files

## Global file reference

```python
{
 "seed" : int s,                  # Random seed for the exosystem
 "fieldSize" : [int X, int Y],    # Size of the ecosystem
 "defaultHP" : int HP,            # Default healthpoints for (new) lifes
 "defaultFP" : int FP,            # Default foodpoints for (new) lifes
 "HPFPEquivalence" : int n,       # How much food points you get for one health point
 "organicwasteDropChance" : int c,# Probability for an animal to drop organic waste on each round
 "meatCompostAfter" : int n,      # How much rounds it takes for a piece of meat to compost
 "foodRestoreAmount" : int n,     # How much food points a piece of meat/organic waste restores
 "defaultVisionRadius" : int r,   # Vision radius for everyone
 "defaultContactRadius" : int r,  # Contact radius for everyone
 "defaultRootRadius" : int r,     # Root spread radius for everyone
 "defaultSeedRadius" : int r,     # Seed spread radius for everyone
 "startRandom" : bool s,          # Start the simulation with a random amount of lifes (must specify lifeforms in lifeDefaults) [not implemented yet]
 "keepHistory" : bool k,          # Wether all the rounds should be kept stored in the json or only the last
 "genders" : [str x, ...],        # List of genders
 "types" : [str t, ...],          # List of types of entities (for example carnivore, herbivore, plant, meat, organic waste)
 "lifeFormDefaults" : dict forms, # All lifeforms with their default values (see further dor forms reference)
 "rounds" : list rounds           # All the rounds with the different lifes (see further for rounds reference)
}
```

## Default lifeforms reference

TODO :

* add reference for plant, meat and organic waste

```python
{
 str key : {                   # Race of the lifeform
  "type": str s,               # type : references index to "type" array
  "color" : str C,             # HEX color code for EcoSym Viewer
  "symbol" : str S,            # Symbol of entity for EcoSym Viewer (emoji)
  "FP" : int f,                # Amount of foodpoints a food entity is worth (only for food (organic waste & meat))
  "lifespan" : int x,          # Lifespan of lifeform (only for animals & plants)
  "reproduceCooldown" : int x, # Number of rounds a lifeform must wait before mating and after which it gives birth when pregnant (only for animals) 
  "getsPregnant" : int x,      # Which gender gets pregnant (only for animals)
  "gestation" : int x,         # Number of rounds it takes for a newborn to develop (only for animals)
  "adultAt" : int x,           # age at which an animal or plant ca reproduce or spread seeds (only for animals & plants)
  "contactRadius" : int x,     # Contact radius (only for animals)
  "visionRadius" : int x,      # Vision radius (only for animals)
  "maxMove" : int x,           # Max move distance (only for animals)
  "rootRadius" : int r,        # Root spread radius (only for plants)
  "seedRadius" : int r         # Seed spread radius (only for plants)
 },
 ...
}

```

## Rounds list reference

```python
[
 [
  {"UUID" : str UUID,                     # UUID of entity
   "lifeform" : str LifeFormDefaultKEY,   # Reference to lifeFormDefaults, can be considered as "race"
   "posX" : int x,                        # X coordinated of entity
   "posY" : int y,                        # Y coordinates of entity
   "FP" : int f,                          # Current energy/food points
   "age" : int a,                         # Current age (only animals, plants & meat)
   "HP" : int h,                          # Current health points (only animals & plants)
   "gender" : int g,                      # Gender of animal, references index to "genders" array (only animals)
   "isPregnant" : int p,                  # Wether an animal is pregnant (1) or not (0) (only animals)
   "gestationCooldown" : int d            # How many "days" until a pregnant animal gives birth (only animals)
   "seedCooldown" : int c                 # How many days until a plant can spread seeds again after it has (only plants)
  },
  ...
 ],
 ...
]
```
