#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your RDSS!
---------------------------
Manipulator keys:
   Joint 1: 1,q
   Joint 2: 2,w
   Joint 3: 3,e
   Joint 4: 4,r
   Joint 6: 6,y
   Joint 7: 7,8
   Joint 8: 8,i
   a,z : palm joint rotation
   s,x : open and close hand
   d,c : claw fingers horizontal movement
   f,v : thumb movement
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8
turn = 0.5

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

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


    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    try:
        print(msg)
        while(1):
            key = getKey()
            if key == '1':
                pub_j1.publish(2.0)
                print("j1 = 2.0")
            elif key == 'q':
                pub_j1.publish(-2.0)
                print("j1 = -2.0")
            elif key == '2':
                pub_j2.publish(2.0)
                print("j2 = 2.0")
            elif key == 'w':
                pub_j2.publish(-2.0)
                print("j2 = -2.0")
            elif key == '3':
                pub_j3.publish(2.0)
                print("j3 = 2.0")
            elif key == 'e':
                pub_j3.publish(-2.0)
                print("j3 = -2.0")
            elif key == '4':
                pub_j4.publish(2.0)
                print("j4 = 2.0")
            elif key == 'r':
                pub_j4.publish(-2.0)
                print("j4 = -2.0")
            elif key == '6':
                pub_j6.publish(2.0)
                print("j5 = 2.0")
            elif key == 'y':
                pub_j6.publish(-2.0)
                print("j6 = -2.0")
            elif key == '7':
                pub_j7.publish(2.0)
                print("j7 = 2.0")
            elif key == 'u':
                pub_j7.publish(-2.0)
                print("j7 = -2.0")
            elif key == '8':
                pub_j8.publish(2.0)
                print("j8 = 2.0")
            elif key == 'i':
                pub_j8.publish(-2.0)
                print("j8 = -2.0")
            elif key == 'a':
                pub_hj.publish(2.0)
                print("hand joint rotation = 2.0")
            elif key == 'z':
                pub_hj.publish(-2.0)
                print("hand joint rotation = 2.0")
            elif key == 's':
                pub_hj11.publish(0.2)
                pub_hj12.publish(-0.25)
                pub_hj22.publish(0.2)
                pub_hj23.publish(-0.25)
                pub_hj32.publish(0.2)
                pub_hj33.publish(-0.25)
                print("hand closing")
            elif key == 'd':
                pub_hj21.publish(1.0)
                pub_hj31.publish(-1.0)
                print("finger distance increase")
            elif key == 'c':
                pub_hj21.publish(-1.0)
                pub_hj31.publish(1.0)
                print("finger distance decrease")
            elif key == 'x':
                pub_hj11.publish(-0.2)
                pub_hj12.publish(0.25)
                pub_hj22.publish(-0.2)
                pub_hj23.publish(0.25)
                pub_hj32.publish(-0.2)
                pub_hj33.publish(0.25)
                print("hand opening")
            elif key == 'f':
                pub_hj11.publish(0.2)
                print("thumb up")
            elif key == 'v':
                pub_hj11.publish(-0.2)
                print("thumb down")
            elif key == 'g':
                pub_hj12.publish(0.2)
                print("finger up")
            elif key == 'b':
                pub_hj12.publish(-0.2)
                print("finger down")
            elif key == 'j':
                pub_hj21.publish(0.2)
                print("finger up")
            elif key == 'm':
                pub_hj21.publish(-0.2)
                print("finger down")
            elif key == 'k':
                pub_hj22.publish(0.2)
                print("finger up")
            elif key == ',':
                pub_hj22.publish(-0.2)
                print("finger down")
            elif key == 'l':
                pub_hj23.publish(0.2)
                print("finger up")
            elif key == '.':
                pub_hj23.publish(-0.2)
                print("finger down")
            elif key == '9':
                pub_hj31.publish(0.2)
                print("finger up")
            elif key == 'o':
                pub_hj31.publish(-0.2)
                print("finger down")
            elif key == '-':
                pub_hj32.publish(0.2)
                print("finger up")
            elif key == '[':
                pub_hj32.publish(-0.2)
                print("finger down")
            elif key == '=':
                pub_hj21.publish(0.2)
                print("finger up")
            elif key == ']':
                pub_hj21.publish(-0.2)
                print("finger down")
            else:
                pub_j1.publish(0.0)
                pub_j2.publish(0.0)
                pub_j3.publish(0.0)
                pub_j4.publish(0.0)
                pub_j6.publish(0.0)
                pub_j7.publish(0.0)
                pub_j8.publish(0.0)
                pub_hj11.publish(0.0)
                pub_hj12.publish(0.0)
                pub_hj21.publish(0.0)
                pub_hj22.publish(0.0)
                pub_hj23.publish(0.0)
                pub_hj31.publish(0.0)
                pub_hj32.publish(0.0)
                pub_hj33.publish(0.0)

            
            # if key in moveBindings.keys():
            #     x = moveBindings[key][0]
            #     th = moveBindings[key][1]
            #     count = 0
            # elif key in speedBindings.keys():
            #     speed = speed * speedBindings[key][0]
            #     turn = turn * speedBindings[key][1]
            #     count = 0

            #     print vels(speed,turn)
            #     if (status == 14):
            #         print msg
            #     status = (status + 1) % 15
            # elif key == ' ' or key == 'k' :
            #     x = 0
            #     th = 0
            #     control_speed = 0
            #     control_turn = 0
            # else:
            #     count = count + 1
            #     if count > 4:
            #         x = 0
            #         th = 0
            #     if (key == '\x03'):
            #         break

            # target_speed = speed * x
            # target_turn = turn * th

            # if target_speed > control_speed:
            #     control_speed = min( target_speed, control_speed + 0.02 )
            # elif target_speed < control_speed:
            #     control_speed = max( target_speed, control_speed - 0.02 )
            # else:
            #     control_speed = target_speed

            # if target_turn > control_turn:
            #     control_turn = min( target_turn, control_turn + 0.1 )
            # elif target_turn < control_turn:
            #     control_turn = max( target_turn, control_turn - 0.1 )
            # else:
            #     control_turn = target_turn

            # pub_right.publish(control_turn) # publish the turn command.
            # pub_left.publish(control_turn) # publish the turn command.
            # pub_move.publish(control_speed) # publish the control speed. 


    except:
        print(e)

    finally:
        pub_right.publish(control_turn)
        pub_left.publish(control_turn)
        pub_move.publish(control_speed)
        # twist = Twist()
        # twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        # twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)