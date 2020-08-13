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

# create a custom operator for the custom button
class CenterOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.center"
    bl_label = "Center Mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        active_obj = bpy.context.view_layer.objects.active
        active_obj.location.x = 0
        active_obj.location.y = 0
        active_obj.location.z = 0
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
        row.operator("object.center", icon="CUBE")
        
# registers and unregisters the class
def register():
    bpy.utils.register_class(AshmoPanel)
    bpy.utils.register_class(CenterOperator)
    
def unregister():
    bpy.utils.register_class(AshmoPanel)
    bpy.utils.register_class(CenterOperator)
    
if __name__ == "__main__":
    register()