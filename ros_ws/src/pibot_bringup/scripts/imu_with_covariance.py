#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

#from tf.transformations import quaternion_from_euler

class IMUWithCovariance():
    def __init__(self):
        # Give the node a name
        rospy.init_node('imu_with_covariance', anonymous=False)

        # Publisher of type Imu
        self.imu_pub = rospy.Publisher('output', Imu, queue_size=1000)
        
        # Wait for the /imu topic to become available
        rospy.wait_for_message('input', Imu)
        
        # Subscribe to the /imu topic
        rospy.Subscriber('input', Imu, self.pub_imu)
        
        rospy.loginfo("Publishing Imu with covariance on /imu_with_covariance")
        self.imu_data = Imu()            # Filtered data
        self.imu_data.orientation_covariance = [1e6, 0, 0, 0, 1e6, 0, 0, 0, 1e-6]
        self.imu_data.angular_velocity_covariance = [1e6, 0, 0, 0, 1e6, 0, 0, 0, 1e-6]
        self.imu_data.linear_acceleration_covariance = [-1,0,0,0,0,0,0,0,0]
        
    def pub_imu(self, msg):
        self.imu_data.header.stamp = rospy.Time.now()
        self.imu_data.header.frame_id = msg.header.frame_id
        self.imu_data.header.seq = msg.header.seq
        self.imu_data.orientation.w = msg.orientation.w
        self.imu_data.orientation.x = msg.orientation.x
        self.imu_data.orientation.y = msg.orientation.y
        self.imu_data.orientation.z = msg.orientation.z
        self.imu_data.linear_acceleration.x = msg.linear_acceleration.x
        self.imu_data.linear_acceleration.y = msg.linear_acceleration.y
        self.imu_data.linear_acceleration.z = msg.linear_acceleration.z
        self.imu_data.angular_velocity.x = msg.angular_velocity.x
        self.imu_data.angular_velocity.y = msg.angular_velocity.y
        self.imu_data.angular_velocity.z = msg.angular_velocity.z
        self.imu_pub.publish(self.imu_data)
        
if __name__ == '__main__':
    try:
        IMUWithCovariance()
        rospy.spin()
    except:
        pass

