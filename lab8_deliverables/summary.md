# Lab 8 Customization Summary: The Snowbot

For this lab, the standard differential-drive robot was highly customized into a "Snowbot" model using URDF geometry primitives. 

**Structural Enhancements:**
* **Chassis:** Designed a thin flat white base plate as the foundational footprint.
* **Body Structure:** Constructed the main chassis using three stacked spheres (bottom, mid, and head) to replicate a snowman structure.
* **Aesthetics:** Engineered detailed facial features using small cylinders (nose) and spheres (eyes, smile). A custom top hat was built using stacked cylinders to form the brim, red band, and top.
* **Sensors:** Mounted a red LiDAR cylinder at the absolute peak of the robot (`z="0.823"`) to ensure an unobstructed line of sight for future Gazebo mapping sessions.

**Kinematics & Mobility:**
* **Drive System:** Implemented a differential drive setup with left and right cylindrical wheels using continuous joints for full rotation. Added decorative red hubs to the wheels.
* **Stability:** Integrated both front and rear spherical casters beneath the base plate to balance the extended vertical height of the model. 
