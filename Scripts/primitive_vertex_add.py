##############################################################################
# Copyright © 2013 Richard Wilks #
# November 1st #
# #
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or #
# (at your option) any later version. #
# #
# This program is distributed in the hope that it will be useful, #
# but WITHOUT ANY WARRANTY; without even the implied warranty of #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #
# GNU General Public License for more details. #
# #
# A copy of the GPLv3 license is available at #
# https://www.gnu.org/licenses/gpl-3.0.html. #
##############################################################################

bl_info = {
    "name": "Vertex",
    "author": "Richard Wilks",
    "version": (0, 1, 0),
    "blender": (2, 69, 1),
    "location": "View3D > Add > Mesh",
    "description": "Create option to add a vertex object",
    "category": "Object"}

import bpy

# Create a single vertex object... the hard way
class primitive_vertex_add(bpy.types.Operator):
    bl_idname = "mesh.primitive_vertex_add"
    bl_label = "Vertex"
    bl_context = "objectmode"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        mesh = bpy.ops.mesh
        obj = bpy.ops.object
        
        mesh.primitive_plane_add()
        obj.editmode_toggle()
        mesh.merge(type='CENTER')
        obj.editmode_toggle()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(primitive_vertex_add.bl_idname, icon="PLUGIN")

# Register and unregister  
def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_func)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()