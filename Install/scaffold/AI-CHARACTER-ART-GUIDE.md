**AI to 3D Character**
**Complete Step-by-Step Guide**
Godot 4 Colony Sim — Beginner Friendly Edition

# **Before You Start**
This guide walks you through making 3D characters for your game using AI tools and Blender. You do not need to be an expert. Every single step is explained in plain language.

Read this whole section before you do anything else. It will save you a lot of time.

## **What You Are Making**
By the end of this guide you will have:
- 2 base character meshes (one male, one female) with 6 body parts each
- 6 cybernetic replacement pieces (arms, legs, chest, head)
- 6 hairstyle meshes (3 for male characters, 3 for female)
- All of these working correctly inside Godot 4

## **Tools You Need to Install First**
Install all of these before starting. They are all free unless marked with a cost.

| Tool | Where to Get It | What It Does |
|------|----------------|--------------|
| Blender | blender.org | The main 3D program. Free. |
| Godot 4 | godotengine.org | Your game engine. Free. |
| Auto-Rig Pro | blendermarket.com | Blender addon for rigging. Costs money (~$40). Worth it. |
| ComfyUI Cloud | comfy.org/cloud | Makes AI concept images. Free tier available. |
| Tripo AI | tripo3d.ai | Turns images into 3D meshes. Free credits to start. |
| Hunyuan3D | 3d.hunyuan.tencent.com | Cleans up mesh topology. Free. |
| Nano Banana Pro | fal.ai/models/fal-ai/nano-banana-pro | Splits character images into parts. Pay per use. |

## **The Golden Rules**
NEVER join your mesh chunks together in Blender. Each body part (head, torso, arms, legs) must always stay as a separate object. If you accidentally join them, press Ctrl+Z immediately to undo.
Always save your work before trying something new. In Blender: File > Save. Do this every 10 minutes.
Do the ENTIRE pipeline on just the male base mesh first before touching anything else. This proves everything works and teaches you the process. The second character will be much faster.

## **How This Guide Is Structured**
This guide has 12 phases. Phases 1 through 11 build the assets. Phase 12 builds a character viewer in Godot so you can test everything works together — swapping cybernetics, changing blend shapes, toggling hair, previewing overlays.

Each phase has numbered steps. Inside some steps there are lettered sub-steps (a, b, c). Follow them in order.

You will see coloured boxes throughout:
- Green box = you did it right, this is what success looks like
- Yellow box = be careful here, common mistake coming up
- Red box = stop, read this before doing anything
- Blue box = helpful hint to make things easier

## **Two Paths: MVP and Final**
Every phase in this guide has a fast MVP path and a slower Final path. As a solo developer, your first goal is a working character system, not a perfect one. Get something working first. Polish it second.

| Phase | MVP Path (fast, gets it working) | Final Path (clean, scalable) |
|-------|----------------------------------|------------------------------|
| Phase 3 (3D gen) | Accept whatever Tripo gives you | Regenerate until you get a clean mesh |
| Phase 4 (cleanup) | Skip Shrinkwrap, just position roughly | Close all gaps cleanly |
| Phase 5 (retopo) | Use Hunyuan3D output as-is | Review and manually fix bad edge loops |
| Phase 6 (textures) | Flat grey skin, no mask maps yet | All 5 mask maps painted properly |
| Phase 7 (rigging) | Use Auto-Rig Pro defaults, test basic pose | Full weight paint cleanup at all joints |
| Phase 8 (blend shapes) | Add Fat and Tall, test at 0.5 only | Find exact cap values, test full range |
| Phase 12 (viewer) | One character, swap one cybernetic | Full viewer with all toggles working |

## **This Work Is Not Linear — Expect to Go Backwards**
The pipeline shows phases in order, but real work is not linear. You will finish Phase 7 and discover a UV problem from Phase 5. You will test in Godot and find a rigging issue. This is normal. Here is what to redo when common problems appear:

| Problem You Discover | Go Back To | What to Redo |
|----------------------|-----------|--------------|
| Visible seam in Godot | Phase 5, Step 2 | Rejoin mesh, redefine cut loops, re-split |
| Shoulder collapses in animation | Phase 7, weight paint section | Fix shoulder weight distribution only |
| Blend shapes show seam drift | Phase 8, Step 1 | Rejoin, re-sculpt on unified mesh, re-split |
| UV atlas wrong after split | Phase 5, UV section | Rejoin, repack UV islands, re-split |
| Normal map looks like photo | Phase 6, normal bake section | Check bake type is Normal not Diffuse, rebake |
| Cybernetic drifts from socket | Phase 7, socket bones section | Verify socket bone has zero length and correct parent |
| Animation bones move wrong | Phase 7, export section | Apply pose as rest pose in Auto-Rig Pro, re-export |

## **Fallback Strategies When Tools Fail**
AI tools and automatic processes fail sometimes. Here is what to do when they do:

| Tool / Step That Failed | Fallback Option | Notes |
|------------------------|----------------|-------|
| Tripo AI gives unusable mesh | Try a different concept image with cleaner background and simpler silhouette. Try Meshy.ai as an alternative. | Usually a background or silhouette clarity issue |
| Hunyuan3D gives bad topology | Use Blender's built-in Remesh modifier (Voxel mode, Voxel Size 0.02) as an alternative retopo starting point. | Lower quality but works. Polish manually. |
| Auto-Rig Pro fails to detect markers | Place markers completely manually in the Smart interface. Do not rely on Guess Markers if character proportions are unusual. | Manual placement takes 10 extra minutes but works reliably |
| Voxel bind gives broken weights | Delete the armature modifier, re-bind with Envelope Weights instead of Voxelize. Then manually paint corrections. | Envelope weights are cruder but more predictable |
| Weight painting feels hopeless | Try Blender's Smooth Weights brush to fix blending issues. Use Transfer Weights from a working side to the broken side. | Transfer Weights works across L/R symmetry |
| Normal map bake crashes or corrupts | Skip normal maps for now. Ship without them. Add them in a later pass once everything else works. | Normal maps are optional for body mesh |
| Godot import errors on .glb | Try exporting as FBX instead and import that. Check Blender export settings: apply modifiers, +Y up, include armature. | FBX import in Godot is more forgiving than glTF |


**  PHASE 1**
**  Create Concept Images**
Tools: ComfyUI Cloud     Estimated time: 1-2 hours
Think of this phase like drawing a blueprint. You are telling the AI what your characters should look like. These images will be used in Phase 3 to create the actual 3D shapes.

## **What is ComfyUI?**
ComfyUI is a website where you can run AI image generation. You type in a description and it draws a picture. Think of it like giving instructions to a very fast robot artist.

## **Setting Up ComfyUI**
**Step 1: **Open your web browser and go to: comfy.org/cloud
**Step 2: **Create a free account if you do not have one. Click Sign Up and follow the instructions.
**Step 3: **Once logged in, you need to load the Qwen Image 2.5 workflow. This is a pre-made setup that gives better results for character art.
**a) **Download the workflow file from the link in the workflow guide document
**b) **In ComfyUI, look for a button that says Load or Import Workflow
**c) **Select the file you downloaded
You will see a diagram with connected boxes appear on screen. That is the workflow loaded correctly.

## **Generate the Male Base Character**
You need a full-body image of your male character with arms held at a 45-degree angle (halfway between straight out and pointing down). This specific arm position is called A-pose and is very important for later steps.

**Step 4: **Find the text input box in ComfyUI. It will be labelled something like Prompt or Positive Prompt.
**Step 5: **Type in this exact prompt (you can change the style words but keep the pose description):
full body male human character, A-pose with arms at 45 degrees, solid pure white background, no shadows, sci-fi colony aesthetic, semi-realistic, neutral expression, no weapons, standing straight, full body visible from head to feet
The background MUST be white or solid colour. If the background has details, the next tool cannot separate the body parts correctly.
**Step 6: **Find the Generate or Run button and click it. Wait for the image to appear. This takes 30-60 seconds.
**Step 7: **Look at the result. Ask yourself these questions:
**a) **Are both arms visible and at roughly 45 degrees?
**b) **Is the whole body visible from head to feet?
**c) **Is the background plain white or a single solid colour?
**d) **Does the character look like a full human, not cut off?
If you answered yes to all four questions, this image is good to use.
If the image does not meet all four checks, click Generate again. The AI makes a different image each time. Keep generating until you get a good one.
**Step 8: **Once you have a good image, find the Upscale option and run it. This makes the image larger and clearer.
**Step 9: **Download the final image. Save it in a folder called character_project and name it: concept_base_male.png

