# Dynamic Traffic Signal Control for Buses Using SUMO and TraCI

## Overview

This project uses SUMO (Simulation of Urban MObility) and TraCI (Traffic Control Interface) to simulate and control traffic at intersections. The simulation includes vehicles of different types, with a specific focus on buses and their interactions with traffic signals. The goal is to manage bus stops and traffic light phases to improve traffic flow and bus scheduling.

## Files

### `busstop.py`

A Python script that interacts with the SUMO simulation using TraCI. Key functionalities include:

- **Simulation Logic:**
  - Monitors vehicles detected by induction loops.
  - Changes lanes or sets stops for buses based on detection.
  - Prints vehicle IDs and manages traffic signal phases.

### `busstop.net.xml`

Defines the road network for the simulation. Contains:

- **Edges and Lanes:** Specifications for road segments and lane properties.
- **Junctions:** Configuration of intersections and traffic light logic.
- **Connections:** Details on how different road segments are connected.

### `busstop.rou.xml`

Specifies vehicle routes and types for the simulation:

- **Vehicle Types:** Defines properties for different vehicle types, including appearance and behavior.
- **Flows:** Describes the flow of vehicles on different routes.
- **Routes:** Specifies routes for vehicles and their departure times.

### `busstop.sumocfg`

The SUMO configuration file that integrates the network, routes, and additional files:

- **Input Files:** References to the network, route, and additional files.

## How to Run

1. **Set Up Environment:**
   - Ensure the `SUMO_HOME` environment variable is set to your SUMO installation directory.

2. **Run the Simulation:**
   - To run with the GUI:
     ```bash
     python busstop.py
     ```
   - To run in non-GUI mode:
     ```bash
     python busstop.py --nogui
     ```

## Dependencies

- SUMO (Simulation of Urban MObility)
- Python libraries: `sumolib`, `traci`
  - To install dependencies:
    ```bash
    pip install sumolib traci
    ```

