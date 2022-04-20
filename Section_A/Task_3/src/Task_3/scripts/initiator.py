#!/usr/bin/env python3
import rospy
rospy.init_node("initiator")
from turtlesim.srv import Kill
from turtlesim.srv import Spawn
# wating for the services to come active
rospy.wait_for_service("/kill")
rospy.wait_for_service("/spawn")
def kill_turtle_service(name):
    #to call service
    kill_turtle=rospy.ServiceProxy("/kill", Kill)
    response= kill_turtle(name)
def spawn_turtle_service(x,y,theta,name):
    spawn_turtle=rospy.ServiceProxy("/spawn", Spawn)
    response= spawn_turtle(x,y,theta,name)
# killing turtle :(
kill_turtle_service('turtle1')   
#spawning turtles
spawn_turtle_service(5.5,9,3.14159,'turtle1')
spawn_turtle_service(5.5,3,0,'turtle2')
