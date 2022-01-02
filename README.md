# EcoSym

[![Website shields.io](https://img.shields.io/website-up-down-green-red/https/ecosym.fredcorp.cc/ping)](https://ecosym.fredcorp.cc)
![checkout workflow](https://github.com/fred-corp/Ecosystem_PO3L_ECAM/actions/workflows/checkout.yml/badge.svg)

Visit the [EcoSym website](https://ecosym.fredcorp.cc) for a live demo !

By Frédéric Druppel (18053) and Lancelot Neirinckx (18206)

## Table of contents

- [EcoSym](#ecosym)
- [Recursivity](#table-of-contents)
- [Preambule](#preambule)
- [Usage](#usage)
- [UML Diagrams](#uml-diagrams)
  - [Class diagram](#class-diagram)
  - [Sequence diagram](#sequence-diagrams)
- [SOLID principles justification](#solid-principles-justification)
  - [Single-responsibility principle](#single-responsibility-principle)
  - [Open–closed principle](#open–closed-principle)
- [Sources](#sources)

## Preambule

This project was created as part of a 3rd year industrial engineering programming course at ECAM Brussels Engineering school. The project requirements can be found on [this website](https://quentin.lurkin.xyz/courses/poo/projet2021/index.html) (in french).

As we could choose the language the project was written in, we chose Python as we're familiar with it, and it's fast to write working code and deploy it on a Linux server.  
In order to make everything faster, javascript or C++ could be used for the backend, but we didn't have the time to play around with that.

A PyGame fork of the project exists in the [pygame branch](https://github.com/fred-corp/Ecosystem_PO3L_ECAM/tree/pygame) of this repo, feel free to give it a try !

The GUI for this project was completely optionnal, and we won't get points for it, so why did we bother designing a *complete* website ? Well, why not !  
It gave us the opportunity to debug a lot of issues during development, and was a way to learn javascript and frontend-backend communication. Plus, it now serves as a neat visualisation of the ecosystem simulation.  
The self-hosted [EcoSym website](https://ecosym.fredcorp.cc) runs on a server in a basement, which automatically updates itself when a new push is made to this repo; yet another learning opportunity for us !

## Usage

Open folder in a terminal.  
Verify your python version, it sould be 3.9 at least :

```zsh
$ python3 --version
Python 3.9.1
```

Install requirements :

```zsh
$ pip3 install -r requirements.txt
```

Go into the backend directory :

```zsh
$ cd backend
```

Launch the server:

```zsh
$ python3 server.py "0.0.0.0"
```

Navigate to `localhost:3000`

> You can also visit the [EcoSym website](https://ecosym.fredcorp.cc) for a live demo !

On the EcoSym website, you can then go to the "simulate" tab, load the example, and then run the simulation.  
More details about the syntax of the example JSON file can be found in the [ecosystemExampleFiles](/ecosystemExampleFiles) folder.

If you run your own instance of the EcoSym simulator, you can change the example JSON (without changing its name) and simply click the "load example" button on the locally hosted website.  
The website may one day have an "upload custom ecosystem file" button, but we didn't have the time to implement that.

Once the example is loaded, you can see a grid with the entities (with corresponding background colors and symbols), each of which you can click to see more info about them.  
You'll also see a collapsable list of the entities next to the grid. This list displays the "lifeform" param of the entities, and if you click on a list item, the corresponding entity is highlighted on the simulation grid in order to track it during the simulation. The tracker can be cleared by ckicking on the list item again.

> Note : the website is best viewed on a computer, but has been optimised as much as possible to run on a mobile device. Nevertheless, your mileage may vary.

## UML Diagrams

The raw PlantUML files can be found in the [diagrams](development/diagrams) folder in [development](development).

### Class diagram

![class diagram](/development/diagram-images/class.png)

### Carnivore sequence diagram

![sequence diagram](/development/diagram-images/carnivore-transparent.png)

## SOLID principles justification

### Single-responsibility principle

"There should never be more than one reason for a class to change."

Each class has it's own responsability. For example a `Plant` object can only act as a plant in the ecosystem. It has it's own methods to get a root zone or a seed zone which are specific to the class responsability.

### Open–closed principle

"Software entities ... should be open for extension, but closed for modification."

Let's take the `Animal` class as an example. If we need to create a new animal, we do not need to modify code inside the `Animal` class but just extend it. For example the `get_contact_zone()` method will return a zone based on `contact_zone` which is a parameter defined by the extended class.

## Sources

- Project requirements : ["PO3L - Projet" on Quentin Lurkin's website](https://quentin.lurkin.xyz/courses/poo/projet2021/index.html)
- [W3schools](https://www.w3schools.com)
- [StackOverflow](https://stackoverflow.com)
- SOLID principles : [Wikipedia](https://en.wikipedia.org/wiki/SOLID)

Made with ❤️, lots of ☕️, and lack of 🛌  
Published under CreativeCommons BY-NC-SA 4.0

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