## **Generate the Female Base Character**
**Step 10: **Repeat Steps 4 through 9 with this prompt:
full body female human character, A-pose with arms at 45 degrees, solid pure white background, no shadows, sci-fi colony aesthetic, semi-realistic, neutral expression, no weapons, standing straight, full body visible from head to feet
**Step 11: **Save the result as: concept_base_female.png

## **Generate Cybernetic Concepts**
You need one image for each cybernetic body part. These are the mechanical replacements that colonists can have installed. Each one should look like a sci-fi machine version of that body part.

**Step 12: **Generate and save each of these. Use the prompts below. Remember: solid white background, no shadows.

| Save As | Prompt to Use | Notes |
|---------|--------------|-------|
| concept_cyber_arm_l.png | sci-fi cybernetic mechanical left arm replacement, hard surface metal, clean mounting plate at shoulder, white background | Should look like a full arm. Right side will be mirrored in Blender. |
| concept_cyber_leg_l.png | sci-fi cybernetic mechanical left leg replacement, hard surface metal, mounting plate at hip, white background | Full leg from hip down. Right side will be mirrored in Blender. |
| concept_cyber_chest.png | sci-fi cybernetic chest plate replacement, hard surface metal, front view, white background | Front-facing |
| concept_cyber_head.png | sci-fi cybernetic head replacement, visor and sensor array, hard surface metal, white background | Full head replacement |

## **Generate Hair Concepts**
**Step 13: **Generate 3 male hairstyles and 3 female hairstyles. Use prompts like:
male short hair, front and side view, isolated on white background, no face, just the hairstyle
**Step 14: **Save as: concept_hair_m_01.png, concept_hair_m_02.png, concept_hair_m_03.png, concept_hair_f_01.png, concept_hair_f_02.png, concept_hair_f_03.png
Phase 1 complete! You should have 14 images saved in your character_project folder.


**  PHASE 2**
**  Split Body Parts**
Tools: Nano Banana Pro     Estimated time: 30 minutes
Nano Banana Pro looks at your full-body character image and creates separate images for each body part. Think of it like cutting out paper dolls, but the AI does it automatically.
You only need to do this for the base character images, not for the cybernetics or hair (those are already single parts).

## **Why Do We Need to Split?**
The next tool (Tripo AI) works best when given one body part at a time. If you give it the full body, the 3D result is usually messy. Giving it each part separately gives much cleaner results.

## **Splitting the Male Character**
**Step 1: **Open your browser and go to: fal.ai/models/fal-ai/nano-banana-pro
**Step 2: **You will see an Upload or Drop Image area. Click it and select your concept_base_male.png file.
**Step 3: **Find the Resolution setting and set it to 2K.
**Step 4: **Look for a settings area where you can choose which parts to generate. Select: head, torso, arm, leg. You only need ONE arm and ONE leg — not left and right separately. The right side will be created by mirroring in Blender.
Mirroring saves you time and ensures both sides are perfectly symmetrical. Asymmetric details like scars and tattoos are added later as shader overlays.
**Step 5: **Click Generate and wait. It will create 4 separate images.
**Step 6: **Download each image and save them:
- part_male_head.png
- part_male_torso.png
- part_male_arm.png  (will become both left and right arm)
- part_male_leg.png  (will become both left and right leg)
Each saved image should show just one body part on a white background.

## **Splitting the Female Character**
**Step 7: **Repeat Steps 1 through 6 using concept_base_female.png
**Step 8: **Save the results as: part_female_head.png, part_female_torso.png, part_female_arm.png, part_female_leg.png
Phase 2 complete! You should now have 8 part images (4 male + 4 female) plus your original concept images.


**  PHASE 3**
**  Generate 3D Meshes**
Tools: Tripo AI     Estimated time: 2-3 hours
This is where the magic happens. Tripo AI looks at each 2D image and creates a 3D object from it. Think of it like a 3D printer that prints from pictures.
You only generate one arm and one leg per character — the right side is created by mirroring in Blender. Similarly, only the left cybernetic arm and leg are generated. This reduces generations from 24 down to 16.

## **Setting Up Tripo AI**
**Step 1: **Go to tripo3d.ai and create a free account.
**Step 2: **Log in. You will see a dashboard with an Upload or Create button.

## **The Right Settings (Use These Every Time)**
These settings are important. Wrong settings = bad 3D meshes. Check them for every single generation.

- Quality: Ultra
- Mesh Type: Triangle
- UV: Auto

## **Generating Each Chunk**
You will repeat this process 16 times, once for each part image. Here is the process for one part:

**Step 3: **Click the Upload or Create button.
**Step 4: **Upload your part image (for example: part_male_head.png).
**Step 5: **Set the three settings: Ultra quality, Triangle mesh, Auto UV.
**Step 6: **Click Generate and wait. This takes 1-3 minutes per mesh.
**Step 7: **When finished, click Export and choose FBX format.
**Step 8: **Save the file with the correct name (see table below).

| Input Image | Save Export As | Notes |
|-------------|---------------|-------|
| part_male_head.png | raw_male_head.fbx | Male base |
| part_male_torso.png | raw_male_torso.fbx | Male base |
| part_male_arm.png | raw_male_arm.fbx | Male base — mirrored to both sides in Blender |
| part_male_leg.png | raw_male_leg.fbx | Male base — mirrored to both sides in Blender |
| part_female_head.png | raw_female_head.fbx | Female base |
| part_female_torso.png | raw_female_torso.fbx | Female base |
| part_female_arm.png | raw_female_arm.fbx | Female base — mirrored |
| part_female_leg.png | raw_female_leg.fbx | Female base — mirrored |
| concept_cyber_arm_l.png | raw_cyber_arm.fbx | Cybernetic arm — mirrored to L and R in Blender |
| concept_cyber_leg_l.png | raw_cyber_leg.fbx | Cybernetic leg — mirrored to L and R in Blender |
| concept_cyber_chest.png | raw_cyber_chest.fbx | Not mirrored — single piece |
| concept_cyber_head.png | raw_cyber_head.fbx | Not mirrored — single piece |
| concept_hair_m_01.png through 03 | raw_hair_m_01.fbx through 03 | 3 male hairstyles |
| concept_hair_f_01.png through 03 | raw_hair_f_01.fbx through 03 | 3 female hairstyles |

Phase 3 complete! You should have 16 .fbx files in your character_project folder.


**  PHASE 4**
**  Assemble and Clean Up in Blender**
Tools: Blender     Estimated time: 2-4 hours
Now you open Blender and put the character together like a puzzle. You will import all the body part meshes, position them correctly to form a complete body, and fix any obvious problems.

## **Opening Blender for the First Time**
When you open Blender, you see a 3D viewport in the middle (the big grey area), a toolbar on the left, properties on the right, and an outliner in the top-right corner. The outliner shows a list of everything in your scene.
**Step 1: **Open Blender. You will see a default scene with a cube, a camera, and a light.
**Step 2: **Delete everything in the default scene: press A to select all objects, then press Delete (or X), then click Delete in the popup.
The 3D viewport should now be completely empty.

## **Importing the Male Body Parts**
**Step 3: **Import the 4 male meshes: go to File > Import > FBX, one at a time.
**a) **raw_male_head.fbx
**b) **raw_male_torso.fbx
**c) **raw_male_arm.fbx
**d) **raw_male_leg.fbx
**Step 4: **You will see each mesh appear in the 3D viewport. They might look like blobs at first — that is normal.
You should see 4 separate objects in your outliner panel (top right).

## **Positioning the Parts**
Move each part into position to form a complete human body. You only have one arm and one leg at this point — you will mirror them in the next step.

Press numpad 1 to look at the character from the front. Press numpad 3 to look from the side. Press numpad 7 to look from the top.
**Step 5: **Click on one object in the outliner to select it. The selected object will have an orange outline.
**Step 6: **Press G to grab/move. Press G then X to move left/right only. Press G then Z to move up/down only.
**Step 7: **Arrange the 4 parts: torso in the middle, head on top, arm on the LEFT side, leg on the LEFT side.
Place the arm and leg on the LEFT side only. The Mirror modifier will create the right side automatically.

## **Mirroring Arms and Legs**
Instead of importing separate left and right meshes, you use Blender's Mirror modifier to create a perfect copy on the opposite side. This guarantees both sides are identical and saves you half the work.

