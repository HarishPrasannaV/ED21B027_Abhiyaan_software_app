#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
if __name__== '__main__':
    # node initialization
    rospy.init_node("node1") 
    rospy.loginfo("Node 1 is now running")
    #publisher initialization
    pub=rospy.Publisher("/team_abhiyaan",String) 
     # defining the rate at which the loop should be executed
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        message=str("Team Abhiyaan rocks")
        rospy.loginfo("Data is being sent to the publisher")
        #publishing the data to topic
        pub.publish(str(message))
        # pausing for every 0.1 seconds
        rate.sleep() 

