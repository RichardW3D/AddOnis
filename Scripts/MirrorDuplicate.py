##############################################################################
#    Copyright © 2013  Richard Wilks                                         #
#    August 11th                                                             #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    A copy of the GPLv3 license is available at                             #
#    https://www.gnu.org/licenses/gpl-3.0.html.                              #
##############################################################################

bl_info = {
    "name": "Mirror Duplicate",
    "author": "Richard Wilks",
    "version": (0, 0, 4),
    "blender": (2, 68, 2),
    "location": "View3D > Tool Shelf",
    "description": "Mirror objects around the 3D Cursor via duplication",
    "category": "3D View"}

import bpy

bpy.types.Scene.apply_mirror_duplicate = bpy.props.BoolProperty(
    name="Apply Mirror",
    description="Apply the scale and recalculate the normals",
    default=False)
    
bpy.types.Scene.linked_duplicate = bpy.props.BoolProperty(
    name="Linked",
    description="Create linked duplicates",
    default=False)

#Mirror along the X-axis
class Mirror_X(bpy.types.Operator):
    """Mirror objects across the X-axis via duplication"""
    bl_idname = "object.mirror_x"
    bl_label = "Mirror X"
    bl_context = "objectmode"
    bl_options = {"UNDO"}

    def execute(self, context):
        scn = bpy.context.scene   
        bpy.ops.object.duplicate(linked=scn.linked_duplicate)
        selected = context.selected_objects
        apply_mirror = scn.apply_mirror_duplicate
        
        #Store current pivot point and switch to 3D Cursor
        pivot = bpy.context.space_data.pivot_point
        context.space_data.pivot_point = 'CURSOR'

        for obj in selected:
            #Lock scaling in unwanted axes
            obj.lock_scale = [False, True, True]
            
            #Correct the rotation of duplicate positive <--> negative
            obj.rotation_euler[1] = -obj.rotation_euler[1]
            obj.rotation_euler[2] = -obj.rotation_euler[2]
                    
        bpy.ops.transform.resize(value=(-1, 1, 1))
        
        #Restore locks and pivot to original states
        for obj in selected:
            scn.objects.active = obj
            obj.lock_scale = [False, False, False]
            
            #Apply Scale and recalculate normals if Apply Mirror is checked
            if apply_mirror == True:
                bpy.ops.object.transform_apply(scale=True)
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.normals_make_consistent()
                bpy.ops.object.editmode_toggle()
      
        bpy.context.space_data.pivot_point = pivot
        scn.apply_mirror_duplicate = False
        scn.linked_duplicate = False
        return {'FINISHED'}

#Mirror along the Y-axis    
class Mirror_Y(bpy.types.Operator):
    """Mirror objects across the Y-axis via duplication"""
    bl_idname = "object.mirror_y"
    bl_label = "Mirror Y"
    bl_context = "objectmode"
    bl_options = {"UNDO"}

    def execute(self, context):
        scn = bpy.context.scene
        bpy.ops.object.duplicate(linked=scn.linked_duplicate)
        selected = context.selected_objects
        apply_mirror = scn.apply_mirror_duplicate
        
        #Store current pivot point and switch to 3D Cursor
        pivot = bpy.context.space_data.pivot_point
        context.space_data.pivot_point = 'CURSOR'

        for obj in selected:
            #Lock scaling in unwanted axes
            obj.lock_scale = [True, False, True]
            
            #Correct the rotation of duplicate positive <--> negative
            obj.rotation_euler[0] = -obj.rotation_euler[0]
            obj.rotation_euler[2] = -obj.rotation_euler[2]
                    
        bpy.ops.transform.resize(value=(1, -1, 1))
        
        #Restore locks and pivot to original states
        for obj in selected:
            scn.objects.active = obj
            obj.lock_scale = [False, False, False]
            
            #Apply Scale and recalculate normals if Apply Mirror is checked
            if apply_mirror == True:
                bpy.ops.object.transform_apply(scale=True)
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.normals_make_consistent()
                bpy.ops.object.editmode_toggle()
      
        bpy.context.space_data.pivot_point = pivot
        scn.apply_mirror_duplicate = False
        scn.linked_duplicate = False
        return {'FINISHED'}

#Mirror along the Z-axis    
class Mirror_Z(bpy.types.Operator):
    """Mirror objects across the Z-axis via duplication"""
    bl_idname = "object.mirror_z"
    bl_label = "Mirror Z"
    bl_context = "objectmode"
    bl_options = {"UNDO"}

    def execute(self, context):
        scn = bpy.context.scene
        bpy.ops.object.duplicate(linked=scn.linked_duplicate)
        selected = context.selected_objects
        apply_mirror = scn.apply_mirror_duplicate
        
        #Store current pivot point and switch to 3D Cursor
        pivot = bpy.context.space_data.pivot_point
        context.space_data.pivot_point = 'CURSOR'

        for obj in selected:
            #Lock scaling in unwanted axes
            obj.lock_scale = [True, True, False]
            
            #Correct the rotation of duplicate positive <--> negative
            obj.rotation_euler[0] = -obj.rotation_euler[0]
            obj.rotation_euler[1] = -obj.rotation_euler[1]
                    
        bpy.ops.transform.resize(value=(1, 1, -1))
        
        #Restore locks and pivot to original states
        for obj in selected:
            scn.objects.active = obj
            obj.lock_scale = [False, False, False]
            
            #Apply Scale and recalculate normals if Apply Mirror is checked
            if apply_mirror == True:
                bpy.ops.object.transform_apply(scale=True)
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.normals_make_consistent()
                bpy.ops.object.editmode_toggle()
      
        bpy.context.space_data.pivot_point = pivot
        scn.apply_mirror_duplicate = False
        scn.linked_duplicate = False
        return {'FINISHED'}

#Draw buttons in Tool Shelf
class VIEW3D_PT_mirrorduplicate(bpy.types.Panel):
    bl_label = "Mirror Duplicate"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"  

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scn = context.scene
        
        #If Linked is enabled, hide Apply Mirror and vice versa
        sub = layout.split()
        if scn.linked_duplicate == False:
            sub.prop(scn, 'apply_mirror_duplicate')
        
        if scn.apply_mirror_duplicate == False:
            sub.prop(scn, 'linked_duplicate')

        sub = layout.split()
        sub.operator('object.mirror_x')
        sub.operator('object.mirror_y')
        sub.operator('object.mirror_z')


#registration of operator classes and panel class      
def register():
    bpy.utils.register_class(VIEW3D_PT_mirrorduplicate)
    bpy.utils.register_class(Mirror_X)
    bpy.utils.register_class(Mirror_Y)
    bpy.utils.register_class(Mirror_Z)

#unregistration of operator classes and panel class 
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_mirrorduplicate)
    bpy.utils.unregister_class(Mirror_X)
    bpy.utils.unregister_class(Mirror_Y)
    bpy.utils.unregister_class(Mirror_Z)

#if __name__ == "__main__":
#    register()
    
