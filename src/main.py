import inductiva

inductiva.api_key = "eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2R0NNIn0.whweYQGREbYqpISkxPjq6xNOLFS8_d7Yii_cD1nq8EGTV4c4tARcUg.ocyH784tTmiVYIR71fPXsw.WhkDOq7SnAVwjwo0NjaJxEGQgdszAB8DJMnJG_0s4QAC9sdXRP0hOHs-TLuf.xYxocbGcdHf6qKG548M17w"

def main():
    print('===========================================')
    print('Starting Inductiva Simulation')
    print('===========================================')

    # Url to a test object in Inductiva Github repository
    vehicle_url = "https://raw.githubusercontent.com/inductiva/inductiva/main" \
                "/assets/vehicle.obj"
    vehicle_path = inductiva.utils.files.download_from_url(vehicle_url)

    # Initialize the scenario
    scenario = inductiva.fluids.WindTunnel(flow_velocity=[30, 0, 0], domain={"x": [-5, 15], "y": [-5, 5], "z": [0, 8]})

    # Run a simulation
    task = scenario.simulate(object_path=vehicle_path, num_iterations=50, resolution="low")

    # Download the simulation output to your local machine.
    output = task.get_output()

    # Get the pressure field over the object
    pressure_field = output.get_object_pressure_field()

    # Render the post-processing
    pressure_field.render()

if __name__=='__main__':
    main()
