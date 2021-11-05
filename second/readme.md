
cd

mkdir rosbagfile

cd rosbagfile

---------------
다른 창

roscore

다른 창

rosrun turtlesim turtlesim_node

다른 창

rosrun turtlesim turtle_teleop_key

--------------
rosbag record -a 

터틀심 테스트를 한다.

테스트 후 ctl-C

rosbag info 파일이름

rosbag play 파일이름