**Step 8: **Click on the arm mesh to select it.
**Step 9: **In the Properties panel on the right, click the blue wrench icon (Modifiers).
**Step 10: **Click Add Modifier > Mirror.
**Step 11: **In the Mirror modifier settings, make sure X Axis is ticked. You should immediately see a mirrored copy appear on the right side of the character.
**Step 12: **Check that the mirror axis is in the right place. The character should be symmetrical — left and right arms should look like a reflection of each other.
If the mirrored copy appears in the wrong place, the object's origin point might be off-centre. Press Ctrl+A > All Transforms first, then try the Mirror modifier again.
**Step 13: **Do NOT apply the Mirror modifier yet. Leave it active for now.
**Step 14: **Repeat steps 8-13 for the leg mesh.
You now have a complete character silhouette with mirrored arms and legs. The Outliner still shows 4 objects, but you can see all 6 chunks represented.

## **Closing Gaps Between Parts**
The parts may have small gaps where they meet (neck, shoulders, hips). Close these so the character looks connected.

**Step 15: **Click on the torso to select it. Press Tab to enter Edit Mode.
**Step 16: **In Edit Mode, click any vertices near a gap and press G to nudge them closed.
You do not need a perfect join here. The join-then-split process in Phase 5 will handle precise seam matching. Just close any obvious large gaps.
**Step 17: **Press Tab to return to Object Mode.

## **Apply the Mirror Modifier**
Now that the character is positioned correctly, apply the Mirror modifier to bake the right-side geometry in.

**Step 18: **Click the arm mesh to select it.
**Step 19: **In the Modifiers panel (blue wrench icon), click Apply next to the Mirror modifier.
**Step 20: **The arm mesh now contains both left and right sides as real geometry.
**Step 21: **Repeat for the leg mesh.
After applying Mirror, both arms share the same UV space. This is intentional — the base skin texture will be identical on both sides. Asymmetric details like scars and tattoos are added as overlay textures at runtime via the shader.

## **Freezing Transforms**
Reset each object's position data before the next step.

**Step 22: **Press A to select all 4 objects.
**Step 23: **Press Ctrl+A and choose All Transforms.
Position/rotation/scale numbers reset to defaults. This is correct.

## **Rough Polycount Reduction**
The AI-generated meshes have too many polygons. Reduce them before uploading to Hunyuan3D.

**Step 24: **Click on one mesh to select it.
**Step 25: **Modifiers panel (blue wrench) > Add Modifier > Decimate.
**Step 26: **Start with Ratio 0.3. If the shape still looks correct, click Apply.
**Step 27: **If the shape looks broken, increase ratio to 0.5 and try again.
**Step 28: **Repeat for all 4 meshes.
**Step 29: **Export each mesh as FBX: File > Export > FBX. Save as: raw_male_head_decimated.fbx, raw_male_torso_decimated.fbx, raw_male_arm_decimated.fbx, raw_male_leg_decimated.fbx
Phase 4 complete! Character assembled with mirrored limbs and polygon count reduced. Ready for retopology.


**  PHASE 5**
**  Retopology and UV Mapping**
Tools: Hunyuan3D + Blender     Estimated time: 3-5 hours
Retopology means rebuilding the mesh surface with clean, evenly-spaced polygons. The AI mesh is messy. Hunyuan3D creates a clean version. Then in Blender you set up the UV map, which is like unfolding the 3D surface into a flat image so textures can be painted onto it.

## **What is Retopology?**
Imagine wrapping a crumpled piece of tin foil around a ball. That is what the AI mesh looks like. Retopology is like replacing that crumpled foil with a perfectly smooth piece of fabric that fits the same shape. The result animates much better.

## **Retopology via Hunyuan3D**
**Step 1: **Go to 3d.hunyuan.tencent.com in your browser.
**Step 2: **Upload raw_male_head_decimated.fbx.
**Step 3: **Choose face count:
**a) **Head and Torso: choose High
**b) **Arms and Legs: choose Standard
**Step 4: **Enable Intelligent UV Unfolding (this automatically creates a UV map).
**Step 5: **Click Generate and wait.
**Step 6: **Download the result and save as: retopo_male_head.fbx
**Step 7: **Repeat for all 6 male chunks, all 6 female chunks, and all 6 cybernetic pieces.
Hair meshes do NOT need Hunyuan3D retopology. You will build the hair cards manually in Blender in Phase 11.
Each retopologised mesh should look smoother and cleaner than the original, with evenly-spaced polygons.

## **Import Retopologised Meshes into Blender**
**Step 8: **Open Blender. Delete the default scene (press A, then Delete).
**Step 9: **Import all 6 retopologised male chunks: File > Import > FBX, one at a time.
**Step 10: **Position them back into a complete character shape (same as Phase 4).

## **Check Total Polygon Count**
**Step 11: **Click on one chunk to select it.
**Step 12: **Look at the bottom of the Blender window. You will see statistics including a triangle count (shown as Tris).
**Step 13: **Add up the tri counts for all 6 chunks. The total should be between 5,000 and 10,000 tris.
If the total is over 10,000, select the largest chunks and add a Decimate modifier with ratio 0.8. Apply it and recheck the count.

## **Setting Up the Shared UV Atlas**
This is one of the most important steps. All 6 body chunks must share one single texture image. To make this work, each chunk's UV map needs to be placed in a different area of the same texture space. Think of it like fitting six small pictures into one large picture frame without overlapping.

The UV Editor is a separate window in Blender. You can open it by going to the top menu, clicking the + icon next to the layout tabs, and choosing UV Editing from the dropdown.
**Step 14: **In Blender, click on the UV Editing tab at the top of the screen (or set it up as described in the tip above).
**Step 15: **Click on the Head chunk in the viewport to select it.
**Step 16: **Press Tab to enter Edit Mode. Press A to select all vertices.
**Step 17: **In the UV Editor on the left, you should see the UV map for the head. It will look like a flat diagram of the mesh surface.
**Step 18: **You need to scale and move the head UV islands to fit in the TOP-LEFT quarter of the UV space. In the UV Editor: press A to select all UV islands, press S to scale them down, then press G to move them to the top-left.
**Step 19: **Press Tab to exit Edit Mode.
**Step 20: **Repeat for each chunk, placing them in different areas:
Because arms and legs were created with the Mirror modifier, both the left and right sides already share the same UV space. This is correct and intentional. You will place them as one set of UV islands, not two.

| Chunk | Where to Place UV Islands | Notes |
|-------|--------------------------|-------|
| Head | Top-left quarter | About 1/4 of total space |
| Torso | Top-right quarter | About 1/4 of total space |
| Arm (L+R mirrored) | Bottom-left half | Both sides share this region. Texture is identical on both arms. |
| Leg (L+R mirrored) | Bottom-right half | Both sides share this region. Texture is identical on both legs. |

**Step 21: **Take a screenshot of the UV Editor showing all UV islands in their positions. Save it as: uv_layout_male.png. You will need this as a reference for painting textures later.
Check that NO UV islands from different chunks overlap each other. If any overlap, the textures will be wrong. Select the overlapping island and move it to fix it.

## **Eliminating Seams — The Right Way**
This is the most important technique in the entire pipeline. Instead of trying to manually match vertex positions between separate chunks after the fact (which is slow, error-prone, and breaks under animation), we use a much better approach: join all chunks into one mesh, define clean cut lines, and then split them apart. Because the split edges come from the same mesh, they are already perfectly matched — by definition.

Do NOT try to match seams by manually typing X, Y, Z coordinates for individual vertices. This approach does not scale and animation will expose any mistakes. Follow the join-then-split method below instead.

**Step 1 — Join All Chunks Into One Mesh**
**Step 22: **In Blender, make sure all 6 retopologised chunks are in your scene and positioned correctly as a complete character.
**Step 23: **Press A to select all 6 chunks.
**Step 24: **Press Ctrl+J to join them into a single mesh object. You now have one unified character mesh.
The Outliner now shows one mesh object instead of six. The character looks identical in the viewport.

**Step 2 — Define Clean Cut Lines**
Now you will select the edge loops exactly where you want the chunks to split. These edge loops become the seams. Because they are part of one mesh, both sides of every seam are already perfectly aligned.

