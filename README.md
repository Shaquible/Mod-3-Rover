# Mod-3-Rover
### Description
This is an implementation of the D* Lite algorithm for autonomous rover path planning. The rover is able to traverse simulated environments in Gazebo, using a 16-segment LiDAR array for obstacle detection. The complete algorithm allows quick pathfinding and obstacle avoidance until the rover reaches its goal position.
### How to use
1. Clone the repository
2. Launch Gazebo and create a virtual environment
3. Run main.py
4. When prompted, enter a target x position that is within half of the grid width. Then enter a target y position that is within half of the grid height. These values can be either negative or positive.

In order to customize the grid size, change the grid_width and grid_height variables to equal any odd numbered positive integer. The resolution of the grid can also be changed by varying the grid_res variable to any positive real number. 
