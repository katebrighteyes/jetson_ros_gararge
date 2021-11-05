
cd

mkdir rosbagfile

cd rosbagfile

rosbag record -a 

---------------
다른 창

roscore

다른 창

rosrun turtlesim turtlesim_node

다른 창

rosrun turtlesim turtle_teleop_key

--------------

rosbag info 파일이름

rosbag play 파일이름