**Step 25: **Press Tab to enter Edit Mode on the joined mesh.
**Step 26: **Switch to Edge Select mode by pressing the number 2 on your keyboard (not numpad).
**Step 27: **Hold Alt and click on an edge at the shoulder where the arm should separate from the torso. This selects the entire edge loop around the shoulder joint.
If Alt+click selects too many or too few edges, you can manually add to the selection by holding Shift and clicking additional edges.
**Step 28: **Select the edge loops at all 5 split points:
- Neck (where head separates from torso)
- Left shoulder (where left arm separates from torso)
- Right shoulder (where right arm separates from torso)
- Left hip (where left leg separates from torso)
- Right hip (where right leg separates from torso)
Make sure your selected edge loops go all the way around the body at each split point with no gaps. You can see selected edges highlighted in orange.

**Step 3 — Mark the Seams**
**Step 29: **With the split edge loops selected, go to Edge menu at the top > Mark Seam. The selected edges will turn red. This marks them for UV splitting later.

**Step 4 — Separate Into Chunks**
**Step 30: **Switch to Face Select mode by pressing 3 on your keyboard.
**Step 31: **Click on a face on the head to select it. Then press Ctrl+L to select all connected faces (the entire head).
**Step 32: **Press P (separate) and choose Selection. The head is now a separate object again.
**Step 33: **Rename it: double-click on it in the Outliner and type body_male_head.
**Step 34: **Repeat steps 31-33 for each remaining region:
- Click a torso face, Ctrl+L to select all, P > Selection, rename body_male_torso
- Click a left arm face, Ctrl+L, P > Selection, rename body_male_arm_l
- Click a right arm face, Ctrl+L, P > Selection, rename body_male_arm_r
- Click a left leg face, Ctrl+L, P > Selection, rename body_male_leg_l
- Click a right leg face, Ctrl+L, P > Selection, rename body_male_leg_r
You now have 6 separate objects again, but their boundary edges are perfectly matched because they all came from the same mesh. There will be zero seam gaps.
Double-check the Outliner shows exactly 6 objects with the correct names before moving on. If any regions got accidentally combined, press Ctrl+Z to undo and repeat.

**Step 5 — Apply This Approach to Blend Shapes Too**
When you add blend shapes in Phase 8, use the same logic: join all chunks, sculpt the Fat and Tall shapes on the unified mesh, then split apart again. This guarantees blend shapes are consistent across all chunks with zero drift at seam boundaries.
Write this down somewhere: join first, sculpt or split, then separate. This one rule eliminates the two biggest risk areas in the entire pipeline.
Phase 5 complete! You have clean retopologised meshes with perfectly matched seams and a shared UV atlas.


**  PHASE 6**
**  Textures and Mask Maps**
Tools: Blender     Estimated time: 3-5 hours
Now you paint the textures. There are two types: the base colour (what the skin looks like) and mask maps (invisible guides that tell the shaders where to do special effects).

## **The Most Important Rule About Textures**
Do NOT bake lighting, shadows, or ambient occlusion into your base colour texture. The texture should be flat and even, like a colouring book page with no shading. Shading is added at runtime by the game engine.
Normal maps are the ONE exception. Normal maps record surface bumps and angles, not lighting. They are allowed and useful.

## **What Each Map Does**

| Map Name | Colours Used | What It Does |
|----------|-------------|--------------|
| Base skin texture | Flat skin colours | The basic colour of the skin. No shading, no highlights. |
| Skin region mask | White and black | White = skin. Black = not skin. Tells the shader where skin ends. |
| Attachment zone mask | Grey gradient | Where cybernetics attach. Fades from white at the socket to black away from it. |
| Variation mask | Grey areas | Where scars and tattoos can appear on the skin. |
| Resonance crack mask | Dark fracture lines | Stress fracture patterns. For characters with resonance powers. |
| Normal map | Blue-purple image | Records surface bumps. Baked from the high-poly mesh. Allowed. |

## **Setting Up for Texture Painting in Blender**
**Step 1: **In Blender, switch to the Texture Paint workspace by clicking the Texture Paint tab at the top.
**Step 2: **Select the torso chunk (or any chunk — we will work on all of them).
**Step 3: **In the Properties panel, click the material icon (circle with small circle) to open Material properties.
**Step 4: **Click New to create a new material.
**Step 5: **Name it mat_body_skin.
**Step 6: **Click the yellow dot next to Base Color and choose Image Texture.
**Step 7: **Click New in the image texture settings. Set Width and Height to 2048. Set Color to a mid-tone skin colour. Click OK.
**Step 8: **Name the image: body_base_male
**Step 9: **Assign this SAME material and SAME image to all 6 body chunks. This is important — they must all share one image.
To assign the same material to another chunk: click the other chunk, go to Material Properties, click the dropdown and select the mat_body_skin material you already created.

## **Painting the Base Skin Texture**
**Step 10: **With the torso selected, look at the Texture Paint workspace. On the left you have painting tools. In the centre is the 3D view. On the right is the UV editor showing your image.
**Step 11: **Paint flat skin colour over the skin areas. Do not add shading or highlights — keep it even.
**Step 12: **Paint slightly different flat colours for different skin zones (face area, body, hands/feet can be slightly different tones).
If you want to use Modddif.com to generate a textured reference: export your assembled character as OBJ (File > Export > Wavefront OBJ), upload to modddif.com, generate textures, then use the result ONLY as a colour reference. Do not use it directly — it will have baked shading that needs to be removed.
**Step 13: **When done: Image > Save As, save as body_base_male.png

## **Painting the Mask Maps**
Each mask map uses the same UV layout as the base texture. You will create a new image for each one and paint in greyscale.

**Step 14: **Skin Region Mask: Create a new 2048x2048 image, paint it all WHITE first. Then paint BLACK over any non-skin areas (eye sockets, inside mouth if visible). Save as: body_skin_mask.png
**Step 15: **Attachment Zone Mask: Create a new 2048x2048 image, paint it all BLACK. Then paint WHITE circles at each socket location (both shoulders, both hips, chest, neck). Use a soft brush to create a gradient fading from white in the centre to black at the edges. Save as: body_attachment_mask.png
**Step 16: **Variation Mask: Create a new 2048x2048 image, paint medium grey over the areas where scars could appear (arms, torso, face sides). Leave palms and soles of feet darker. Save as: body_variation_mask.png
**Step 17: **Resonance Crack Mask: Create a new 2048x2048 image, paint BLACK everywhere. Then using a thin hard brush, paint DARK GREY branching crack lines across the torso and arms. Think of cracked dry earth or lightning bolt shapes. Save as: body_resonance_mask.png

## **Overlay Textures — Asymmetric Details**
Because the arms and legs use mirrored UVs, the base skin texture is identical on both sides. To add asymmetric details (a scar on only the left arm, a tattoo on only the right shoulder), you use overlay textures. These are separate small images that the shader composites on top of the base skin at runtime.

Think of overlay textures like stickers. The base skin is the character's body. An overlay sticker is placed on top in a specific spot. You can mix and match different stickers to create unique-looking colonists without ever changing the base skin texture.

Overlay textures do NOT need to share the body atlas UV layout. They have their own UV unwrap, designed specifically for placement on one area of the body.

**Step 18: **To create a scar overlay for the left arm: in Blender, select the arm mesh and enter Edit Mode.
**Step 19: **Select only the faces on the LEFT arm (the faces on the left side of the mirror seam).
**Step 20: **Go to UV > Unwrap. This creates a UV map just for the left arm faces.
**Step 21: **Create a new 512x512 image. Paint a scar pattern on it. The UV map you just created tells the shader exactly where on the arm this image appears.
**Step 22: **Save as: overlay_scar_arm_l_01.png
**Step 23: **You can create as many overlays as you want: scars, tattoos, birthmarks, burn marks. Each is a small texture. Mix different overlays per colonist for visual variety.
Overlay textures are used by the runtime shader system. Creating the actual shader that composites overlays is done in Godot, not Blender. This step just produces the texture files.

## **Normal Map Baking (Cybernetics)**
For the cybernetic pieces, we can bake a normal map from the high-poly AI mesh to capture all the surface detail. This makes the low-poly version look much more detailed.

