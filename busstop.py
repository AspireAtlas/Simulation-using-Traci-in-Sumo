import os
import sys
import optparse

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="Run the command-line version of SUMO")
    options, args = opt_parser.parse_args()
    return options

def run():
    Step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(Step)
        det_vehs = traci.inductionloop.getLastStepVehicleIDs("det_0")
        det_vehs0 = traci.inductionloop.getLastStepVehicleIDs("det_01")
        det_vehs1 = traci.inductionloop.getLastStepVehicleIDs("det_1")
        det_vehs2 = traci.inductionloop.getLastStepVehicleIDs("det_2")
        
        for veh in det_vehs0:
        	if traci.vehicle.getTypeID(veh) == "bus":
        		traci.vehicle.changeLane(veh,0,25)
        
        for veh in det_vehs:
            print(veh)

            if traci.vehicle.getTypeID(veh) == "bus":
                edge_id = "E2"  
                print(f"Stopping bus {veh} at edge {edge_id}...")
                traci.vehicle.setStop(veh, edgeID=edge_id, pos=56.15, duration=15)
                
        for veh in det_vehs1:
            print(veh)
            traci.vehicle.changeLane(veh, 2, 20)

        for veh in det_vehs2:
            print(veh)
            traci.vehicle.changeLane(veh, 2, 25)

        Step += 1
    traci.close()
    sys.stdout.flush()

if __name__ == "__main__":
    options = get_options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "busstop.sumocfg", "--tripinfo-output", "tripinfo.xml"])
    run()

