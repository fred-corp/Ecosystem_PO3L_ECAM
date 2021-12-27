# Refernce of JSON ecosystem files

## Global file reference

```python
{
 "seed" : int s,                  # Random seed for the exosystem
 "fieldSize" : [int X, int Y],    # Size of the ecosystem
 "defaultHP" : int HP,            # Default healthpoints for (new) lifes
 "defaultFP" : int FP,            # Default foodpoints for (new) lifes
 "starveAfter" : int n,           # Remove 1 FP after n amount of rounds
 "HPFPEquivalence" : int n,       # How much food points you get for one health point
 "meatCompostAfter" : int n,      # How much rounds it takes for a piece of meat to compost
 "foodRestoreAmount" : int n,     # How much food points a piece of meat/organic waste restores
 "defaultVisionRadius" : int r,   # Vision radius for everyone
 "defaultContactRadius" : int r,  # Contact radius for everyone
 "defaultRootRadius" : int r,     # Root spread radius for everyone
 "defaultSeedRadius" : int r,     # Seed spread radius for everyone
 "startRandom" : bool s,          # Start the simulation with a random amount of lifes (must specify lifeforms in lifeDefaults)
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
  "type": str s,               # type : references to "type" array
  "color" : str C,             # HEX color code for EcoSym Viewer
  "lifespan" : int x,          # Lifespan of lifeform (only for animals & plants)
  "reproduceCooldown" : int x, # Number of rounds a lifeform must wait before mating (only for animals)
  "getsPregnant" : int x,      # Which gender gets pregnant (only for animals)
  "gestation" : int x,         # Number of rounds it takes for a newborn to develop (only for animals)
  "adultAt" : int x,           # age at which an animal or plant ca reproduce or spread seeds
  "contactRadius" : int x,     # Contact radius (only for animals)
  "visionRadius" : int x,      # Vision radius (only for animals)
  "maxMove" : int x,           # Max move distance (only for animals)
  "rootRadius" : int r,        # Root spread radius (only for plants)
  "seedRadius" : int r,        # Seed spread radius (only for plants)
 },
 ...
}

```

## Rounds list reference

```python
[
 [
  {"UUID" : str UUID,
   "lifeform" : str LifeFormDefaultKEY,
   "posX" : int x,
   "posY" : int y,
   "age" : int a,
   "HP" : int h,               # only animals & plants
   "FP" : int f,               # only animals & plants
   "gender" : int g,           # only animals
   "isPregnant" : int p,       # only animals,
   "gestationCooldown" : int d # only animals
  },
  ...
 ],
 ...
]
```