**Step 18: **In Blender, import both the high-poly cybernetic mesh (raw_cyber_arm_l.fbx) AND the retopologised version (retopo_cyber_arm_l.fbx).
**Step 19: **Position them both exactly on top of each other.
**Step 20: **Select the LOW-POLY mesh (retopo version).
**Step 21: **Create a new material with an Image Texture node. Create a new 2048x2048 image. Name it cyber_arm_l_normal. Make sure this node is selected (click it once so it has a white border) but DO NOT connect it to anything.
**Step 22: **Go to Render Properties (camera icon in Properties panel). Change render engine to Cycles.
**Step 23: **Scroll down to find the Bake section. Click on it to expand it.
**Step 24: **Set Bake Type to Normal.
**Step 25: **Turn on Selected to Active.
**Step 26: **Set Extrusion to 0.03.
**Step 27: **Click Bake and wait (this takes 1-5 minutes).
The image in your Image Texture node should now show a blue-purple image with slight colour variations at the edges and panels. This is a correct normal map.
If the baked image looks like a photo with light and shadow instead of blue-purple, the bake settings are wrong. You may have baked a Diffuse map instead of a Normal map. Check step 24.
**Step 28: **Save the normal map: Image > Save As, save as cyber_arm_l_normal.png
**Step 29: **Repeat for all 6 cybernetic pieces.
Phase 6 complete! You have all texture maps ready for use.


**  PHASE 7**
**  Rigging (Adding Bones)**
Tools: Blender + Auto-Rig Pro     Estimated time: 4-6 hours
Rigging means adding a skeleton inside the character so it can move and animate. Think of it like putting the wire frame inside a puppet. The bones tell each part of the mesh how to move.

## **Installing Auto-Rig Pro**
**Step 1: **Purchase Auto-Rig Pro from blendermarket.com/products/auto-rig-pro. You will download a .zip file.
**Step 2: **In Blender: Edit > Preferences > Add-ons > Install.
**Step 3: **Select the .zip file you downloaded.
**Step 4: **Find Auto-Rig Pro in the add-on list and tick the checkbox next to it to enable it.
**Step 5: **Close Preferences. You should now see an Auto-Rig Pro panel in the right sidebar (press N if you do not see the sidebar).
You should see an Auto-Rig Pro section in the N panel sidebar on the right of the viewport.

## **Preparing the Character**
**Step 6: **Make sure all 6 body chunks are in your scene and positioned correctly as a complete character in A-pose.
**Step 7: **Select all 6 chunks by pressing A.
**Step 8: **Press Ctrl+A > All Transforms to freeze the transforms.

## **Running Auto-Rig Pro Smart**
**Step 9: **In the Auto-Rig Pro panel (N sidebar), click Smart.
**Step 10: **Click Get Selected Objects. Auto-Rig Pro will analyse your meshes.
**Step 11: **Click Guess Markers. Auto-Rig Pro will place coloured markers on the character showing where it thinks the joints are.
**Step 12: **Check each marker position. You will see markers for: head top, chin, left and right shoulders, left and right wrists, left and right hips, left and right ankles.
**Step 13: **If any marker is in the wrong place, click and drag it to the correct position. For example, if the wrist marker is halfway up the forearm, drag it down to the actual wrist.
Take your time checking markers. Wrong markers = wrong animation. The most common mistakes are: wrist markers too high, ankle markers too high, hip markers too far apart.
**Step 14: **Once all markers look correct, click Go. Auto-Rig Pro will build the rig.
You should see a new armature (skeleton) appear inside the character. It will be visible as orange/yellow lines in the viewport.

## **Binding the Mesh to the Skeleton**
**Step 15: **In the Auto-Rig Pro panel, click Skin.
**Step 16: **Click Voxelize. Wait while Blender calculates how each part of the mesh should follow each bone.
**Step 17: **Click Bind.
Nothing visible changes immediately. The mesh is now bound to the skeleton.

## **Testing the Rig**
**Step 18: **Click on the armature (the skeleton, shown as lines).
**Step 19: **Press Tab to enter Edit Mode... actually for testing: change from Object Mode to Pose Mode using the dropdown at the top-left of the viewport.
**Step 20: **Click on one of the arm bones. Press G to move it, or R to rotate it.
**Step 21: **Watch what happens to the mesh. The arm should follow the bone movement.
**Step 22: **Check for problems:
**a) **Does the shoulder area pinch or collapse? This needs weight paint fixing.
**b) **Does part of the torso move when it should not? Weight paint fixing needed.
**c) **Does the arm move cleanly from shoulder to wrist? Good!
**Step 23: **Press Ctrl+Z multiple times to undo all the test movements and return the pose to rest position.

## **Fixing Weight Paint Problems**
Weight paint controls which bones influence which parts of the mesh, and by how much. Red areas are strongly influenced by a bone, blue areas are not influenced at all.

**Step 24: **If you see deformation problems: click on the mesh chunk that has problems.
**Step 25: **Change from Object Mode to Weight Paint mode using the dropdown.
**Step 26: **Click on a bone in the Properties panel > Vertex Groups to see which bone you are painting for.
**Step 27: **Paint red (weight = 1.0) on areas that should follow this bone completely.
**Step 28: **Paint blue (weight = 0.0) on areas that should NOT follow this bone.
For arms: the shoulder bone should have weight 1.0 at the top of the upper arm, fading to 0.0 halfway down. The elbow bone takes over from there. This creates smooth bending.
**Step 29: **After fixing: go back to Pose Mode and test again.

## **Limiting Bone Influences**
**Step 30: **Select all mesh chunks (press A in Object Mode).
**Step 31: **Go to Object Data Properties > Vertex Groups.
**Step 32: **Click the dropdown arrow next to Vertex Groups and find Limit Total.
**Step 33: **Set the limit to 4. Click OK.
This makes sure no vertex is controlled by more than 4 bones, which is required for game engines to work correctly.

## **Adding Socket Bones**
Socket bones are special bones where cybernetics and equipment will attach in the game. They do not move the mesh — they are just attachment points.

**Step 34: **Click on the armature and press Tab to enter Edit Mode.
**Step 35: **To add a socket bone: hold Shift and click on the shoulder bone to select it. Then press E to extrude a new bone from it.
**Step 36: **Move the new bone to sit at the shoulder attachment point (where the cybernetic arm would connect). Click to confirm.
**Step 37: **With the new bone selected, look at the Bone Properties panel on the right. Change the name to: upperarm_l_socket
**Step 38: **In Bone Properties, find the Deform checkbox and UNTICK it. Socket bones should not deform the mesh.
**Step 39: **Set the bone's tail position to be the same as its head position (zero length bone). You can do this by typing the same coordinates for both Head and Tail in the Bone Properties.
**Step 40: **Add all 6 socket bones using the same process:

| Socket Bone Name | Parent (Extrude From) | Position |
|-----------------|----------------------|----------|
| upperarm_l_socket | Left upper arm bone | Left shoulder attachment point |
| upperarm_r_socket | Right upper arm bone | Right shoulder attachment point |
| thigh_l_socket | Left thigh bone | Left hip attachment point |
| thigh_r_socket | Right thigh bone | Right hip attachment point |
| spine_03_socket | Upper spine/chest bone | Centre chest attachment point |
| neck_01_socket | Neck bone | Base of skull / head attachment |

**Step 41: **Press Tab to exit Edit Mode.

## **Exporting for Godot**
**Step 42: **Select all mesh chunks AND the armature (press A).
**Step 43: **Go to File > Export > glTF 2.0 (.glb/.gltf).
**Step 44: **In the export options panel on the right:
**a) **Make sure Include > Selected Objects is ticked
**b) **Transform > +Y Up should be ticked
**c) **Geometry > Apply Modifiers should be ticked
**d) **Animation > Shape Keys (Morph Targets) should be ticked
**Step 45: **Click Export glTF 2.0 and save as: body_male_rigged.glb
Phase 7 complete! You have a rigged character exported as a .glb file ready for Godot.


**  PHASE 8**
**  Blend Shapes (Body Variation)**
Tools: Blender     Estimated time: 2-3 hours
Blend shapes (also called shape keys) let you morph the character between different body types using sliders. You will create two: Fat and Tall. These will be used to randomly generate different-looking colonists.

## **What is a Blend Shape?**
Imagine a clay model. A blend shape records a different position for every point of clay. When you turn a slider from 0 to 1, every point moves from its original position to its blend shape position. At 0.5, every point is halfway between.

## **The Most Important Rule for Blend Shapes**
Do NOT add blend shapes to each chunk separately. If you sculpt Fat and Tall on each chunk individually, the seams will drift and pop when you move the sliders. Instead, use the same join-then-split approach from Phase 5. Join all chunks, sculpt the blend shapes on the unified mesh, then split apart again. This guarantees perfect consistency across all chunks.

## **Step 1 — Join All Chunks**
**Step 1: **Make sure all 6 body chunks are in your scene and positioned correctly.
**Step 2: **Press A to select all chunks.
**Step 3: **Press Ctrl+J to join them into one single mesh.
You now have one unified mesh. The Outliner shows one object.

