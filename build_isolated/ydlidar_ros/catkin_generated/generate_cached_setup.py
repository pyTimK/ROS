# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/wcm-mob/catkin_ws/devel_isolated/navstack_pub;/home/wcm-mob/catkin_ws/devel_isolated/move_base;/home/wcm-mob/catkin_ws/devel_isolated/rotate_recovery;/home/wcm-mob/catkin_ws/devel_isolated/global_planner;/home/wcm-mob/catkin_ws/devel_isolated/navfn;/home/wcm-mob/catkin_ws/devel_isolated/move_slow_and_clear;/home/wcm-mob/catkin_ws/devel_isolated/dwa_local_planner;/home/wcm-mob/catkin_ws/devel_isolated/clear_costmap_recovery;/home/wcm-mob/catkin_ws/devel_isolated/carrot_planner;/home/wcm-mob/catkin_ws/devel_isolated/base_local_planner;/home/wcm-mob/catkin_ws/devel_isolated/nav_core;/home/wcm-mob/catkin_ws/devel_isolated/costmap_2d;/home/wcm-mob/catkin_ws/devel_isolated/voxel_grid;/home/wcm-mob/catkin_ws/devel_isolated/rplidar_ros;/home/wcm-mob/catkin_ws/devel_isolated/navigation;/home/wcm-mob/catkin_ws/devel_isolated/amcl;/home/wcm-mob/catkin_ws/devel_isolated/map_server;/home/wcm-mob/catkin_ws/devel_isolated/localization_data_pub;/home/wcm-mob/catkin_ws/devel_isolated/launch_jetson_nano_bot;/home/wcm-mob/catkin_ws/devel_isolated/imu_bno055;/home/wcm-mob/catkin_ws/devel_isolated/go_to_goal_turtlesim;/home/wcm-mob/catkin_ws/devel_isolated/fake_localization;/home/wcm-mob/catkin_ws/devel;/home/wcm-mob/ydlidar_ws/devel;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/wcm-mob/catkin_ws/devel_isolated/ydlidar_ros/env.sh')

output_filename = '/home/wcm-mob/catkin_ws/build_isolated/ydlidar_ros/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
