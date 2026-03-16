修改文件后，需要在工作空间目录下执行colcon built
或者使用colcon built --symlink-install 
后者只需执行一次，后续修改后保存后自动更新
rqt_graph ; 查看图形化概览
ros2 topic list ;例举当前话题
ros2 topic info /"topic_name" ;查看话题信息
ros2 interface show "topic_type" ;the type can be cheak by line6,this line can show the interface of the type
ros2 topic echo /"topic_name" ; get message from "topic_name",seen as a subscriber node