## **Step 2 — Add the Basis Shape Key**
**Step 4: **Click on the joined mesh to select it.
**Step 5: **In the Properties panel on the right, click the green triangle icon (Object Data Properties).
**Step 6: **Scroll down to find Shape Keys. Click the + button. A shape key named Basis appears. This records the default/normal shape and cannot be edited.

## **Step 3 — Add the Fat Shape Key**
**Step 7: **Click + again to add a second shape key. Rename it to: Fat
**Step 8: **Make sure Fat is selected/highlighted in the list.
**Step 9: **Press Tab to enter Edit Mode. The shape key is now recording your changes.
**Step 10: **Press A to select all vertices.
**Step 11: **Enable Proportional Editing: press O (the letter O). A circle icon appears in the header. This makes changes fade out gradually rather than affecting only the exact vertices you move.
**Step 12: **Press S then X to scale on the X axis (left/right). Move your mouse slightly outward to make the body wider. Click to confirm.
**Step 13: **Press S then Y slightly to add depth (front/back width).
**Step 14: **The widening should be most noticeable at: waist, hips, upper arms, thighs.
**Step 15: **Press Tab to exit Edit Mode.
**Step 16: **Test by moving the Fat slider from 0 to 1. The whole body should get wider together, with no seam gaps appearing.
When Fat = 1.0, the character looks noticeably heavier AND the seams stay perfectly invisible.
**Step 17: **Set Fat slider back to 0.

## **Step 4 — Add the Tall Shape Key**
**Step 18: **Click + to add another shape key. Rename it to: Tall
**Step 19: **With Tall selected, press Tab to enter Edit Mode.
**Step 20: **Press A to select all. Press S then Z to scale on the Z (up/down) axis. Move mouse slightly upward. Click to confirm.
The whole body should get taller together. Do not try to stretch only the legs or only the torso — scaling the entire unified mesh keeps everything proportional.
**Step 21: **Press Tab to exit. Test the Tall slider. The character should get taller at 1.0 with no seam popping.
**Step 22: **Set Tall slider back to 0.

## **Step 5 — Split Back Into Chunks**
**Step 23: **Now split the unified mesh back into 6 chunks using the same method as Phase 5, Steps 30-34:
**a) **Press Tab to enter Edit Mode, switch to Face Select (press 3)
**b) **Click a head face, press Ctrl+L to select all connected, press P > Selection
**c) **Repeat for torso, left arm, right arm, left leg, right leg
**d) **Rename each chunk correctly in the Outliner
You now have 6 separate chunks again, each with identical Fat and Tall shape keys that are perfectly consistent with each other. Moving Fat to 0.8 on any chunk will look exactly the same as on any other chunk.

## **Finding the Safe Slider Cap Values**
**Step 22: **Set both Fat and Tall sliders to 1.0 at the same time on all chunks.
**Step 23: **Look very carefully at the result. Do you see any pinching, collapsing, or weird distortion?
**Step 24: **If yes: slowly reduce both sliders until the distortion goes away. Write down this value.
**Step 25: **For example: if distortion starts at 0.9, your cap value is 0.8 (a little safety margin).
**Step 26: **Write down the cap values you found: Fat cap = ___, Tall cap = ___. You will use these in Godot later.

## **Re-Export with Shape Keys**
**Step 27: **Select all chunks and the armature (press A).
**Step 28: **File > Export > glTF 2.0.
**Step 29: **Make sure Shape Keys (Morph Targets) is ticked in export options.
**Step 30: **Save as: body_male_final.glb
Phase 8 complete! Your character has working blend shapes. Write down your cap values somewhere safe.


**  PHASE 9**
**  Import into Godot 4 and Validate**
Tools: Godot 4     Estimated time: 2-3 hours
Now you bring the character into the game engine. This phase also involves setting up bone mapping so that any standard animation can work on your character.

## **Setting Up Your Godot Project**
**Step 1: **Open Godot 4. Create a new project if you do not have one yet: click New Project, choose a folder, click Create & Edit.
**Step 2: **In the FileSystem panel (bottom left), create a folder structure: right-click on res:// and create these folders:
**a) **assets/characters
**b) **assets/animations
**c) **assets/cybernetics
**Step 3: **Copy your body_male_final.glb file into the assets/characters folder on your computer (not in Godot — just in the actual folder on your hard drive).
**Step 4: **Godot will automatically detect the new file. You should see it appear in the FileSystem panel.

## **Configuring the Import Settings**
**Step 5: **Click on body_male_final.glb in the FileSystem panel to select it.
**Step 6: **Look at the Import panel (it might be a tab near the FileSystem panel, or go to Scene > Import).
**Step 7: **Find the setting: Animation > Import Rest As RESET. Turn this ON.
**Step 8: **Click Reimport at the bottom of the Import panel.
The file should import without any red error messages in the Output panel at the bottom of the screen.

## **Setting Up Bone Mapping**
This is how you tell Godot which bone in your rig corresponds to which standard humanoid bone. You only need to do this once and can reuse the result for all characters.

**Step 9: **In the FileSystem panel, double-click on body_male_final.glb to open it as a scene.
**Step 10: **In the Scene panel (top left), you will see a tree of nodes. Find and click on the node called Skeleton3D. It might be nested inside other nodes.
**Step 11: **Look at the Inspector panel on the right. Find a property called Bone Map. Click on it and select New BoneMap from the dropdown.
**Step 12: **After creating the BoneMap, click on it in the Inspector to expand it.
**Step 13: **Find the Profile setting and set it to: SkeletonProfileHumanoid
**Step 14: **Godot will now show a list of standard humanoid bones with dropdown menus next to each one. Some will auto-detect (shown in green). Some will be blank or orange (need manual mapping).
**Step 15: **For any blank slots, click the dropdown and find the matching bone from your Auto-Rig Pro skeleton:

| Godot Slot Name | Select This Bone | Notes |
|----------------|-----------------|-------|
| Hips | c_root_master.x | The main root/hip bone |
| Spine | spine_01.x | Lower spine |
| Chest | spine_02.x | |
| UpperChest | spine_03.x | |
| Neck | neck.x | |
| Head | head.x | |
| LeftUpperArm | arm_stretch.l | |
| LeftLowerArm | forearm_stretch.l | |
| LeftHand | hand.l | |
| LeftUpperLeg | thigh_stretch.l | |
| LeftLowerLeg | leg_stretch.l | |
| LeftFoot | foot.l | |

For Right side bones, everything is the same but replace .l with .r. For example: arm_stretch.r for RightUpperArm.
**Step 16: **Once all slots show green, find the Save button in the Inspector and save this BoneMap as a resource file: click the save icon next to the BoneMap property and save to assets/characters/bone_map_humanoid.tres
All bone slots should show green. If any show red, that bone has no match — check your Auto-Rig Pro export included all bones.

## **Setting Up the Test Scene**
**Step 17: **Go to Scene > New Scene.
**Step 18: **Click Other Node and add a Node3D as the root. Name it TestScene.
**Step 19: **Click the + button to add a child node. Add a Camera3D. Position it in front of where the character will stand.
**Step 20: **Drag body_male_final.glb from the FileSystem panel into the scene viewport. It will appear as a character in the scene.
**Step 21: **Press F5 (or click the play button) to run the scene. You should see your character in the game view.
You should see the character standing in the game viewport. All 6 mesh chunks visible and correctly positioned.

## **Testing Animations**
**Step 22: **Go to mixamo.com, create a free Adobe account if needed.
**Step 23: **Upload your body_male_final.glb file to Mixamo. It will ask you to place markers for hips, wrists, elbows, knees, and chin. Place them correctly.
**Step 24: **Search for the Idle animation. Click on it to preview. Enable In Place.
**Step 25: **Download: choose FBX, With Skin, 30 FPS.
**Step 26: **Save as: anim_idle.fbx. Copy it into your Godot assets/animations folder.
**Step 27: **In Godot, click on anim_idle.fbx in FileSystem. In the Import panel, set Animation > Import As: Animation.
**Step 28: **Find the Retarget option in the import settings. Set the BoneMap to your bone_map_humanoid.tres file.
**Step 29: **Click Reimport.
**Step 30: **In your test scene, add an AnimationPlayer node as a child of your character.
**Step 31: **Drag the imported idle animation into the AnimationPlayer.
**Step 32: **Press play and watch the character animate.
The character should play the idle animation with all 6 chunks deforming correctly. Arms and legs should move naturally.
If bones move in the wrong direction or twist unnaturally, the rest pose may have pre-rotations. You need to go back to Blender, select the armature, go to Auto-Rig Pro panel, and click Apply Pose as Rest Pose, then re-export.

