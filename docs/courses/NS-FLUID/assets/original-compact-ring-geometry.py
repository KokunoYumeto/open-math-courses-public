"""Exact containing-torus geometry for EX14–EX18; run with Blender in background."""
import bpy,math
from mathutils import Vector
from pathlib import Path
OUT=Path(__file__).resolve().parent
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32
scene.cycles.use_denoising=True;scene.render.resolution_x=1500;scene.render.resolution_y=1000;scene.render.resolution_percentage=100
scene.world.color=(.8,.8,.8)
scene.view_settings.view_transform='Standard'
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.95,.97,1,1)
scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
def mat(name,col,alpha=1):
 m=bpy.data.materials.new(name);m.diffuse_color=(*col,alpha);m.use_nodes=True
 nt=m.node_tree;nt.nodes.clear();out=nt.nodes.new('ShaderNodeOutputMaterial')
 if alpha<1:
  trans=nt.nodes.new('ShaderNodeBsdfTransparent');surf=nt.nodes.new('ShaderNodeBsdfDiffuse');surf.inputs[0].default_value=(*col,1)
  mix=nt.nodes.new('ShaderNodeMixShader');mix.inputs[0].default_value=alpha;nt.links.new(trans.outputs[0],mix.inputs[1]);nt.links.new(surf.outputs[0],mix.inputs[2]);nt.links.new(mix.outputs[0],out.inputs[0])
 else:
  surf=nt.nodes.new('ShaderNodeBsdfDiffuse');surf.inputs[0].default_value=(*col,1);nt.links.new(surf.outputs[0],out.inputs[0])
 return m
blue=mat('Containing torus',(.16,.42,.7),.16);wire=mat('Torus coordinate curves',(.18,.39,.65))
gold=mat('Original meridian boundary',(.9,.47,.05));dark=mat('Original coordinate markers',(.08,.12,.18))
def curve(name,pts,material,width=.035,closed=False):
 cu=bpy.data.curves.new(name,'CURVE');cu.dimensions='3D';cu.bevel_depth=width;cu.bevel_resolution=2
 sp=cu.splines.new('POLY');sp.points.add(len(pts)-1)
 for p,co in zip(sp.points,pts):p.co=(*co,1)
 sp.use_cyclic_u=closed;ob=bpy.data.objects.new(name,cu);bpy.context.collection.objects.link(ob);ob.data.materials.append(material);return ob
ell=12.;R=4.
bpy.ops.mesh.primitive_torus_add(major_radius=ell,minor_radius=R,major_segments=128,minor_segments=48)
tor=bpy.context.object;tor.name='s=ell+r, r^2+z^2=R^2';tor.data.materials.append(blue)
for p in tor.data.polygons:p.use_smooth=True
for theta in [math.pi/2,math.pi,3*math.pi/2]:
 curve('Meridian coordinate circle',[( (ell+R*math.cos(t))*math.cos(theta),(ell+R*math.cos(t))*math.sin(theta),R*math.sin(t)) for t in [2*math.pi*j/160 for j in range(160)]],wire,.018,True)
for v in [math.pi/2,3*math.pi/2]:
 curve('Latitude coordinate circle',[((ell+R*math.cos(v))*math.cos(t),(ell+R*math.cos(v))*math.sin(t),R*math.sin(v)) for t in [2*math.pi*j/192 for j in range(192)]],wire,.018,True)
curve('Original meridian disk boundary',[(ell+R*math.cos(t),0,R*math.sin(t)) for t in [2*math.pi*j/192 for j in range(192)]],gold,.095,True)
curve('Physical axis',[(0,0,-7),(0,0,9)],dark,.065)
curve('Original center radius',[(0,0,0),(ell,0,0)],dark,.055)
curve('Original minor radius',[(ell,0,0),(ell,0,R)],gold,.055)
for pt in [(0,0,0),(ell,0,0)]:
 bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=.16,location=pt);bpy.context.object.data.materials.append(dark)
bpy.ops.object.camera_add(location=(31,-42,28));cam=bpy.context.object
cam.rotation_euler=(Vector((0,0,0))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=43;scene.camera=cam
def text_world(text,pos,size=.65,material=dark):
 cu=bpy.data.curves.new(text,'FONT');cu.body=text;cu.size=size;cu.align_x='CENTER'
 ob=bpy.data.objects.new(text,cu);bpy.context.collection.objects.link(ob);ob.location=pos;ob.rotation_euler=cam.rotation_euler;ob.data.materials.append(material)
 return ob
text_world('ell = 12',(5,-1,1.4),.75)
text_world('R = 4',(13.8,-1,2.1),.65,gold)
text_world('physical axis: s = 0',(-1,0,10),.7)
text_world('meridian origin',(12,-1,-1.3),.62)
def overlay(txt,y,size=.67):
 ob=text_world(txt,(0,0,0),size);ob.parent=cam;ob.location=(0,y,-48);ob.rotation_euler=(0,0,0)
overlay('A compact meridian disk becomes a torus in physical space',12.6,.82)
overlay('Physical radius s = ell + r; volume element = s dr dtheta dz',-11.7,.66)
overlay('EX14-EX18. The surface bounds the support; it is not a vortex-amplitude plot.',-12.7,.53)
bpy.ops.object.light_add(type='AREA',location=(0,-14,25));bpy.context.object.data.energy=2300;bpy.context.object.data.shape='DISK';bpy.context.object.data.size=20
scene.render.image_settings.file_format='PNG';scene.render.filepath='//original-compact-ring-geometry.png'
scene.render.use_stamp_filename=False
for screen in bpy.data.screens:
 for area in screen.areas:
  for space in area.spaces:
   if space.type=='FILE_BROWSER' and space.params:
    space.params.directory=b'//'
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'original-compact-ring-geometry.blend'))
bpy.ops.render.render(write_still=True)

