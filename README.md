# Mod-3-Rover
### Description
This is an implementation of the D* Lite algorithm for autonomous rover navigation. The rover is able to traverse simulated environments in Gazebo, using a 16-segment LiDAR array for obstacle detection. The completed algorithm is used for quick pathfinding and obstacle avoidance until a target position is reached by the rover.
### How to use
1. Launch Gazebo and create a virtual environment
2. Run main.py
3. When prompted, enter a target x-coordinate that is within half of the grid width. Then enter a target y-coordinate that is within half of the grid height. These values can be either negative or positive.

In order to customize the grid size, change the grid_width and grid_height variables to equal any odd numbered positive integer. The resolution of the grid can also be changed by varying the grid_res variable to any positive real number. 