## **Testing Blend Shapes**
**Step 33: **In your Godot scene, click on one of the MeshInstance3D nodes (a body chunk).
**Step 34: **In the Inspector, find Blend Shapes. You should see Fat and Tall listed with sliders.
**Step 35: **Move the Fat slider to your cap value (for example 0.8). The mesh should get wider.
**Step 36: **Move the Tall slider to your cap value. The mesh should get taller.
**Step 37: **Repeat for all 6 mesh chunks.
All 6 chunks should blend correctly with no distortion within the cap values.

## **Testing Socket Bones**
**Step 38: **In your test scene, click on the Skeleton3D node.
**Step 39: **Add a child node: BoneAttachment3D.
**Step 40: **In the Inspector for BoneAttachment3D, set Bone Name to: upperarm_l_socket
**Step 41: **Add a child MeshInstance3D to the BoneAttachment3D. Set its mesh to a simple BoxMesh. This is your placeholder to confirm the socket works.
**Step 42: **Run the scene with the idle animation playing.
**Step 43: **Watch the small box. It should stay attached to the left shoulder and move with the animation.
The box follows the shoulder throughout the animation. Socket bone is working.
**Step 44: **Repeat this test for all 6 socket bones.
**Step 45: **Remove the test boxes when done.

## **Stress Test — 10 Characters at Once**
Before moving on, run one final stress test. This catches seam popping and deformation problems that only show up when many characters are running at the same time — exactly what your colony sim needs.

**Step 46: **In your test scene, duplicate your character 9 times so you have 10 total: select the character, press Shift+D, click to place, repeat.
**Step 47: **For each character, set different random Fat and Tall values within your cap range. For example: character 1 gets Fat=0.3 Tall=0.6, character 2 gets Fat=0.7 Tall=0.2, etc.
**Step 48: **Make sure all 10 characters are playing the idle animation.
**Step 49: **Slowly zoom the camera in close to one character, then zoom out to see all 10. Look carefully for:
**a) **Visible seam lines between chunks on any character
**b) **Mesh parts separating or floating away from each other
**c) **Weird stretching or collapsing at shoulders, hips, or neck
**d) **Performance — does Godot slow down with 10 characters animating?
All 10 characters animate smoothly with no visible seams, no deformation problems, and acceptable performance. You are ready to build the full set of deliverables.
If you see seam problems on ANY character: go back to Phase 5 and check your join-then-split process. Do not move on until all 10 characters pass this test.
Phase 9 complete! Your character is fully working in Godot 4. Congratulations — the hardest part is done!


**  PHASE 10**
**  Cybernetic Pieces**
Tools: Blender + Godot 4     Estimated time: 4-6 hours
Now you process each of the 6 cybernetic pieces using a simplified version of the base mesh pipeline. Hard surface pieces are faster because they do not need blend shapes or complex weight painting.

## **Process for Each Cybernetic Piece**
Repeat all of these steps for each piece: Left Arm, Right Arm, Left Leg, Right Leg, Chest, Head.

**Step 1: **Open Blender. Delete the default scene.
**Step 2: **Import the raw cybernetic FBX (for example: raw_cyber_arm_l.fbx).
**Step 3: **Add a Decimate modifier. Set ratio to 0.3. Check the shape still looks correct. Apply the modifier.
**Step 4: **Upload the decimated mesh to Hunyuan3D. Choose Hard Surface and Standard quality. Enable UV Unfolding. Download and import the retopologised result.
**Step 5: **Target poly count: 500 to 1,500 triangles per piece. Add more decimation if needed.
**Step 6: **Create a material and flat colour texture for this piece. Hard metal grey tones, no baked lighting.
**Step 7: **Bake a normal map from the high-poly raw mesh to the retopologised mesh (same process as Phase 6, steps 18-29).
**Step 8: **Position the cybernetic piece so it lines up with where it would attach to the character body. The attachment end should extend 1-1.5cm into where the body chunk would be.
**Step 9: **Import a copy of your body_male_final.glb skeleton. You need the armature to rig the cybernetic piece.
**a) **File > Append (not Import) > navigate to body_male_final.glb > Object > select the Armature
**Step 10: **Select the cybernetic mesh. Then Shift-click the armature to also select it. Press Ctrl+P > With Automatic Weights to bind the mesh to the skeleton.
**Step 11: **Go to Weight Paint mode. For an arm cybernetic, paint the ENTIRE mesh with weight = 1.0 for the upperarm_l bone. Zero for everything else. Hard 100% weight — no blending.
Cybernetics are hard surface, so you want hard 100% weights. One bone = one section of the cybernetic. No smooth transitions needed.
**Step 12: **Export as glTF 2.0. Save as: cyber_arm_l_01.glb
**Step 13: **In Godot: copy the file to assets/cybernetics/. Import it.
**Step 14: **In your test scene: add a BoneAttachment3D to the Skeleton3D, set it to upperarm_l_socket.
**Step 15: **Add a child node importing your cybernetic scene.
**Step 16: **Hide the body_arm_l mesh chunk (click the eye icon next to it in the scene tree).
**Step 17: **Run the idle animation and check:
**a) **Does the cybernetic arm stay attached to the shoulder socket?
**b) **Is there a visible gap between the attachment end and the torso?
**c) **Does it move naturally with the animation?
Cybernetic piece is working if: no visible gap, moves with the body, looks correct in the scene.
**Step 18: **Repeat for all 6 cybernetic pieces.
Phase 10 complete! All 6 cybernetic pieces are working in Godot.


**  PHASE 11**
**  Hair Meshes**
Tools: Blender + Godot 4     Estimated time: 2-3 hours
Hair meshes are flat card shapes that create the illusion of hair volume. Each hairstyle is a different mesh. They attach to the head socket bone and can be swapped out like equipment.

## **What Are Hair Cards?**
Instead of modelling every strand of hair, game artists use flat rectangles (cards) with hair images on them. When you have many cards overlapping at different angles, it looks like a real hairstyle. Think of it like making a 3D bush from flat cardboard cutouts.

## **Building Hair Cards in Blender**
**Step 1: **Open Blender. Delete default scene.
**Step 2: **Look at your concept_hair_m_01.png image for reference — open it on a second monitor or in a viewer.
**Step 3: **Create a flat plane: Shift+A > Mesh > Plane. This is your first hair card.
**Step 4: **Press S to scale it smaller. Position it where hair would start at the top of the head. Rotate it (press R) to angle it the way the hair flows.
**Step 5: **Duplicate the plane (Shift+D) and position the copy to cover more of the hairstyle.
**Step 6: **Add more cards, overlapping slightly, until the overall shape matches the concept image silhouette.
You only need 8-15 cards for a simple colony sim hairstyle. More is not better — keep it simple.
**Step 7: **When the shape looks right, select all cards and press Ctrl+J to join them into one object. Name it equip_hair_m_01.
**Step 8: **UV unwrap the combined object: press Tab for Edit Mode, press A for select all, then UV > Smart UV Project. This automatically creates UV coordinates.

## **Hair Textures**
**Step 9: **Create a new 1024x1024 image in Blender's image editor. Name it hair_m_01_alpha.
**Step 10: **Paint hair strands on this image: white where hair is visible, black where it is transparent. The edges should have irregular strand-like shapes, not sharp straight edges.
**Step 11: **Create another 1024x1024 image. Name it hair_m_01_base. Paint a flat mid-brown or neutral colour. This will be tinted at runtime.
**Step 12: **Create a third 1024x1024 image. Name it hair_m_01_roughness. Paint light grey with slight variation. This controls the sheen of the hair.
**Step 13: **Save all three images.

## **Rigging Hair to the Socket Bone**
**Step 14: **Import a copy of the armature from your base character (File > Append > body_male_final.glb > Object > Armature).
**Step 15: **Select the hair mesh. Then Shift-click the armature. Press Ctrl+P > With Automatic Weights.
**Step 16: **Go to Weight Paint mode. Paint the ENTIRE hair mesh with weight = 1.0 for the neck_01 bone (or head bone). Zero for everything else.
**Step 17: **Export as glTF 2.0. Save as: equip_hair_m_01.glb

