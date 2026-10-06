"""Reproducible Blender scene for the irrational-orbit proof. CC0-1.0.

Run: blender --background --python conic-orbit-torus.py
Requires Blender 4.5. The Arial font is used when installed, with Blender's
built-in font as a fallback. All geometry, sample counts and mathematical
labels are defined below; the finite drawing does not prove recurrence.
"""
import bpy, math, json, hashlib
from pathlib import Path
from mathutils import Vector
HERE=Path(__file__).resolve().parent
bpy.ops.wm.read_factory_settings(use_empty=True)
scene=bpy.context.scene
scene.render.engine='BLENDER_EEVEE_NEXT'
scene.render.resolution_x=1600; scene.render.resolution_y=1150; scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.render.film_transparent=False
scene.render.use_stamp=False
scene.render.use_stamp_filename=False
scene.render.use_stamp_note=False
scene.world=bpy.data.worlds.new('White background');scene.world.use_nodes=True
scene.world.node_tree.nodes['Background'].inputs[0].default_value=(1,1,1,1)
scene.world.node_tree.nodes['Background'].inputs[1].default_value=.8
scene.view_settings.view_transform='Standard'
def mat(name,color):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*color,1);bs.inputs['Roughness'].default_value=.7
    return m
ink=mat('Label ink',(.018,.040,.070));grid=mat('Torus coordinate grid',(.56,.65,.71))
for material,color in [(ink,(.007,.012,.020)),(grid,(.21,.26,.31))]:
    nodes=material.node_tree.nodes;nodes.clear()
    out=nodes.new('ShaderNodeOutputMaterial');emission=nodes.new('ShaderNodeEmission')
    emission.inputs['Color'].default_value=(*color,1)
    material.node_tree.links.new(emission.outputs[0],out.inputs['Surface'])
blue=mat('Sampled orbit',(.035,.30,.61));red=mat('Basepoint',(.71,.14,.08));gold=mat('Return point m5',(.96,.53,.06))
R=1.8;r=.6
def E(theta,phi):return ((R+r*math.cos(phi))*math.cos(theta),(R+r*math.cos(phi))*math.sin(theta),r*math.sin(phi))
def curve(name,points,material,radius=.008):
    c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.resolution_u=1;c.bevel_depth=radius;c.bevel_resolution=2
    s=c.splines.new('POLY');s.points.add(len(points)-1)
    for p,v in zip(s.points,points):p.co=(*v,1)
    o=bpy.data.objects.new(name,c);scene.collection.objects.link(o);o.data.materials.append(material);return o
for k in range(12):curve('Meridian '+str(k),[E(2*math.pi*k/12,2*math.pi*j/192) for j in range(193)],grid,.005)
for k in range(8):curve('Parallel '+str(k),[E(2*math.pi*j/256,2*math.pi*k/8) for j in range(257)],grid,.005)
N=6000;umax=20*math.pi
curve('Orbit sample 0 to20pi',[E(umax*k/N,math.sqrt(2)*umax*k/N) for k in range(N+1)],blue,.014)
def point(name,position,material,radius):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,radius=radius,location=position)
    o=bpy.context.object;o.name=name;o.data.materials.append(material)
    for face in o.data.polygons:face.use_smooth=True
point('j0',(R+r,0,0),red,.046)
epsilon=1/(5*math.sqrt(2)+7)
point('j10pi return',E(0,2*math.pi*epsilon),gold,.04)
camdata=bpy.data.cameras.new('Orthographic camera');cam=bpy.data.objects.new('Orthographic camera',camdata);scene.collection.objects.link(cam)
cam.location=(7,-9,7);cam.rotation_euler=(-cam.location).to_track_quat('-Z','Y').to_euler();camdata.type='ORTHO';camdata.ortho_scale=7.1;scene.camera=cam
bpy.context.view_layer.update()
fontpath=Path('C:/Windows/Fonts/arial.ttf')
font=bpy.data.fonts.load(str(fontpath)) if fontpath.exists() else None
def label(body,x,y,size=.10):
    data=bpy.data.curves.new('Caption','FONT');data.body=body;data.size=size
    if font:data.font=font
    o=bpy.data.objects.new('Caption',data);scene.collection.objects.link(o)
    o.location=cam.matrix_world@Vector((x,y,-5));o.rotation_euler=cam.rotation_euler;data.materials.append(ink)
label('An irrational orbit on the torus',-3.2,2.17,.23)
label('j(u) = (exp(i u), exp(i sqrt(2) u)) in S¹ x S¹',-3.2,1.97,.13)
label('Blue: numerical curve for 0 <= u <= 20 pi; 6,001 samples.',-3.2,-1.80,.105)
label('Red: j(0). Gold: j(10 pi), a return close to j(0) after a long parameter interval.',-3.2,-1.98,.105)
label('Shown embedding: ((1.8 + 0.6 cos(phi)) cos(theta), (1.8 + 0.6 cos(phi)) sin(theta), 0.6 sin(phi)).',-3.2,-2.15,.085)
label('theta = u, phi = sqrt(2) u. The finite picture is not a proof of density or recurrence.',-3.2,-2.29,.09)
label('Proof: SH02-CON-EXAMPLE-DENSE-ORBIT. Independent course construction.',-3.2,-2.43,.078)
for name,loc,energy,size in [('Key',(2,-5,8),850,6),('Fill',(-5,-2,3),500,5)]:
    data=bpy.data.lights.new(name,'AREA');data.energy=energy;data.shape='DISK';data.size=size
    ob=bpy.data.objects.new(name,data);scene.collection.objects.link(ob);ob.location=loc;ob.rotation_euler=(-ob.location).to_track_quat('-Z','Y').to_euler()
scene.render.filepath=str(HERE/'orbit-torus.png')
bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'orbit-torus.blend'))
bpy.ops.render.render(write_still=True)
report={'blender_version':bpy.app.version_string,'scene':'orbit-torus.blend','image':'orbit-torus.png','curve_parameter_interval':['0','20*pi'],'curve_sample_count':N+1,'major_radius':'1.8','minor_radius':'0.6','slope':'sqrt(2)','basepoint':[2.4,0,0],'return_parameter':'10*pi','return_epsilon':'1/(5*sqrt(2)+7)','wire_grid':'12 meridians and8 parallels; not sheaf support','visual_tube_radius':.014,'no_intrinsic_metric_or_density_claim':True,'bindings':[]}
for name in [Path(__file__).name,'orbit-torus.blend','orbit-torus.png']:
    raw=(HERE/name).read_bytes();report['bindings'].append({'file':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(HERE/'blender-render.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
