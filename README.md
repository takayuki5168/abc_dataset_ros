ABC Dataset ROS
===============

## Description
ROS package to use ABC dataset<cite>[hoge][1]</cite> in ROS.

## Demonstrations

## Requirement
- FreeCAD
```
$ sudo apt-get install freecad
```
- 7z
```
$ sudo apt-get install p7zip-full
```

## Usage
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/takayuki5168/abc_dataset_ros
$ cd abc_dataset_ros
$ catkin bt
$ ./scripts/download_step.sh                                       # Download CAD dataset whose format is STEP
$ ./scripts/convert_step_to_stl.py                                 # Convert STEP files to STL files
$ ./scripts/generate_sdf.sh                                        # Generate SDF files with STL files
$ roslaunch gazebo_ros empty_world.launch world_name:=test.world   # Render SDF files in Gazebo
```

[1] S. Koch, A. Matveev, Z. Jiang, F. Williams, A. Alexey, E. Burnaev, M. Alexa, D. Zorin, and Panozzo, Daniele. ABC: A Big CAD Model Dataset For Geometric Deep Learning. CVPR2019
