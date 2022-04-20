#!/usr/bin/env python3
from ast import Str
import rospy
from std_msgs.msg import String
#global variable to store data from callback function
data=None
newSentence=None
# defining the callback function
def msg_callback(msg):
    # using the global variables inside callback
    global newSentence
    global data
    # storing data recived from topic after converting it into string
    data=str(msg.data)
    #reversing the sring word by word
    words = data.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
if __name__== '__main__':
    # node initialization
    rospy.init_node("node3")
    rospy.loginfo("Node 3 is now running")
    # publisher initialization
    pub=rospy.Publisher("/naayihba_maet",String)
    # defining the date at which the loop should be executed
    rate=rospy.Rate(10)
    #subscribing to topic
    sub=rospy.Subscriber("/team_abhiyaan",String,callback=msg_callback)
    while not rospy.is_shutdown():
        message=newSentence
        rospy.loginfo("Data is being sent to the publisher")
        # publishing data to topic
        pub.publish(message)
        # pausing for 0.1 sec per one loop eecution
        rate.sleep()

