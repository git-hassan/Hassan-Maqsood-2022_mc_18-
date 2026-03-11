Lab Report - Week 2

MCT-454L Mobile Robotics
Instructor: Dr. Maria Akram
Student: Hassan Maqsood
Registration No: 2022-MC-18


1. Objective

The objective of this lab was to get familiar with ROS 2 command-line tools, understand how turtlesim works, and learn how to control a simulated robot using topics and services. We also explored rqt to call services through a graphical interface.


2. Steps Followed

Step 1: Launching Turtlesim

I launched the turtlesim node using the command ros2 run turtlesim turtlesim_node. A window appeared showing a turtle on a blue background. This node acts as a simple robot simulator where the turtle represents a robot that can be moved and controlled.

Step 2: Controlling the Turtle with Keyboard

I opened a new terminal and ran ros2 run turtlesim turtle_teleop_key. This launched the teleop node which let me control the turtle using arrow keys. Pressing the keys published velocity commands on the /turtle1/cmd_vel topic and the turtle moved accordingly.

Step 3: Exploring Topics

I used ros2 topic list to see all active topics. Then I ran ros2 topic echo /turtle1/pose to observe the turtle's position in real time. As I moved the turtle, the x, y, and theta values kept updating in the terminal showing the current position and angle.

Step 4: Sending Velocity Commands

I used ros2 topic pub to send velocity commands directly to the turtle without using the keyboard. I set linear x to 2.0 and angular z to 1.8 which made the turtle move in a circle automatically. This showed how topics can be used to control a robot from the terminal.

Step 5: Resetting the Simulation

I called the /reset service using ros2 service call /reset std_srvs/srv/Empty. The turtle immediately returned to its starting position and all the lines it drew were cleared. This was my first time using a service call and I could clearly see the difference between topics (continuous) and services (one-time action).

Step 6: Using rqt

I opened rqt and explored the node graph which showed the /turtlesim and /teleop_turtle nodes connected through topics like /turtle1/cmd_vel and /turtle1/pose. I also used the Service Caller plugin in rqt to call services through a graphical interface instead of the terminal.

Step 7: Calling /reset from rqt

I selected the /reset service in rqt Service Caller and clicked Call. The response showed std_srvs/srv/Empty.Response and the turtle reset to its starting position. This confirmed the service was called successfully.

Step 8: Spawning a Second Turtle

I selected the /spawn service in rqt and filled in x as 2.0, y as 2.0, theta as 0.0, and name as turtle2. After clicking Call the response showed the name turtle2 and a second turtle appeared in the turtlesim window. This showed how services can be used to modify the simulation state.

Step 9: Controlling the Second Turtle

I sent velocity commands to turtle2 using ros2 topic pub /turtle2/cmd_vel with the same linear and angular values. The second turtle started moving in a circle independently from the first turtle. This showed that each turtle has its own separate topic for control.

Step 10: Teleporting the Turtle

I used the /turtle1/teleport_absolute service in rqt with x as 10.0, y as 10.0, and theta as 0.0. The turtle instantly jumped to that position in the simulation window. This is a good example of a service because it is a one-time action and not a continuous stream of data.

Step 11: Changing Background Color

I changed the background color by setting the parameters background_r to 255, background_g to 0, and background_b to 0 using ros2 param set commands. Then I called the /clear service from rqt to apply the change. The background turned red which confirmed the parameters were updated successfully.


3. Observations

Topics are used for continuous data like velocity commands and position updates.
Services are used for one-time actions like resetting, spawning, and teleporting.
Each turtle has its own set of topics so they can be controlled independently.
rqt provides a graphical way to interact with nodes, topics, and services without using the terminal.
The node graph in rqt clearly shows how nodes communicate with each other through topics.


4. Conclusion

This lab gave me a clear understanding of how ROS 2 topics and services work in practice. Topics are used when data needs to flow continuously between nodes while services handle one-time requests and responses. The turtlesim simulator made it easy to see the results of each command in real time. Using rqt also helped me understand the overall structure of a ROS 2 system visually.
