# Inductiva-Testing

- Repo for testing of Inductiva sofwtare 
- Code base: https://github.com/inductiva/inductiva

## Modifications
*Testing environment: Ubuntu 20.04 WSL in Windows 11*

1. Error iterating PosixPath object

- Path: 'inductiva\utils\templates.py'

- Error: 
<span style="color: red"> 
Traceback (most recent call last):
  File "main.py", line 31, in <module>
    main()
  File "main.py", line 19, in main
    task = scenario.simulate(object_path=vehicle_path, num_iterations=50, resolution="low")
  File "/mnt/c/Users/dyxcv/Documents/Inductiva/src/inductiva/fluids/wind_tunnel/wind_tunnel.py", line 128, in simulate
    task = super().simulate(simulator,
  File "/mnt/c/Users/dyxcv/Documents/Inductiva/src/inductiva/scenarios.py", line 119, in simulate
    self.create_input_files(simulator, input_dir)
  File "/mnt/c/Users/dyxcv/Documents/Inductiva/src/inductiva/scenarios.py", line 60, in create_input_files
    utils.templates.batch_replace_params(
  File "/mnt/c/Users/dyxcv/Documents/Inductiva/src/inductiva/utils/templates.py", line 83, in batch_replace_params
    replace_params(
  File "/mnt/c/Users/dyxcv/Documents/Inductiva/src/inductiva/utils/templates.py", line 48, in replace_params
    environment = Environment(loader=FileSystemLoader((template_dir)))
  File "/usr/lib/python3/dist-packages/jinja2/loaders.py", line 163, in __init__
    self.searchpath = list(searchpath)
TypeError: 'PosixPath' object is not iterable
</span>

- Modifications:

    ```
    environment = Environment(loader=FileSystemLoader(template_dir))
    ```
    
    To

    ```
    environment = Environment(loader=FileSystemLoader(str(template_dir)))
    ```
    