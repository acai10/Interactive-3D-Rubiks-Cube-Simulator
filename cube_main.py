import pyvista as pv
from pyvistaqt import BackgroundPlotter
import numpy as np

interval = 300  # ms

class Rubix:
    def __init__(self, dim=3):
        # Key events
        self.key_pressed = False
        self.direction = 1  # 1 -> 90, (-1) -> (-90)

        # Dimension of the cube
        self.dim = dim
        self.cubes_num = self.dim ** self.dim

        # Initialization
        self.cube = pv.Cube()

        # Colormap
        self.cube.cell_data["face_ids"] = np.arange(6)

        # Block mesh
        self.blocks = [plotter.add_mesh(self.cube,
                                        show_edges=True,
                                        cmap=["red",
                                              "orange",
                                              "cyan",
                                              "green",
                                              "yellow",
                                              "white"]) for _ in range(self.cubes_num)]

        # For transformations
        self.transforms = [pv.Transform() for _ in range(self.cubes_num)]

        # Positions
        self.positions = [(x,y,z) for x in range(self.dim) for y in range(self.dim) for z in range(self.dim)]

        # Blocks with positions - (x,y,z): block
        self.actor = {pos: block for pos, block in zip(self.positions, self.blocks)}

        # Constructing the cube (set the individual positions)
        for pos, block in self.actor.items():
            block.position = pos

    def update_positions(self):
        self.actor = {tuple(map(round, block.center)): block for block in self.actor.values()}
        new_block_dict = {}
        for pos in self.positions:
            for k, v in self.actor.items():
                if pos == k:
                    new_block_dict[pos] = v
                    break
        self.actor = new_block_dict

# Rotations
def rotation_right():
    rotation_center = np.array(magic_cube.positions[4])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in magic_cube.positions:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_x(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_x(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

def rotation_left():
    rotation_center = np.array(magic_cube.positions[4])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in magic_cube.positions[18:]:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_x(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_x(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

def rotation_above():
    rotation_center = np.array(magic_cube.positions[14])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in magic_cube.positions[2::3]:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_z(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_z(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

def rotation_under():
    rotation_center = np.array(magic_cube.positions[14])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in magic_cube.positions[0::3]:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_z(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_z(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

def rotation_front():
    rotation_center = np.array(magic_cube.positions[16])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in [y for y in magic_cube.positions if y[1] == 2]:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_y(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_y(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

def rotation_back():
    rotation_center = np.array(magic_cube.positions[10])
    ind = 0
    for pos, c in magic_cube.actor.items():
        if pos in [y for y in magic_cube.positions if y[1] == 0]:
            ind += 1

            # Transform
            t = magic_cube.transforms[ind]
            t.translate(-rotation_center)
            t.rotate_y(magic_cube.direction*30)
            t.translate(rotation_center)
            c.transform(t, inplace=True)

            # Render
            plotter.render()

            # Put back the transformation
            t.translate(-rotation_center)
            t.rotate_y(magic_cube.direction*(-30))
            t.translate(rotation_center)

            if ind == 9: break

# Call a rotation and lock the Key
def call_rot_up_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_right, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_down_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_right, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_up_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_left, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_down_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_left, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_above_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_above, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_above_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_above, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_under_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_under, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_under_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_under, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_front_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_front, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_front_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_front, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_back_right():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = 1
    plotter.add_callback(rotation_back, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

def call_rot_back_left():
    if magic_cube.key_pressed: return
    magic_cube.key_pressed = True
    magic_cube.direction = -1
    plotter.add_callback(rotation_back, interval=10, count=3)
    plotter.add_callback(unlock_key, interval=interval, count=1)
    magic_cube.update_positions()

# Unlock the Key
def unlock_key():
    magic_cube.key_pressed = False

if __name__ == "__main__":
    try:
        # Background
        pv.global_theme.background = 'black'

        # Create the plotter window
        plotter = BackgroundPlotter(title='Magic Cube')
        plotter.hide_axes()

        # Create the cube
        magic_cube = Rubix(3)

        # Set Camera
        plotter.reset_camera(render=True)

        # Keys
        plotter.add_key_event(key='l', callback=call_rot_up_right)
        plotter.add_key_event(key='L', callback=call_rot_down_right)

        plotter.add_key_event(key='j', callback=call_rot_up_left)
        plotter.add_key_event(key='J', callback=call_rot_down_left)

        plotter.add_key_event(key='i', callback=call_rot_above_right)
        plotter.add_key_event(key='I', callback=call_rot_above_left)
        
        plotter.add_key_event(key='k', callback=call_rot_under_right)
        plotter.add_key_event(key='K', callback=call_rot_under_left)

        plotter.add_key_event(key='o', callback=call_rot_front_right)
        plotter.add_key_event(key='O', callback=call_rot_front_left)

        plotter.add_key_event(key='u', callback=call_rot_back_right)
        plotter.add_key_event(key='U', callback=call_rot_back_left)

        # Execute
        plotter.app.exec_()

    except KeyboardInterrupt:
        print("Animation end.")
