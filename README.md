# Hyperspace Emulator

This is a Repo of my Create task that I wrote in my Junior of High School for AP Computer Science Principles. It is intended to emulate a hyperdrive from Star Wars, using real world math combined with Star Wars lore math to determine how fast it would take to get to each planet.

## Overview

The Hyperspace Emulator is an interactive Python application that simulates traveling through hyperspace to different planets in our solar system. Using a unique blend of real-world astronomical distances and Star Wars lore-based calculations, this program calculates travel times and provides a visual experience of jumping between planets.

## Features

- **Interactive Navigation**: Choose any planet (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, or Pluto) to travel to
- **Accurate Distance Calculations**: Uses real astronomical data combined with Star Wars hyperdrive calculations
- **Visual Feedback**: Displays animated GIFs of the planets and lightspeed effects using Python's Turtle graphics library
- **Travel Time Estimation**: Calculates and displays how long it will take to reach your destination
- **Skip Option**: For longer journeys, optionally skip to the destination instead of watching the full travel animation
- **Travel Log**: Tracks all destinations visited during your session in `traveltimes.txt`

## Requirements

- Python 3.x
- `turtle` module (included in standard Python installation)

## Files

- **Main.py** - The main application file containing all the navigation and hyperspace travel logic
- **[Planet].gif** - Visual assets for each celestial body:
  - Earth.gif
  - Mercury.gif
  - Venus.gif
  - Mars.gif
  - Jupiter.gif
  - Saturn.gif
  - Uranus.gif
  - Neptune.gif
  - Pluto.gif
  - Sun.gif
  - lightspeed.gif (hyperspace effect)
  - Start.gif
- **traveltimes.txt** - Log file that records your travel destinations

## How to Run

```bash
python Main.py
```

Follow the on-screen prompts to select a destination. The program will calculate travel time and display an animation of your journey.

### Commands

- Enter a planet name (proper case): Travel to that planet
  - Valid destinations: Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
- Type **Orbit** to exit the program

## The Math

The Hyperspace Emulator uses the formula:

```
Travel Time = 50855.08 × Distance (in AU) × 10
```

Where:
- AU (Astronomical Unit) represents the distance from Earth to the Sun (~149.6 million km)
- The constant 50855.08 represents the Star Wars-based hyperdrive multiplier
- Distances are stored as fractional AUs for accurate calculations

This unique formula combines real-world orbital mechanics with Star Wars universe physics to create travel time estimates that feel authentic to the franchise while remaining grounded in actual celestial distances.

## Learning Outcomes

This project demonstrates:
- Python fundamentals (loops, conditionals, functions, file I/O)
- Data structures (dictionaries, lists)
- Graphics programming with Turtle
- Mathematical calculations and formulas
- Event-driven programming
- Creative problem-solving (blending real science with fiction)

## Usage Example

```
Where would you like to go? 
Use proper case please.
Type Orbit to exit. Mars

That will take 50.21 seconds
Approaching destination
49.211 seconds left
...
You have arrived at Mars
```

## Notes

- The program stores your travel history in `traveltimes.txt`
- Some longer journeys (to outer planets) may take several minutes in real-time unless you choose to skip
- The visual animations use Python's Turtle graphics library for a unique retro-style interface
- This was created as an educational project for AP Computer Science Principles

## Future Improvements

Possible enhancements to this project could include:
- Refactoring to reduce code repetition for each planet
- More sophisticated graphics and animations
- Additional planets and star systems
- Customizable hyperdrive settings
- Better data validation and error handling

---

*Created by awesomeshot5051 in 2024*
