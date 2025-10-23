from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise

app = Ursina()

window.color = color.rgb(0, 200, 211)
window.exit_button.visible  = False

grassStrokeText = load_texture("grass_14.png")

def input(key):
    if key == "q" or key == "escape":
        quit()

#def update():
##    jeff.rotation_y += 0.1
##    jeff.rotation_x += 0.7


jeff = Entity(model='cube', color=color.pink,
              texture=grassStrokeText)


terrain = Entity(model=None, collider=None)

noise = PerlinNoise(octaves=4, seed=2021)
amp = 3
freq = 12

## genrate floor plan
terrainWidth = 32
for i in range(terrainWidth*terrainWidth):
    bud = Entity(model="cube", color=color.green)
    bud.x = floor(i/terrainWidth)
    bud.z = floor(i%terrainWidth)
    bud.y = floor((noise([bud.x/freq, bud.z]))*amp)
    bud.parent = terrain



terrain.combine(auto_destroy=False)
terrain.collider = "mesh"
terrain.texture = grassStrokeText

subject = FirstPersonController()
subject.x = subject.z = 5
subject.y = 12

app.run()
