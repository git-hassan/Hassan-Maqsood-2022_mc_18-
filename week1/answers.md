Week 1 Post-Lab Answers

Name: Hassan Maqsood
Registration Number: 2022-MC-18
Course: MCT-454L Mobile Robotics
Instructor: Dr. Maria Akram


Q1. Define: node, topic, package, workspace

Node: A node is just a program that runs and does one job in ROS 2, like printing a message or reading a sensor.

Topic: A topic is like a channel that nodes use to send and receive messages between each other.

Package: A package is simply a folder that contains our ROS 2 code and some extra files that tell ROS 2 how to build and run it.

Workspace: A workspace is the main folder where we keep all our packages and where we run colcon build to compile everything.


Q2. Why is sourcing required? What happens if you do not source?

Sourcing is required because ROS 2 needs to know where our packages are installed. When we run source install/setup.bash, it tells the terminal where to find everything. If we skip it, the terminal has no idea ROS 2 even exists and just shows errors like command not found or package not found. I actually faced this problem myself when my .bashrc had the wrong path and every new terminal was giving errors.


Q3. What is the purpose of colcon build? What folders does it generate?

colcon build compiles our package and makes it ready to run. Before building, ROS 2 cannot run our code at all. After we run it, three new folders appear in our workspace.

build folder has temporary files created during building.
install folder has the actual files ROS 2 uses to run our package.
log folder has logs that help us see what went wrong if the build fails.


Q4. What does the entry_points console script do in setup.py?

It tells ROS 2 the name of our node and which function to run when we call ros2 run. For example when we write simple_node = my_first_pkg.simple_node:main, it means whenever we type ros2 run my_first_pkg simple_node, go to the file simple_node.py and run the main function. Without this line ROS 2 just says No executable found which I also got during this lab.


Q5. Publisher Subscriber Diagram

+----------------------+                   +----------------------+
|       Node A         |                   |       Node B         |
|    (Publisher)       |                   |    (Subscriber)      |
|                      |                   |                      |
|  sends messages      |   /chatter topic  |  receives messages   |
|  on a topic          +-----------------> |  and reads them      |
+----------------------+                   +----------------------+

Node A keeps sending messages on the /chatter topic.
Node B is listening on the same topic and reads every message that arrives.
They don't talk to each other directly, the topic connects them automatically.
