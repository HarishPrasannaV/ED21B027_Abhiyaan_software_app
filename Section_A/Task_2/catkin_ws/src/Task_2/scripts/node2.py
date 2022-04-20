#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
# defining the callback function
def msg_callback(msg):
    rospy.loginfo(msg)
if __name__ == '__main__':
    # node initialization
    rospy.init_node("node2")
    # subscribing to the topic
    sub=rospy.Subscriber("/team_abhiyaan",String,callback=msg_callback)
    rospy.loginfo("Node 2 is now running")
    #executing the loop until shutdown
    rospy.spin()
