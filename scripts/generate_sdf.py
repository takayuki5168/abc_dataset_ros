#!/usr/bin/env python

import sys, os

path = os.path.dirname(os.path.abspath(__file__)) + '/../models/step_test/'
dirs = os.listdir(path)

for i in range(len(dirs)):
    dir_path = path + dirs[i]

    model_name = dirs[i]
    print(model_name)

    # model.config
    config_str = "<?xml version=\"1.0\" ?>\n\
<model>\n\
  <name>" + model_name + "</name>\n\
  <version>1.0</version>\n\
  <sdf version=\"1.6\">model.sdf</sdf>\n\
  <author>\n\
    <name></name>\n\
    <email></email>\n\
  </author>\n\
  <description></description>\n\
</model>"

    config_file_name = dir_path + '/model.config'
    with open(config_file_name, mode='w') as f:
        f.write(config_str)

    # model.sdf
    sdf_str = "<?xml version='1.0'?>\n\
<sdf version=\"1.4\">\n\
  <model name=\"" + model_name + "\">\n\
    <pose>0 0 0.5 0 0 0</pose>\n\
    <link name=\"link\">\n\
      <inertial>\n\
        <mass>1.0</mass>\n\
        <inertia>\n\
          <ixx>0.083</ixx>\n\
          <ixy>0.0</ixy>\n\
          <ixz>0.0</ixz>\n\
          <iyy>0.083</iyy>\n\
          <iyz>0.0</iyz>\n\
          <izz>0.083</izz>\n\
        </inertia>\n\
      </inertial>\n\
      <collision name=\"collision\">\n\
        <geometry>\n\
          <mesh>\n\
            <uri>model://step_test/" + model_name + "/model.stl</uri>\n\
            <scale>0.001 0.001 0.001</scale>\n\
          </mesh>\n\
        </geometry>\n\
      </collision>\n\
      <visual name=\"" + model_name + "\">\n\
        <geometry>\n\
          <mesh>\n\
            <uri>model://step_test/" + model_name + "/model.stl</uri>\n\
            <scale>0.001 0.001 0.001</scale>\n\
          </mesh>\n\
        </geometry>\n\
        <material>\n\
          <script>\n\
            <uri>model:///materials/metal1.material</uri>\n\
            <name>Metal1</name>\n\
          </script>\n\
        </material>\n\
      </visual>\n\
    </link>\n\
  </model>\n\
</sdf>"

    config_file_name = dir_path + '/model.sdf'
    with open(config_file_name, mode='w') as f:
        f.write(sdf_str)
