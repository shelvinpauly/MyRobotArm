///////////////////////////////////////////////////////////
To Run the package:
-copy the package to the catkin_ws/src and make
-source
-enter the command:
	roslaunch wam16 template_launch.launch
To run the teleop file:
-open new terminal
-navigate to catkin_ws
-source
-enter the command:
	rosrun wam16 template_teleop.py
For rviz
-open new terminal
-source
	rviz	
////////////////////////////////////////////////////////////
To get the interaction environment:
-once the gazebo world is loaded
-click on the ball and place inthe world
-use s to scale and t to translate the spawned item
////////////////////////////////////////////////////////////
To run the forward and inverse kinematics:
-open the src folder in the package and run the forward kinematics python file.
-for the inverse file integrate the file in the forward file so that the variables from the other file are easily imported.
-incase you want to run it as a different file make sure the contents of the first file are properly imported.
///////////////////////////////////////////////////////////

