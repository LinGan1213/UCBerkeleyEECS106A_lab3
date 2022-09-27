#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
import example_forward_kinematics as aa

# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(JointState):

    # Print the contents of the message to the console
    #Tts.timestamp = rospy.get_time()
    #print(Tts.message)
    #aa.baxter_forward_kinematics_from_joint_state(JointState)
    #print(aa.baxter_forward_kinematics_from_joint_state(JointState))
    print(JointState.position)

# Define the method which contains the node's main functionality
def listener():

    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    rospy.Subscriber("robot/joint_states", JointState, callback)
    #print(JointState.position)

    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C
    rospy.spin()

# Python's syntax for a main() method
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.
    rospy.init_node('listener', anonymous=True)

    listener()
