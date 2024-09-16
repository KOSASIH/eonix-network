import cv2
import numpy as np
from pyar import ARScene, ARNode

class ARExperience:
    def __init__(self, ar_scene):
        self.ar_scene = ar_scene
        self.ar_node = ARNode(self.ar_scene, "AR Node")
        self.ar_node.set_position(0, 0, -5)

        # Load the AR marker
        self.ar_marker = cv2.imread("ar_marker.png")

    def run(self):
        # Capture video from the camera
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Detect the AR marker
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250))

            # Draw the AR node
            if ids is not None:
                self.ar_node.set_position(corners[0][0][0], corners[0][0][1], -5)
                self.ar_scene.draw()

            # Display the output
            cv2.imshow("AR Experience", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ar_scene = ARScene()
    ar_experience = ARExperience(ar_scene)
    ar_experience.run()
