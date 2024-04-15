# Installation

Install the required packages with:
```sh
pip install -r requirements.txt
```

To install this as package make a local copy, activate your environment and run pip install:
```
>> git clone https://github.com/Zimmer-lab/imutils
>> conda activate my_env
>> pip install /path/to/folder/with/setup/dot/py
```
you can check
https://github.com/Zimmer-lab/protocols/blob/master/computational/zimmer_lab_code_pipeline/04-installing_personal_python_packages.md
for details.

# Description
## General:
This package has some image processing tools written by Ulises.
## LoguruConfigurator:
A simple to use logging library.
See documentation (docs)
## Read Microscopy (Micromanager) dataset:
#### Open Dataset:
```
>> from MicroscopeDataReader.MicroscopeDataReader import MicroscopeDataReader
>> my_dataet = MicroscopeDataReader(dataset_path)
```
#### Get Data as lazy loaded dask array:
```
>> dask_array = my_dataset.dask_array
>> my_dataset.get_axis_order() > ['position', 'time', 'channel', 'z', 'y', 'x']
>> my_dataset.get_axis_string() > PTCZYX
```
#### Get single image as nparry (loaded into memory)
```
# image = my_dataset.read_image(position = position, time = time, channel=channel, z=z)
# (or get_frame)
>> image = my_dataset.get_frame(time = 42) # not given arguments are 0
```
#### View dataset with napari
```
# napari is not in the requirement file! Please install separately.
>> my_dataset.open_in_napari()
```
### Additional Documentation
Additional Documentation as jupyter lab book in docs!