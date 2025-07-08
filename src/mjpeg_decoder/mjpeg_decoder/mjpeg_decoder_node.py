import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

class MJPEGDecoder(Node):
    def __init__(self, input_topic, output_topic):
        super().__init__('mjpeg_decoder')
        self.bridge = CvBridge()
        self.sub = self.create_subscription(Image, input_topic, self.callback, 10)
        self.pub = self.create_publisher(Image, output_topic, 10)
        self.get_logger().info(f"Subscribed to: {input_topic} | Publishing to: {output_topic}")

    def callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is not None:
            rgb_msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
            rgb_msg.header = msg.header
            self.pub.publish(rgb_msg)
        else:
            self.get_logger().warn('Frame could not be decoded.')

def main(args=None):
    rclpy.init(args=args)
    # Standardwerte (für Kamera 1)
    input_topic = '/fisheye_left/image_raw'
    output_topic = '/fisheye_left/image_rgb'
    # Wenn per Argument übergeben, diese nutzen
    if len(sys.argv) > 2:
        input_topic = sys.argv[1]
        output_topic = sys.argv[2]
    node = MJPEGDecoder(input_topic, output_topic)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
