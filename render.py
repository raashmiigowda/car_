import bpy
import os

# =====================================================
# ABSOLUTE PATHS
# =====================================================

CAR_BLEND = r"C:\Users\Rashmii\Downloads\car - Copy ZIP\car - Copy\assets\car\car.glb.blend"

HDR_PATH = r"C:\Users\Rashmii\Downloads\car - Copy ZIP\car - Copy\environments\current_environment.hdr"

OUTPUT = r"C:\Users\Rashmii\Downloads\car - Copy ZIP\car - Copy\outputs\final_render.png"

print("Car file:", CAR_BLEND)
print("Car exists:", os.path.exists(CAR_BLEND))
print("HDR file:", HDR_PATH)
print("HDR exists:", os.path.exists(HDR_PATH))

if not os.path.exists(CAR_BLEND):
    raise FileNotFoundError(f"Car file not found:\n{CAR_BLEND}")

if not os.path.exists(HDR_PATH):
    raise FileNotFoundError(f"HDR file not found:\n{HDR_PATH}")

# =====================================================
# CLEAN SCENE
# =====================================================

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# =====================================================
# APPEND ALL COLLECTIONS FROM .BLEND FILE
# =====================================================

with bpy.data.libraries.load(CAR_BLEND, link=False) as (data_from, data_to):
    data_to.collections = data_from.collections

for collection in data_to.collections:
    if collection is not None:
        bpy.context.scene.collection.children.link(collection)

# =====================================================
# WORLD
# =====================================================

scene = bpy.context.scene

if scene.world is None:
    scene.world = bpy.data.worlds.new("World")

world = scene.world
world.use_nodes = True

nodes = world.node_tree.nodes
links = world.node_tree.links

nodes.clear()

env = nodes.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load(HDR_PATH)

bg = nodes.new("ShaderNodeBackground")
bg.inputs["Strength"].default_value = 1.0

out = nodes.new("ShaderNodeOutputWorld")

links.new(env.outputs["Color"], bg.inputs["Color"])
links.new(bg.outputs["Background"], out.inputs["Surface"])

# =====================================================
# GROUND
# =====================================================

bpy.ops.mesh.primitive_plane_add(size=50, location=(0, 0, 0))
ground = bpy.context.object

try:
    ground.is_shadow_catcher = True
except AttributeError:
    pass

# =====================================================
# CAMERA
# =====================================================

bpy.ops.object.camera_add(location=(5, -7, 3))
camera = bpy.context.object
camera.rotation_euler = (1.2, 0, 0.6)
camera.data.lens = 50

scene.camera = camera

# =====================================================
# RENDER SETTINGS
# =====================================================

scene.render.engine = "CYCLES"
scene.cycles.samples = 128
scene.cycles.use_denoising = True

scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

scene.render.film_transparent = False
scene.render.filepath = OUTPUT

# =====================================================
# RENDER
# =====================================================

print("Rendering...")

bpy.ops.render.render(write_still=True)

print("Render completed!")
print("Saved to:", OUTPUT)