#importdefs
import bpy
from g_tools.bpy_itfc_funcs import curve_fs
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, CollectionProperty 
from bpy.types import Operator

#fdef


#opdef
class simple_hair_curve_op(bpy.types.Operator):
    """NODESC"""
    bl_idname = "curve.simple_hair_curve"
    bl_label = "Simple Hair Curve"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category ="Tools"
    bl_options = {'UNDO','REGISTER'}
    

    zero_last_radius = bpy.props.BoolProperty(name = "Set radius of last point to zero", default = True)
    split_bevel = bpy.props.BoolProperty(name = "Split bevel object in two", default = False)
    use_cyclic_u = bpy.props.BoolProperty(name = "Use cyclic",default = True)
    use_fill_caps = bpy.props.BoolProperty(name = "Use fill caps",default = True)

    curve_type = bpy.props.StringProperty(default = "n")
    bevel_curve_type = bpy.props.StringProperty(default = "p")




    def execute(self, context):
        curve_fs.simple_hair_curve(split_bevel = self.split_bevel,curve_type = self.curve_type,bevel_curve_type = self.bevel_curve_type,use_cyclic_u = self.use_cyclic_u,use_fill_caps = self.use_fill_caps,zero_last_radius = self.zero_last_radius)
        return {'FINISHED'}
        
class curve_to_armature_op(bpy.types.Operator):
    """NODESC"""
    bl_idname = "curve.curve_to_armature"
    bl_label = "Curve to armature"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category ="Tools"
    bl_options = {'UNDO','REGISTER'}
    
    use_apply_on_spline = bpy.props.BoolProperty(default = True)
    make_new_arm = bpy.props.BoolProperty(default = True)
    base_name = bpy.props.StringProperty(default = "Bone")
    align_bones = bpy.props.BoolProperty(default = True)
    do_bone_parent = bpy.props.BoolProperty(default = True)
    
    def execute(self, context):
        curve_fs.curve_to_armature(make_new_arm = self.make_new_arm,base_name = self.base_name,use_apply_on_spline = self.use_apply_on_spline,align_bones = self.align_bones,do_bone_parent = self.do_bone_parent)
        return {'FINISHED'}
        
        
class GCurvePanel(bpy.types.Panel):
    """Creates a Panel in the 3D View"""
    bl_label = "GCurve"    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "G Tools"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        #rowdefs
        row = layout.row()
        row.operator("curve.simple_hair_curve")
        row = layout.row()
        row.operator("curve.curve_to_armature")
        
        
def register():
    #regdef
    bpy.utils.register_class(simple_hair_curve_op)
    bpy.utils.register_class(curve_to_armature_op)
    bpy.utils.register_class(GCurvePanel)

def unregister():
    #unregdef
    bpy.utils.unregister_class(simple_hair_curve_op)
    bpy.utils.unregister_class(curve_to_armature_op)
    bpy.utils.unregister_class(GCurvePanel)
    
    