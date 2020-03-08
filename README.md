ABC Dataset ROS
===============
## Description
ROS package to use ABC dataset (A Big CAD Model Dataset)<cite>[hoge][1]</cite> in ROS.

![abc_gazebo](https://github.com/takayuki5168/abc_dataset_ros/blob/master/images/abc_gazebo.png)

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
### Preliminaries
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/takayuki5168/abc_dataset_ros
$ cd abc_dataset_ros
$ catkin bt
$ ./scripts/download_step.sh         # Download CAD dataset whose format is STEP
$ ./scripts/convert_step_to_stl.py   # Convert STEP files to STL files
```

### Render in Rviz
```bash
$ ./scripts/generate_udf.sh   # Generate UDF files with STL files
$ roslaunch abc_dataset_ros rviz_demo.launch
```

### Render in Gazebo
```bash
$ ./scripts/generate_sdf.sh   # Generate SDF files with STL files
$ roslaunch abc_dataset_ros gazebo_demo.launch
#$ roslaunch gazebo_ros empty_world.launch world_name:=test.world
```

[1] S. Koch, A. Matveev, Z. Jiang, F. Williams, A. Alexey, E. Burnaev, M. Alexa, D. Zorin, and Panozzo, Daniele. ABC: A Big CAD Model Dataset For Geometric Deep Learning. CVPR2019