## **Testing Hair in Godot**
**Step 18: **Copy equip_hair_m_01.glb to assets/characters/ in Godot.
**Step 19: **In your test scene, add a BoneAttachment3D to the Skeleton3D. Set Bone Name to: neck_01_socket.
**Step 20: **Add the hair mesh as a child of the BoneAttachment3D.
**Step 21: **Run the scene with idle animation. The hair should sit on the head and move with it.
**Step 22: **Test the bald look: hide the hair mesh node (click its eye icon). The head should look clean without the hair.
Hair sits correctly on the head. Bald look works cleanly.
**Step 23: **Repeat for all 6 hairstyles (3 male + 3 female).
Phase 11 complete! All 6 hairstyles are working in Godot.


**  PHASE 12**
**  Character Viewer — Testing Everything Together**
Tools: Godot 4     Estimated time: 2-3 hours
Now you build a simple interactive test scene in Godot where you can preview your full character system. This is not a game — it is a tool for checking that every part of your pipeline works correctly. You will be able to swap cybernetics, change blend shapes, toggle hair, preview overlays, and run animations, all from one screen.

Build this viewer before you start making any game systems. It gives you a fast way to spot problems and confirm fixes without loading a full game scene.

## **12.1  Scene Structure**
Create a new scene in Godot called CharacterViewer.tscn. The scene tree will look like this:

| Node | Purpose |
|------|---------|
| Node3D (root) | Root of the scene |
| Camera3D | Orbiting camera so you can view from any angle |
| DirectionalLight3D | Basic lighting to see the character clearly |
| CharacterRoot (Node3D) | Holds the character and all attachments |
| body_male_final (imported) | Your base character mesh with skeleton |
| AnimationPlayer | Plays idle/walk/run animations |
| CanvasLayer > Control | UI panel with all the toggle controls |

## **12.2  Orbiting Camera**
**Step 1: **Add a Camera3D to the scene. Position it at (0, 1.0, 3.0) facing the origin.
**Step 2: **Create a new script on the root Node3D called viewer.gd. Add this camera orbit code:
Script contents: extend Node3D, store orbit_angle and orbit_radius variables, get Camera3D with @onready. In _process: check ui_left and ui_right inputs to change orbit_angle, then update camera.position.x and camera.position.z using sin/cos of orbit_angle times radius. Call camera.look_at(Vector3(0, 1.0, 0)) to keep it facing the character.
**Step 3: **Press F5 to run the scene. Use the left and right arrow keys to orbit around the character.
You can now rotate the camera around the character to inspect it from all angles.

## **12.3  Animation Controls**
**Step 4: **Add an AnimationPlayer node as a child of your character scene.
**Step 5: **Import your idle, walk, and run animations (from Phase 9) and add them to the AnimationPlayer.
**Step 6: **Add this to your viewer.gd script to cycle animations:
See the workflow guide document for the complete GDScript code for this step.
**Step 7: **Press Spacebar in the viewer to cycle through idle, walk, and run animations.

## **12.4  Blend Shape Sliders**
Add UI sliders to control the Fat and Tall blend shapes in real time.

**Step 8: **In the CanvasLayer > Control node, add a VBoxContainer.
**Step 9: **Add a Label node inside it. Set its text to: Body Shape
**Step 10: **Add an HSlider node. Name it FatSlider. Set Min = 0, Max = your Fat cap value (e.g. 0.8), Step = 0.01.
**Step 11: **Add another HSlider. Name it TallSlider. Set Min = 0, Max = your Tall cap value.
**Step 12: **In your viewer.gd script, add:
See the workflow guide document for the complete GDScript code for this step.
**Step 13: **Run the scene. Moving the sliders should visibly change the character's body shape in real time.
Fat and Tall sliders update the character body smoothly. No seam popping visible at any slider value within cap range.

## **12.5  Cybernetic Toggle Buttons**
Add buttons to equip and unequip each cybernetic piece. Equipping a cybernetic hides the corresponding body chunk and shows the cybernetic mesh.

**Step 14: **For each cybernetic slot, add a Button node to the VBoxContainer. Label them: Left Arm, Right Arm, Left Leg, Right Leg, Chest, Head.
**Step 15: **Make sure each cybernetic piece is already added to the scene as a child of the appropriate BoneAttachment3D node (from Phase 10), but set to invisible by default.
**Step 16: **Add this toggle logic to viewer.gd:
See the workflow guide document for the complete GDScript code for this step.
**Step 17: **Run the scene. Click Left Arm to toggle between the flesh arm and the cybernetic arm.
Flesh arm disappears and cybernetic arm appears cleanly at the shoulder attachment point. No visible gap. Repeat for all 6 slots.

## **12.6  Hair Toggle**
**Step 18: **Add a OptionButton (dropdown) to the VBoxContainer. Label it Hair Style.
**Step 19: **Add items to it: Bald, Male Style 1, Male Style 2, Male Style 3 (or whichever styles you have).
**Step 20: **Make sure all hair meshes are in the scene attached to neck_01_socket, set to invisible by default except the first one.
**Step 21: **Connect the OptionButton item_selected signal:
See the workflow guide document for the complete GDScript code for this step.
**Step 22: **Run the scene. The dropdown should switch between bald and each hairstyle.
Hairstyles switch correctly. Bald option shows a clean head with no artifacts.

## **12.7  Overlay Preview**
Add a way to toggle scar and resonance crack overlays to see how they look at runtime.

**Step 23: **In Godot, create a new ShaderMaterial for the character's skin. This replaces the default material.
**Step 24: **In the shader, add two uniform texture slots:
See the workflow guide document for the complete GDScript code for this step.
**Step 25: **Assign your body_base_male.png, overlay_scar_arm_l_01.png, and body_resonance_mask.png to the shader's texture slots.
**Step 26: **Add two HSliders to the viewer UI: Scar Strength and Resonance Strength (both 0.0 to 1.0).
**Step 27: **Connect sliders to update the shader parameters:
See the workflow guide document for the complete GDScript code for this step.
**Step 28: **Run the viewer. Moving the Scar Strength slider should fade scars onto the character's skin. Moving Resonance Strength should make the crack pattern appear.
Overlays blend onto the character correctly. No hard edges. The base skin colour is unchanged at 0. Full effect visible at 1.

## **12.8  Final Viewer Test**
Run through this full test sequence to confirm everything works together:

- Character loads and stands in T/A pose with idle animation playing
- Camera orbits correctly with arrow keys
- Fat slider changes body width on all chunks simultaneously with no seam gaps
- Tall slider changes body height on all chunks simultaneously with no seam gaps
- Left Arm cybernetic toggles cleanly — flesh hidden, cyber shown, no gap
- Right Arm cybernetic toggles cleanly
- Left Leg cybernetic toggles cleanly
- Right Leg cybernetic toggles cleanly
- Chest cybernetic toggles cleanly
- Head cybernetic toggles cleanly
- All cybernetics can be active simultaneously with no visual conflicts
- Hair dropdown cycles through all styles and bald correctly
- Scar overlay fades in and out correctly
- Resonance crack mask fades in and out correctly
- Switching animation (Space) works with all cybernetics and hair active
- 10 characters spawned simultaneously with random blend shapes — no seams, acceptable performance
All checks pass. Your character system is complete and ready for game systems integration.


# **Final Checklist**
Use this checklist to confirm everything is complete before moving on to building the rest of your game.

## **Base Meshes**
- Male base mesh imports into Godot without errors
- Female base mesh imports into Godot without errors
- All 6 chunks visible and correctly positioned on each character
- Idle, walk, and run animations play correctly on both characters
- Fat blend shape works on all chunks (within cap value)
- Tall blend shape works on all chunks (within cap value)
- All 6 socket bones present and tracked correctly
- No visible seams between chunks under normal lighting

## **Cybernetic Pieces**
- All 6 cybernetic pieces import correctly
- Each attaches to the correct socket bone without misalignment
- No visible gap at attachment point when corresponding body chunk is hidden
- Each piece moves correctly with animations

## **Hair Meshes**
- All 6 hairstyles import correctly
- Each attaches to neck_01_socket and follows head movement
- Bald look (hidden hair) looks clean with no artifacts

## **Character Viewer**
- Camera orbits correctly
- All blend shape sliders work in real time
- All 6 cybernetic toggles work correctly
- Hair dropdown cycles correctly
- Scar and resonance overlays blend correctly via shader
- 10-character stress test passes

## **Blend Shape Cap Values (Write These Down)**

| Shape Key | Your Cap Value | Notes |
|-----------|---------------|-------|
| Fat | ___ | Maximum before distortion appears |
| Tall | ___ | Maximum before distortion appears |


**End of Guide — You did it!**
