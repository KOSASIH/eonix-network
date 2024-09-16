import pygame
from pyvr import VRScene, VRNode

class VRExperience:
    def __init__(self, vr_scene):
        self.vr_scene = vr_scene
        self.vr_node = VRNode(self.vr_scene, "VR Node")
        self.vr_node.set_position(0, 0, -5)

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        # Run the VR experience
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Draw the VR node
            self.vr_scene.draw()
            self.screen.blit(self.vr_scene.get_surface(), (0, 0))

            # Update the screen
            pygame.display.flip()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    vr_scene = VRScene()
    vr_experience = VRExperience(vr_scene)
    vr_experience.run()
