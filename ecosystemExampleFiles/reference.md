# Refernce of JSON ecosystem files

## Global file reference

```python
{
 "seed" : int s,               # Random seed for the exosystem
 "fieldSize" : [int X, int Y], # Size of the ecosystem
 "defaultHP" : int HP,         # Default healthpoints for (new) lifes
 "defaultFP" : int FP,         # Default foodpoints for (new) lifes
 "starveAfter" : int n,        # Remove 1 FP after n amount of rounds
 "HPFPEquivalence" : int n,    # How much food points you get for one health point
 "meatCompostAfter" : int n,   # How much rounds it takes for a piece of meat to compost
 "foodRestoreAmount" : int n, # How much food points a piece of meat/organic waste restores
 "visionRadius" : int r,       # Vision radius for everyone
 "contactRadius" : int r,      # Contact radius for everyone
 "rootRadius" : int r,         # Root spread radius for everyone
 "seedRadius" : int r,         # Seed spread radius for everyone
 "startRandom" : bool s,       # Start the simulation with a random amount of lifes (must specify lifeforms in lifeDefaults)
 "lifeDefaults" : dict forms,  # All lifeforms with their default values (see further dor forms reference)
 "rounds" : list rounds        # All the rounds with the different lifes (see further for rounds reference)
}
```

## Default lifeforms reference

```python
{
 str key : {                   # Race of the lifeform
  "species": str s,            # Species : animal or vegetal
  "color" : str C,             # HEX color code for EcoSym Viewer
  "diet" : int x,              # 0 : Herbivorous, 1 : Carnivorous, 2 : Omnivorous
  "lifespan" : int x,          # Lifespan of lifeform
  "reproduceCooldown" : int x, # Number of rounds a lifeform must wait before mating/spreading seeds again
  "gestation" : int x,         # Number of rounds it takes for a newborn to develop/a seed to grow to a plant
  "hierarchy" : int x          # Hierarchy of the lifeform. A higher hierarchy lifeform can eat a lower hierarchy lifeform,
  "foodDropAmount" : int x     # Amount of food pieces dropped (meat or organic waste)
 },
 ...
}

```

## Rounds list reference

```python
[
 [str UUID, str lifeform, int gender, bool isPregnant, int cooldown, int age, int HP, int FP, int X,  int Y],
 ...
]
```
