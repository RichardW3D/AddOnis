##############################################################################
# Copyright © 2013 Richard Wilks                                             #
# August 11th                                                                #
#                                                                            #
# This program is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by       #
# the Free Software Foundation, either version 3 of the License, or          #
# (at your option) any later version.                                        #
#                                                                            #
# This program is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of             #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the               #
# GNU General Public License for more details.                               #
#                                                                            #
# A copy of the GPLv3 license is available at                                #
# https://www.gnu.org/licenses/gpl-3.0.html.                                 #
##############################################################################

bl_info = {
    "name": "Sculpt Brushes",
    "author": "Richard Wilks",
    "version": (0, 2),
    "blender": (2, 67, 1),
    "location": "Sculpt Mode > Shift-A",
    "description": "A menu with basic brushes",
    "warning": "",
    "wiki_url": "https://github.com/RichardW3D/AddOnis/wiki/Sculpt-Brushes",
    "tracker_url": "",
    "category": "3D View"}
    
import bpy

#Create menu
class SculptBrushes(bpy.types.Menu):
    bl_label = "Sculpt Brushes"
    bl_idname = "sculpt.brush_tools"
    
    #Draw the menu
    def draw(self, context):
        layout = self.layout
        
        #Call menu within menu
        layout.menu(ListDefaultBrushes.bl_idname, 'Brushes')

#Create menu within menu
class ListDefaultBrushes(bpy.types.Menu):
    bl_label = "Brush Defaults"
    bl_idname = "sculpt.brush_menu"
        
        #Create the menu
    def draw(self, context):
        layout = self.layout
        paint = "paint.brush_select"
       # brush = context.scene.tool_settings.sculpt.brush -- retained for future reference     
             
        #Populate menu with brushes
        layout.operator(paint, text = 'Blob', icon = 'BRUSH_BLOB').sculpt_tool = 'BLOB'
        layout.operator(paint, text = 'Clay', icon = 'BRUSH_CLAY').sculpt_tool = 'CLAY'
        layout.operator(paint, text = 'Clay Strips', icon = 'BRUSH_CLAY_STRIPS').sculpt_tool = 'CLAY_STRIPS'
        layout.operator(paint, text = 'Crease', icon = 'BRUSH_CREASE').sculpt_tool = 'CREASE'
        layout.operator(paint, text = 'Draw', icon = 'BRUSH_SCULPT_DRAW').sculpt_tool = 'DRAW'
        layout.operator(paint, text = 'Fill', icon = 'BRUSH_FILL').sculpt_tool = 'FILL'
        layout.operator(paint, text = 'Flatten', icon = 'BRUSH_FLATTEN').sculpt_tool = 'FLATTEN'
        layout.operator(paint, text = 'Grab', icon = 'BRUSH_GRAB').sculpt_tool = 'GRAB'
        layout.operator(paint, text = 'Inflate', icon = 'BRUSH_INFLATE').sculpt_tool = 'INFLATE'
        layout.operator(paint, text = 'Layer', icon = 'BRUSH_LAYER').sculpt_tool = 'LAYER'
        layout.operator(paint, text = 'Mask', icon = 'BRUSH_MASK').sculpt_tool = 'MASK'
        layout.operator(paint, text = 'Nudge', icon = 'BRUSH_NUDGE').sculpt_tool = 'NUDGE'
        layout.operator(paint, text = 'Pinch', icon = 'BRUSH_PINCH').sculpt_tool = 'PINCH'
        layout.operator(paint, text = 'Scrape', icon = 'BRUSH_SCRAPE').sculpt_tool = 'SCRAPE'
        layout.operator(paint, text = 'Smooth', icon = 'BRUSH_SMOOTH').sculpt_tool = 'SMOOTH'
        layout.operator(paint, text = 'Snake Hook', icon = 'BRUSH_SNAKE_HOOK').sculpt_tool = 'SNAKE_HOOK'
        layout.operator(paint, text = 'Thumb', icon = 'BRUSH_THUMB').sculpt_tool = 'THUMB'
        layout.operator(paint, text = 'Twist', icon = 'BRUSH_ROTATE').sculpt_tool = 'ROTATE'

#Keymap and Registration            
addon_keymaps = []

def register():
    bpy.utils.register_class(ListDefaultBrushes)
    bpy.utils.register_class(SculptBrushes)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = 'Sculpt')    
    kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS',  shift=True)
    kmi.properties.name = SculptBrushes.bl_idname
    addon_keymaps.append((km, kmi))

#Keymap removal and Unregistration
def unregister():
    bpy.utils.unregister_class(ListDefaultBrushes)
    bpy.utils.unregister_class(SculptBrushes)
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
