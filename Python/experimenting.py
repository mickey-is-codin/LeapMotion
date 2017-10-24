import Leap, sys, thread, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

x = []
handHeight = []

class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    def on_init(self, controller):
        print "Initialized"
        
    def on_connect(self, controller):
        print "Motion Sensor Connected"
        
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_disconnect(self, controller):
        print "Motion Sensor Disconnected"
        
    def on_exit(self, controller):
        print "Exited"
        
    def on_frame(self, controller):
        frame = controller.frame()

        positionRight = 0

        """print "Frame ID: " + str(frame.id) \
            + " Timestamp: " + str(frame.timestamp) \
            + " Number of Hands: " + str(len(frame.hands)) \
            + " Number of Fingers: " + str(len(frame.fingers)) \
            + " Number of Tools: " + str(len(frame.tools)) \
            + " Number of Gestures: " + str(len(frame.gestures()))"""

        for hand in frame.hands:
            if hand.is_left:
                handType = "Left Hand"

                leftThumb = hand.fingers[0]
                leftIndex = hand.fingers[0]
                leftMiddle = hand.fingers[0]
                leftRing = hand.fingers[0]
                leftPinky = hand.fingers[0]

            else:
                handType = "Right Hand"

                rightThumb = hand.fingers[0]
                rightIndex = hand.fingers[0]
                rightMiddle = hand.fingers[0]
                rightRing = hand.fingers[0]
                rightPinky = hand.fingers[0]

                positionRight = hand.palm_position.y

                handHeight.append(positionRight)

            #print handType + " Hand ID: " + str(hand.id) + " Palm Position: " + str(hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction

            #print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG)
            #print "Roll: " + str(direction.roll * Leap.RAD_TO_DEG)
            #print "Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)

        #x.append(frame.time)
        #plt.plot(x,handHeight)
        print "Hand Height (mm): " + "%.0f" % positionRight

    
def main():
    listener = LeapMotionListener()
    controller = Leap.Controller()
    
    controller.add_listener(listener)
    
    print "Press enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

        
if __name__ == "__main__":
    main()