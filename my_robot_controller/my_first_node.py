#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__('first_node')
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)  #创建一个定时器，每隔1秒调用一次timer_callback函数

    def timer_callback(self):
        self.get_logger().info('Timer callback triggered!'+str(self.counter_))  #在timer_callback函数中，使用get_logger()方法获取日志记录器，并调用info()方法输出一条信息
        self.counter_+=1  #每次调用timer_callback函数时，counter变量会增加1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)  #调用rclpy.spin()函数，使节点进入循环状态，等待事件发生并处理它们。当节点被关闭时，调用
    rclpy.shutdown()

if __name__ == '__main__':
    main()