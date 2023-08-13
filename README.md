# RDSS Remote Assistance

This project involved designing and simulating a robotic system to assist humans. The goal was to develop an autonomous solution to support dressing tasks in healthcare and home settings.

## System Overview

The system consists of a 7-DOF Barrett WAM robotic arm with a 3-finger gripping end effector. The lightweight arm provides human-like dexterity for manipulating clothes and accessories.

Key capabilities:

- Reach across wide spherical workspace to access garments
- Form complex gripper poses to grasp variety of clothing items 
- Follow dressing trajectories while avoiding collisions
- Integrate with sensors for closed-loop control

## Implementation 

- Constructed manipulator CAD model with accurate joint axes and DH parameters
- Derived analytical inverse and forward kinematics for position control
- Simulated dynamic model in ROS/Gazebo and tuned PID controllers
- Implemented keyboard teleoperation to demonstrate picking and manipulation

## Results

- Kinematics analyses matched with simulated model joint poses
- Stable gripper grasping and manipulation of a spherical object  
- Intuitive joint-level control through keyboard teleoperation
- Demonstrated feasibility of using robot for dressing assistance

## Future Work

- Add computer vision for garment detection and trajectory planning
- Implement advanced controllers for smoother motion
- Validate on physical robot prototype with real garments
- Test with human subjects and integrate safety mechanisms
- Explore bi-manual robots for faster dressing of multiple items

## Running RDSS Simulation:
- Extrac the package to workspace/src and build
- source the workspace

- Launching the model
```
roslaunch RDSS template_launch.launch
```

### To run the teleop file:
- Open a new terminal
- Navigate to your workspce
- Source the workspace
- Operating RDSS
```
rosrun RDSS template_teleop.py
```

## For rviz Visualization
- Open new terminal
- Source the workspace
```
rviz	
```

# To get the interaction environment:
- Once the gazebo world is loaded
- Click on the ball and place inthe world
- Use 's' to scale and 't' to translate the spawned item

# To run the forward and inverse kinematics:
- Open the src folder in the package and run the forward kinematics python file.
- For the inverse file integrate the file in the forward file so that the variables from the other file are easily imported.
- Incase you want to run it as a different file make sure the contents of the first file are properly imported.

