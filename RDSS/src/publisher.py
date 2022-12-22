#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub_j1 = rospy.Publisher('wam16/j1_control/command', Float64, queue_size=10)  # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_j2 = rospy.Publisher('wam16/j2_control/command', Float64, queue_size=10)
    pub_j3 = rospy.Publisher('wam16/j3_control/command', Float64, queue_size=10)
    pub_j4 = rospy.Publisher('wam16/j4_control/command', Float64, queue_size=10)
    pub_j6 = rospy.Publisher('wam16/j6_control/command', Float64, queue_size=10)
    pub_j7 = rospy.Publisher('wam16/j7_control/command', Float64, queue_size=10)
    pub_j8 = rospy.Publisher('wam16/j8_control/command', Float64, queue_size=10)
    pub_hj = rospy.Publisher('wam16/hj_control/command', Float64, queue_size=10)
    pub_hj11 = rospy.Publisher('wam16/hj11_control/command', Float64, queue_size=10)
    pub_hj12 = rospy.Publisher('wam16/hj12_control/command', Float64, queue_size=10)
    pub_hj21 = rospy.Publisher('wam16/hj21_control/command', Float64, queue_size=10)
    pub_hj22 = rospy.Publisher('wam16/hj22_control/command', Float64, queue_size=10)
    pub_hj23 = rospy.Publisher('wam16/hj23_control/command', Float64, queue_size=10)
    pub_hj31 = rospy.Publisher('wam16/hj31_control/command', Float64, queue_size=10)
    pub_hj32 = rospy.Publisher('wam16/hj32_control/command', Float64, queue_size=10)
    pub_hj33 = rospy.Publisher('wam16/hj33_control/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_j1.publish(2.0)
        pub_j2.publish(2.0)
        pub_j3.publish(2.0)
        pub_j4.publish(2.0)
        pub_j6.publish(2.0)
        pub_j7.publish(2.0)
        pub_j8.publish(2.0)
        pub_hj.publish(2.0)
        pub_hj11.publish(2.0)
        pub_hj12.publish(2.0)
        pub_hj21.publish(2.0)
        pub_hj22.publish(2.0)
        pub_hj23.publish(2.0)
        pub_hj31.publish(2.0)
        pub_hj32.publish(2.0)
        pub_hj32.publish(2.0)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass