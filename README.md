# RDSS Remote Dressing Support System
This package is tested on ROS Melodic.

## To Run the package:
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

////////////////////////////////////////////////////////////
# To get the interaction environment:
-once the gazebo world is loaded
-click on the ball and place inthe world
-use s to scale and t to translate the spawned item

////////////////////////////////////////////////////////////
# To run the forward and inverse kinematics:
-open the src folder in the package and run the forward kinematics python file.
-for the inverse file integrate the file in the forward file so that the variables from the other file are easily imported.
-incase you want to run it as a different file make sure the contents of the first file are properly imported.
///////////////////////////////////////////////////////////
