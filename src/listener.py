#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

'''
	pub2 = rospy.Publisher('filtered', String, queue_size=10)
#	rospy.init_node('listener', anonymous=True)
#	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		tenmex = "I receive 10 messagges | %s" % rospy.get_time()
		rospy.loginfo(tenmex)
		pub2.publish(tenmex)
#		rate.sleep()
'''

class Counter:
	def __init__(self):
		self.counter = 0

	def inc(self):
		if self.counter == 10:
			self.counter = 1
		else:
			self.counter = self.counter + 1
		return self.counter


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

	if c.inc() == 10:
		tenmex = "I receive 10 messagges | %s" % rospy.get_time()
		rospy.loginfo(tenmex)
		pub.publish(tenmex)


def listener():

	global c
	c = Counter()

	global pub
	pub = rospy.Publisher("filtered", String, queue_size=10)

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("chatter", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()







if __name__ == '__main__':
	listener()
