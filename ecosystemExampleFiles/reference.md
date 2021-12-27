# Refernce of JSON ecosystem files

## Global file reference

```python
{
 "seed" : int s,                 # Random seed for the exosystem
 "fieldSize" : [int X, int Y],   # Size of the ecosystem
 "defaultHP" : int HP,           # Default healthpoints for (new) lifes
 "defaultFP" : int FP,           # Default foodpoints for (new) lifes
 "starveAfter" : int n,          # Remove 1 FP after n amount of rounds
 "HPFPEquivalence" : int n,      # How much food points you get for one health point
 "meatCompostAfter" : int n,     # How much rounds it takes for a piece of meat to compost
 "foodRestoreAmount" : int n,    # How much food points a piece of meat/organic waste restores
 "defaultVisionRadius" : int r,  # Vision radius for everyone
 "defaultContactRadius" : int r, # Contact radius for everyone
 "defaultRootRadius" : int r,    # Root spread radius for everyone
 "defaultSeedRadius" : int r,    # Seed spread radius for everyone
 "startRandom" : bool s,         # Start the simulation with a random amount of lifes (must specify lifeforms in lifeDefaults)
 "genders" : [str x, ...],       # List of genders
 "type" : [str t, ...],          # List of type eof entities (for example carnivore, herbivore, plant, meat, organic waste)
 "lifeDefaults" : dict forms,    # All lifeforms with their default values (see further dor forms reference)
 "rounds" : list rounds          # All the rounds with the different lifes (see further for rounds reference)
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
  "diet" : int x,              # 0 : Herbivorous, 1 : Carnivorous, 2 : Omnivorous
  "lifespan" : int x,          # Lifespan of lifeform
  "reproduceCooldown" : int x, # Number of rounds a lifeform must wait before mating/spreading seeds again
  "getsPregnant" : int x,      # Which gender gets pregnant
  "gestation" : int x          # Number of rounds it takes for a newborn to develop/a seed to grow to a plant,
  "contactRadius" : int x,     # Contact radius
  "visionRadius" : int x,      # Vision radius
  "maxMove" : int x            # Max move distance
 },
 ...
}

```

## Rounds list reference

```python
[
 [str UUID, str lifeform, int gender, int isPregnant, int gestationCooldown, int age, int HP, int FP, int X, int Y],
 ...
]
```
