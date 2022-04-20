#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
#decleration of global variables
x1=5.5
x2=5.5
y1=9
y2=3
def pose_callback_1(pose :Pose):
    global x1
    global y1
    x1=pose.x
    y1=pose.y
def pose_callback_2(pose: Pose):
    global x2
    global y2
    x2=pose.x
    y2=pose.y
if __name__ =='__main__':
    rospy.init_node("controller")
    # initiation of publishers to control turtles
    pub1=rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size=10)
    pub2=rospy.Publisher("/turtle2/cmd_vel", Twist,queue_size=10)
    rate=rospy.Rate(10)
    # initiation of subscribers to find position of turtles
    sub1=rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback_1)
    sub2=rospy.Subscriber("/turtle2/pose", Pose, callback=pose_callback_2)
    # initial conditions
    m1=3
    m2=3
    v_init_1=-1.25
    v_init_2=1.25
    g=15
    # calculating center of mass
    com_x=((5.5*m1)+(5.5*m2))/(m1+m2)
    com_y=((9*m1)+(3*m2))/(m1+m2)
    r_init_1=((5.5-com_x)**2 + (9-com_y)**2)**0.5
    r_init_2=((5.5-com_x)**2 + (3-com_y)**2)**0.5
    ct1=Twist()
    ct2=Twist()
    u=g*((m1*m2)/(m1+m2))
    #calculation of length of semi major axis
    a1=(u*r_init_1)/(2*u-(r_init_1*v_init_1*v_init_1))
    a2=(u*r_init_2)/(2*u-(r_init_2*v_init_2*v_init_2))
    while not rospy.is_shutdown():
        r1=((x1-com_x)**2 + (y1-com_y)**2)**0.5
        r2=((x2-com_x)**2 + (y2-com_y)**2)**0.5
        d=(((x2-x1)**2 + (y2-y1)**2))**0.5
        # formula to find tangential velocity and angular velocity(taken from wikipedia,idk physics )
        v1=((u)*((2/r_init_1)-(1/a1)))**5
        w1=v1/r1
        v2=((u)*((2/r_init_2)-(1/a2)))**5
        w2=v2/r2
        ct1.linear.x=v1.real
        ct1.angular.z=w1.real
        ct2.linear.x=v2.real
        ct2.angular.z=w2.real
        # publishing the velocities to respective turtles
        pub1.publish(ct1)
        pub2.publish(ct2)
        rate.sleep()
