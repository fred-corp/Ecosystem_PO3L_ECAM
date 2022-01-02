# Ecosystem

[![Website shields.io](https://img.shields.io/website-up-down-green-red/https/ecosym.fredcorp.cc/ping)](https://ecosym.fredcorp.cc)
![checkout workflow](https://github.com/fred-corp/Ecosystem_PO3L_ECAM/actions/workflows/checkout.yml/badge.svg)

> Visit the [EcoSym website](https://ecosym.fredcorp.cc) for a live demo !

## TODO

- [ ] work on issues
- [ ] write report
- [ ] sleep

## Usage

Launch the server:

```python
python3 server.py "0.0.0.0"
```

Navigate to `localhost:3000`

> You can also still visit the [EcoSym website](https://ecosym.fredcorp.cc) for a live demo !

## UML Diagrams

### Class diagram

![class diagram](/development/class.png)

### Sequence diagram

```![sequence diagram](/development/sequence.png)```

## SOLID principles justification

### Single-responsibility principle

> "There should never be more than one reason for a class to change."

Each class has it's own responsability. For example a `Plant` object can only act as a plant in the ecosystem. It has it's own methods to get a root zone or a seed zone which are specific to the class responsability.

### Open–closed principle

> "Software entities ... should be open for extension, but closed for modification."

Let's take the `Animal` class as an example. If we need to create a new animal, we do not need to modify code inside the `Animal` class but just extend it. For example the `get_contact_zone()` method will return a zone based on `contact_zone` which is a parameter defined by the extended class.

## Sources

- Project requirements : ["PO3L - Projet" on Quentin Lurkin's website](https://quentin.lurkin.xyz/courses/poo/projet2021/index.html)
- [W3schools](https://www.w3schools.com)
- [StackOverflow](https://stackoverflow.com)
- SOLID principles : [Wikipedia](https://en.wikipedia.org/wiki/SOLID)

A different implementation based on pygame can be found in the `pygame` branch.

Made with ❤️, lots of ☕️, and lack of 🛌  
Published under CreativeCommons BY-NC-SA 4.0

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
