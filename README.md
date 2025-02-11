# Car Lights Simulation

A Python-based interactive car lights simulation using the Turtle graphics library. This program creates a visual representation of a car's front headlights, rear lights, and turning signals with user-controlled functionality.

## Description

This simulation creates four light assemblies representing a car's lighting system:
- Two front light assemblies (left and right) with:
  - Main headlights (white)
  - Turn signals (yellow)
- Two rear light assemblies (left and right) with:
  - Brake lights (red)
  - Turn signals (yellow)

## Features

- Interactive light control through user input
- Front headlights with white illumination
- Rear lights with red illumination
- Synchronized turning signals on all four corners
- Blinking turn signal animation
- Black background for better visibility
- Custom-sized light elements
- Distinctive light housing designs (white for front, red for rear)

## Prerequisites

To run this simulation, you need:
- Python 3.x
- Python Turtle graphics library (included in standard Python installation)
- `time` module (included in standard Python installation)

## Installation

1. Clone or download the code to your local machine
2. Save it as `car_lights.py` (or any preferred name with `.py` extension)
3. Ensure Python is installed on your system

## Usage

1. Open your terminal/command prompt
2. Navigate to the directory containing the script
3. Run the script using Python:
   ```bash
   python car_lights.py
   ```
4. Follow the prompts:
   - Type 'on' when asked to turn on the headlights
   - Type 'on' when asked to activate turning signals
   - Press Enter to exit the program

## Interactive Controls

The program currently supports these inputs:
1. Initial headlight control:
   - Type 'on' to turn on front headlights
   - Any other input keeps lights off
2. Turn signal control:
   - Type 'on' to activate all turn signals
   - Any other input keeps turn signals off

## Technical Details

### Light Components
- Front headlight dimensions: 100x50 pixels
- Rear light dimensions: 100x50 pixels
- Square shapes for light indicators
- Different size multipliers for main lights (2.3x3.3) and turn signals (2.3x1.5)

### Light Positions
- Front lights: y=200
- Rear lights: y=-200
- Left side: x=-300 to -200
- Right side: x=200 to 300

### Light States
- Grey: Light is off
- White: Front headlights on
- Yellow: Turn signals active
- Red: Rear lights on

### Timing
- Turn signal blink rate: 0.8 seconds on, 0.8 seconds off

## Planned Features (TODOs)
1. Arrow key controls for turning lights on/off
2. Spacebar control for brake lights
3. 'Off' option for turning off all lights

## Customization

You can modify these parameters in the code:
- Light colors (by modifying the `color()` values)
- Box dimensions (by adjusting the `fd()` values)
- Light sizes (using `shapesize()`)
- Blink timing (by modifying the `seconds` variables)

## Known Limitations

- Limited interactive controls
- No way to turn off lights once turned on
- Must restart program to change light states
- No keyboard controls (yet)

## Contributing

Feel free to fork this project and submit improvements via pull requests. Some areas for potential enhancement:
- Implementing the planned TODO features
- Adding more interactive controls
- Creating animated startup/shutdown sequences
- Adding more realistic light effects
- Implementing a GUI control panel

## License

This project is available for educational and personal use.

## Author's Note

This simulation is designed for educational purposes to demonstrate:
- Turtle graphics in Python
- User input handling
- Time-based animations
- State management
- Visual element positioning and sizing

## Troubleshooting

Common issues and solutions:
1. Black screen only:
   - Verify all coordinates are within screen bounds
   - Check if Python is properly installed
2. Lights not turning on:
   - Ensure correct input ('on' is case-sensitive)
   - Check if Turtle graphics is working properly
3. Program not responding:
   - Use Ctrl+C to exit if needed
   - Close the Turtle graphics window
