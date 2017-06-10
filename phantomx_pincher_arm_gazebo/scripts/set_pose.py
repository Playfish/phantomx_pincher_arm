#!/usr/bin/env python
"""
Usage: set_torso_pose.py <pose>
  <pose> is the height of the torso (0.0 to 0.35m)
"""
import sys
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

if __name__=='__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        exit(-1)

    rospy.init_node('set_torso_pose')

    # The arm is controlled by a joint trajectory action
    rospy.loginfo('Waiting for torso_controller...')
    client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
    client.wait_for_server()
    rospy.loginfo('...connected.')

    # Create a trajectory
    trajectory = JointTrajectory()
    trajectory.joint_names = ["arm_shoulder_pan_joint"]
    trajectory.points.append(JointTrajectoryPoint())
    trajectory.points[0].positions = [float(sys.argv[1])]
    trajectory.points[0].velocities = [0.0]
    trajectory.points[0].accelerations = [0.0]
    trajectory.points[0].time_from_start = rospy.Duration(7.0)  # we can get anywhere by 7s

    # Put this trajectory in an action goal
    rospy.loginfo("Setting torso pose to %f" % trajectory.points[0].positions[0])
    goal = FollowJointTrajectoryGoal()
    goal.trajectory = trajectory
    goal.goal_time_tolerance = rospy.Duration(0.0)

    # Send the goal
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration(8.0))
    rospy.loginfo('...done')
