bl_info = {
    "name" : "Ashmo Panel",
    "author" : "Chris Cummings",
    "version" : (1, 0),
    "blender" : (2, 83, 4),
    "location" : "View3d > Tool",
    "warning" : "", # warnings to display to the user of the addon
    "wiki_url" : "",
    "category" : "",
}



import bpy # importing blender python

def test_function():
    print("My function")

# create a menu button that centers the selection to (0,0,0) and brings up the export(.fbx) menu
class CenterOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.center"
    bl_label = "Center Mesh and Export(.fbx)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.view_layer.objects.active.location = (0,0,0) # centers the selected object
        bpy.ops.export_scene.fbx("INVOKE_DEFAULT") # brings up export .fbx menu
        return {'FINISHED'}

class FreezeTransformsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.freeze"
    bl_label = "Freeze Transforms"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.view_layer.objects.active.delta_location = bpy.context.view_layer.objects.active.location
        bpy.context.view_layer.objects.active.location = (0,0,0) # centers the selected object
        bpy.context.view_layer.objects.active.delta_rotation_euler = bpy.context.view_layer.objects.active.rotation_euler
        bpy.context.view_layer.objects.active.rotation_euler = (0,0,0) # fixes rotation
        bpy.context.view_layer.objects.active.delta_scale = bpy.context.view_layer.objects.active.scale
        bpy.context.view_layer.objects.active.scale = (1,1,1) # sets scale to 1
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0) #set cursor to 0,0,0
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN') #set origin to cursor
        return {'FINISHED'}

# create a panel on the sidebar
class AshmoPanel(bpy.types.Panel):
    bl_label = "Ashmo Panel"
    bl_idname = "PT_AshmoPanel"
    bl_space_type = "VIEW_3D" # defines on what view the panel will appear, in this case 3d view
    bl_region_type = "UI"
    bl_category = "Ashmo"
    
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row() # adds an empty row
        row.operator("object.center", icon="PIVOT_CURSOR")
        row = layout.row() # adds an empty row
        row.operator("object.freeze", icon="CURSOR")
        
# registers and unregisters the class
def register():
    bpy.utils.register_class(AshmoPanel)
    bpy.utils.register_class(CenterOperator)
    bpy.utils.register_class(FreezeTransformsOperator)
    
def unregister():
    bpy.utils.register_class(AshmoPanel)
    bpy.utils.register_class(CenterOperator)
    bpy.utils.register_class(FreezeTransformsOperator)
    
if __name__ == "__main__":
    register()