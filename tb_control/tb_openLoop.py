import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
#TOTAL TIME OF SIMULATION
MAX_TIME = 10.0
VEL_X = 0.1
class NodeTracker(Node):
    def __init__(self):
        super().__init__('node_tracker')
        #Captures velocity given by the user when running the node to simulate scenarios, by default 0.1 if ommited.
        self.declare_parameter('vel_x', VEL_X)
        # Store the simulation start time when the node is initialized
        self.sim_start_time = self.get_clock().now()
        # Create a timer to print the elapsed simulation time every 1 second and set speed
        self.timer = self.create_timer(0.1, self.timer_callback)
        #Define the topic to send velocities
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        #Track time and current state
        self.total_time = 0
        self.scenario = 1
        #Define the message to send velocities
        self.message = Twist()
    def timer_callback(self):
        current_sim_time = self.get_clock().now()
        diff_time = current_sim_time - self.sim_start_time
        self.total_time  = diff_time.nanoseconds / 1e9
        print(f'Total time is: {self.total_time} seconds')
        self.check_scenario()
    def check_scenario(self):
        """
        This function checks the current scenario and updates the linear velocity of the robot accordingly.

        Parameters:
        None

        Returns:
        None

        The function updates the 'message' attribute of the NodeTracker class. The 'linear.x' value of the 'message'
        is set based on the current scenario and elapsed time. The function also changes the scenario and resets
        relevant variables when necessary.
        Scenario 1: Robot
        """
        param_value = float(self.get_parameter('vel_x').value)
        if self.scenario == 1:
            print(f'Constant speed is {self.message.linear.x} m/s')
            self.message.linear.x = param_value
            if self.total_time >= MAX_TIME:
                print('-------------------------PASS TO SCENARIO 2---------------------------------------')
                self.message.linear.x = 0.0
                self.total_time = 0
                self.scenario = 2
                self.sim_start_time = self.get_clock().now()
        if self.scenario == 2:
            if self.total_time <= 0.3 * MAX_TIME :
                self.message.linear.x = param_value * (1/3) * self.total_time
                print(f'Increasing speed to: {self.message.linear.x} m/s')
            elif self.total_time <= MAX_TIME * 0.7:
                print(f'Constant speed is {self.message.linear.x} m/s')
                self.message.linear.x = param_value
            elif self.total_time > MAX_TIME * 0.7 and self.total_time <= MAX_TIME:
                self.message.linear.x = param_value * (( -1/3 * self.total_time ) + ( MAX_TIME / 3 ))
                print(f'Decreasing speed to: {self.message.linear.x} m/s')
            else:
                self.total_time = 0
                self.scenario = -1
                self.message.linear.x = 0.0
                self.destroy_timer(self.timer)
        print(f'Velocity to send is {self.message.linear.x} m/s')
        self.publisher.publish(self.message)
def main(args=None):
    rclpy.init(args=args)
    node_tracker = NodeTracker()
    rclpy.spin(node_tracker)
    node_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
