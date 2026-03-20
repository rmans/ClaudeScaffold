# AI to 3D Character — Complete Step-by-Step Guide

> **Scope:** Godot 4 game characters using AI tools and Blender. Beginner friendly — every step is explained in plain language.

---

# Before You Start

Read this whole section before you do anything else. It will save you a lot of time.

## What You Are Making

By the end of this guide you will have:

- 2 base character meshes (one male, one female) with 6 body parts each
- 6 cybernetic replacement pieces (arms, legs, chest, head)
- 6 hairstyle meshes (3 for male characters, 3 for female)
- All of these working correctly inside Godot 4

## Tools You Need to Install First

Install all of these before starting. They are all free unless marked with a cost.

| Tool | Where to Get It | What It Does |
|------|----------------|--------------|
| Blender | blender.org | The main 3D program. Free. |
| Godot 4 | godotengine.org | Your game engine. Free. |
| Auto-Rig Pro | blendermarket.com | Blender addon for rigging. ~$40. Worth it. |
| ComfyUI Cloud | comfy.org/cloud | Makes AI concept images. Free tier available. |
| Tripo AI | tripo3d.ai | Turns images into 3D meshes. Free credits to start. |
| Hunyuan3D | 3d.hunyuan.tencent.com | Cleans up mesh topology. Free. |
| Nano Banana Pro | fal.ai/models/fal-ai/nano-banana-pro | Splits character images into parts. Pay per use. |

## The Golden Rules

> **STOP — Read these before doing anything.**
>
> 1. **NEVER join your mesh chunks together in Blender.** Each body part (head, torso, arms, legs) must always stay as a separate object. If you accidentally join them, press `Ctrl+Z` immediately.
> 2. **Always save your work before trying something new.** In Blender: `File > Save`. Do this every 10 minutes.
> 3. **Do the ENTIRE pipeline on just the male base mesh first.** This proves everything works and teaches you the process. The second character will be much faster.

## How This Guide Is Structured

This guide has 12 phases. Phases 1–11 build the assets. Phase 12 builds a character viewer in Godot so you can test everything together.

Each phase has numbered steps. Inside some steps there are lettered sub-steps (a, b, c). Follow them in order.

**Callout key:**

| Marker | Meaning |
|--------|---------|
| **SUCCESS** | You did it right — this is what success looks like |
| **WARNING** | Be careful here — common mistake coming up |
| **STOP** | Read this before doing anything |
| **TIP** | Helpful hint to make things easier |

## Two Paths: MVP and Final

Every phase has a fast MVP path and a slower Final path. Get something working first. Polish it second.

| Phase | MVP Path (fast) | Final Path (clean) |
|-------|----------------|-------------------|
| 3 — 3D gen | Accept whatever Tripo gives you | Regenerate until you get a clean mesh |
| 4 — Cleanup | Skip Shrinkwrap, just position roughly | Close all gaps cleanly |
| 5 — Retopo | Use Hunyuan3D output as-is | Review and manually fix bad edge loops |
| 6 — Textures | Flat grey skin, no mask maps yet | All 5 mask maps painted properly |
| 7 — Rigging | Use Auto-Rig Pro defaults, test basic pose | Full weight paint cleanup at all joints |
| 8 — Blend shapes | Add Fat and Tall, test at 0.5 only | Find exact cap values, test full range |
| 12 — Viewer | One character, swap one cybernetic | Full viewer with all toggles working |

## This Work Is Not Linear — Expect to Go Backwards

You will finish Phase 7 and discover a UV problem from Phase 5. This is normal.

| Problem You Discover | Go Back To | What to Redo |
|----------------------|-----------|--------------|
| Visible seam in Godot | Phase 5, Step 2 | Rejoin mesh, redefine cut loops, re-split |
| Shoulder collapses in animation | Phase 7, weight paint | Fix shoulder weight distribution only |
| Blend shapes show seam drift | Phase 8, Step 1 | Rejoin, re-sculpt on unified mesh, re-split |
| UV atlas wrong after split | Phase 5, UV section | Rejoin, repack UV islands, re-split |
| Normal map looks like photo | Phase 6, normal bake | Check bake type is Normal not Diffuse, rebake |
| Cybernetic drifts from socket | Phase 7, socket bones | Verify socket bone has zero length and correct parent |
| Animation bones move wrong | Phase 7, export | Apply pose as rest pose in Auto-Rig Pro, re-export |

## Fallback Strategies When Tools Fail

| Tool / Step That Failed | Fallback Option | Notes |
|------------------------|----------------|-------|
| Tripo AI gives unusable mesh | Different concept image with cleaner background. Try Meshy.ai. | Usually a background/silhouette clarity issue |
| Hunyuan3D gives bad topology | Blender's Remesh modifier (Voxel mode, Size 0.02) | Lower quality but works. Polish manually. |
| Auto-Rig Pro fails to detect markers | Place markers manually in the Smart interface | Manual placement takes 10 extra minutes but works reliably |
| Voxel bind gives broken weights | Delete armature modifier, re-bind with Envelope Weights | Envelope weights are cruder but more predictable |
| Weight painting feels hopeless | Smooth Weights brush + Transfer Weights from working side | Transfer Weights works across L/R symmetry |
| Normal map bake crashes | Skip normal maps for now — add them later | Normal maps are optional for body mesh |
| Godot import errors on `.glb` | Export as FBX instead. Check: apply modifiers, +Y up, include armature. | FBX import in Godot is more forgiving than glTF |

---

# Phase 1 — Create Concept Images

> **Tools:** ComfyUI Cloud | **Time:** 1–2 hours

Think of this phase like drawing a blueprint. You are telling the AI what your characters should look like. These images will be used in Phase 3 to create the actual 3D shapes.

## What is ComfyUI?

ComfyUI is a website where you can run AI image generation. You type in a description and it draws a picture.

## Setting Up ComfyUI

1. Open your web browser and go to `comfy.org/cloud`.
2. Create a free account if you do not have one.
3. Load the **Qwen Image 2.5** workflow:
   - a. Download the workflow file from the workflow guide document.
   - b. In ComfyUI, click **Load** or **Import Workflow**.
   - c. Select the file you downloaded.

> **SUCCESS:** You will see a diagram with connected boxes appear on screen.

## Generate the Male Base Character

You need a full-body image with arms at a 45-degree angle (**A-pose**). This arm position is critical for later steps.

4. Find the text input box (labelled **Prompt** or **Positive Prompt**).
5. Enter this prompt (you can change style words but keep the pose description):

```
full body male human character, A-pose with arms at 45 degrees, solid pure white background, no shadows, sci-fi colony aesthetic, semi-realistic, neutral expression, no weapons, standing straight, full body visible from head to feet
```

> **WARNING:** The background MUST be white or solid colour. If the background has details, the next tool cannot separate the body parts correctly.

6. Click **Generate** and wait 30–60 seconds.
7. Check the result:
   - a. Are both arms visible and at roughly 45 degrees?
   - b. Is the whole body visible from head to feet?
   - c. Is the background plain white or a single solid colour?
   - d. Does the character look like a full human, not cut off?

> **SUCCESS:** If you answered yes to all four, this image is good.
>
> **WARNING:** If not, click Generate again. The AI makes a different image each time. Keep going until you get a good one.

8. Run the **Upscale** option to make the image larger and clearer.
9. Download and save as `concept_base_male.png` in a folder called `character_project`.

## Generate the Female Base Character

10. Repeat Steps 4–9 with this prompt:

```
full body female human character, A-pose with arms at 45 degrees, solid pure white background, no shadows, sci-fi colony aesthetic, semi-realistic, neutral expression, no weapons, standing straight, full body visible from head to feet
```

11. Save as `concept_base_female.png`.

## Generate Cybernetic Concepts

One image per cybernetic body part. Solid white background, no shadows.

12. Generate and save each:

| Save As | Prompt | Notes |
|---------|--------|-------|
| `concept_cyber_arm_l.png` | `sci-fi cybernetic mechanical left arm replacement, hard surface metal, clean mounting plate at shoulder, white background` | Right side will be mirrored in Blender |
| `concept_cyber_leg_l.png` | `sci-fi cybernetic mechanical left leg replacement, hard surface metal, mounting plate at hip, white background` | Right side will be mirrored in Blender |
| `concept_cyber_chest.png` | `sci-fi cybernetic chest plate replacement, hard surface metal, front view, white background` | Front-facing |
| `concept_cyber_head.png` | `sci-fi cybernetic head replacement, visor and sensor array, hard surface metal, white background` | Full head replacement |

## Generate Hair Concepts

13. Generate 3 male and 3 female hairstyles. Example prompt:

```
male short hair, front and side view, isolated on white background, no face, just the hairstyle
```

14. Save as: `concept_hair_m_01.png` through `03`, `concept_hair_f_01.png` through `03`.

> **SUCCESS:** Phase 1 complete — you should have 14 images in your `character_project` folder.

---

# Phase 2 — Split Body Parts

> **Tools:** Nano Banana Pro | **Time:** 30 minutes

Nano Banana Pro takes your full-body character image and creates separate images for each body part. You only need this for the base characters — cybernetics and hair are already single parts.

## Why Split?

Tripo AI works best with one body part at a time. Full-body images produce messy 3D results. Separate parts give much cleaner meshes.

## Splitting the Male Character

1. Go to `fal.ai/models/fal-ai/nano-banana-pro`.
2. Upload `concept_base_male.png`.
3. Set Resolution to **2K**.
4. Select parts: **head, torso, arm, leg**. Only ONE arm and ONE leg — the right side will be mirrored in Blender.

> **TIP:** Mirroring saves time and ensures perfect symmetry. Asymmetric details (scars, tattoos) are added later as shader overlays.

5. Click **Generate** and wait.
6. Download and save:
   - `part_male_head.png`
   - `part_male_torso.png`
   - `part_male_arm.png` (will become both left and right arm)
   - `part_male_leg.png` (will become both left and right leg)

> **SUCCESS:** Each image shows just one body part on a white background.

## Splitting the Female Character

7. Repeat Steps 1–6 using `concept_base_female.png`.
8. Save as: `part_female_head.png`, `part_female_torso.png`, `part_female_arm.png`, `part_female_leg.png`.

> **SUCCESS:** Phase 2 complete — 8 part images (4 male + 4 female) plus your originals.

---

# Phase 3 — Generate 3D Meshes

> **Tools:** Tripo AI | **Time:** 2–3 hours

Tripo AI turns each 2D image into a 3D object. You only generate one arm and one leg per character — mirroring handles the other side. This reduces generations from 24 to 16.

## Setting Up Tripo AI

1. Go to `tripo3d.ai` and create a free account.
2. Log in. You will see a dashboard with an **Upload** or **Create** button.

## Required Settings (Use Every Time)

> **WARNING:** Wrong settings = bad meshes. Check these for every generation.

- **Quality:** Ultra
- **Mesh Type:** Triangle
- **UV:** Auto

## Generating Each Chunk

Repeat this for all 16 parts:

3. Click **Upload** or **Create**.
4. Upload your part image (e.g., `part_male_head.png`).
5. Confirm settings: Ultra quality, Triangle mesh, Auto UV.
6. Click **Generate** (1–3 minutes per mesh).
7. Click **Export** and choose **FBX** format.
8. Save with the correct name:

| Input Image | Save As | Notes |
|-------------|---------|-------|
| `part_male_head.png` | `raw_male_head.fbx` | Male base |
| `part_male_torso.png` | `raw_male_torso.fbx` | Male base |
| `part_male_arm.png` | `raw_male_arm.fbx` | Mirrored to both sides in Blender |
| `part_male_leg.png` | `raw_male_leg.fbx` | Mirrored to both sides in Blender |
| `part_female_head.png` | `raw_female_head.fbx` | Female base |
| `part_female_torso.png` | `raw_female_torso.fbx` | Female base |
| `part_female_arm.png` | `raw_female_arm.fbx` | Mirrored |
| `part_female_leg.png` | `raw_female_leg.fbx` | Mirrored |
| `concept_cyber_arm_l.png` | `raw_cyber_arm.fbx` | Mirrored to L and R |
| `concept_cyber_leg_l.png` | `raw_cyber_leg.fbx` | Mirrored to L and R |
| `concept_cyber_chest.png` | `raw_cyber_chest.fbx` | Single piece |
| `concept_cyber_head.png` | `raw_cyber_head.fbx` | Single piece |
| `concept_hair_m_01–03.png` | `raw_hair_m_01–03.fbx` | 3 male hairstyles |
| `concept_hair_f_01–03.png` | `raw_hair_f_01–03.fbx` | 3 female hairstyles |

> **SUCCESS:** Phase 3 complete — 16 `.fbx` files in your `character_project` folder.

---

# Phase 4 — Assemble and Clean Up in Blender

> **Tools:** Blender | **Time:** 2–4 hours

Import all body part meshes, position them into a complete body, and fix obvious problems.

## Opening Blender for the First Time

The 3D viewport is the big grey area in the middle. The **Outliner** (top-right) shows everything in your scene.

1. Open Blender.
2. Delete everything in the default scene: press `A` to select all, then `Delete`, then confirm.

> **SUCCESS:** The 3D viewport should now be completely empty.

## Importing the Male Body Parts

3. Import the 4 male meshes via `File > Import > FBX`, one at a time:
   - a. `raw_male_head.fbx`
   - b. `raw_male_torso.fbx`
   - c. `raw_male_arm.fbx`
   - d. `raw_male_leg.fbx`
4. They might look like blobs at first — that is normal.

> **SUCCESS:** 4 separate objects visible in the Outliner panel.

## Positioning the Parts

> **TIP:** Press `Numpad 1` = front view. `Numpad 3` = side view. `Numpad 7` = top view.

5. Click an object in the Outliner to select it (orange outline).
6. Press `G` to grab/move. `G` then `X` = left/right only. `G` then `Z` = up/down only.
7. Arrange: torso in the middle, head on top, arm on the LEFT side, leg on the LEFT side.

> **WARNING:** Place arm and leg on the LEFT side only. The Mirror modifier creates the right side automatically.

## Mirroring Arms and Legs

Mirror modifier creates a perfect symmetrical copy, saving half the work.

8. Click the arm mesh to select it.
9. In Properties panel, click the blue wrench icon (**Modifiers**).
10. Click `Add Modifier > Mirror`.
11. Make sure **X Axis** is ticked. A mirrored copy should appear on the right side.
12. Verify the character looks symmetrical.

> **TIP:** If the mirrored copy appears in the wrong place, press `Ctrl+A > All Transforms` first, then try again.

13. Do **NOT** apply the Mirror modifier yet. Leave it active.
14. Repeat steps 8–13 for the leg mesh.

> **SUCCESS:** Complete character silhouette with mirrored arms and legs. Outliner shows 4 objects, but all 6 chunks are represented visually.

## Closing Gaps Between Parts

15. Click the torso, press `Tab` to enter Edit Mode.
16. Click vertices near gaps and press `G` to nudge them closed.

> **TIP:** You don't need a perfect join here. The join-then-split process in Phase 5 handles precise seam matching.

17. Press `Tab` to return to Object Mode.

## Apply the Mirror Modifier

18. Click the arm mesh.
19. In the Modifiers panel, click **Apply** next to the Mirror modifier.
20. The arm mesh now contains both sides as real geometry.
21. Repeat for the leg mesh.

> **TIP:** After applying Mirror, both arms share the same UV space. This is intentional — asymmetric details are added as overlay textures at runtime.

## Freezing Transforms

22. Press `A` to select all 4 objects.
23. Press `Ctrl+A` and choose **All Transforms**.

> **SUCCESS:** Position/rotation/scale numbers reset to defaults.

## Rough Polycount Reduction

AI meshes have too many polygons. Reduce before uploading to Hunyuan3D.

24. Click one mesh to select it.
25. `Modifiers panel > Add Modifier > Decimate`.
26. Start with **Ratio 0.3**. If the shape still looks correct, click **Apply**.
27. If the shape looks broken, increase ratio to 0.5 and try again.
28. Repeat for all 4 meshes.
29. Export each as FBX: `raw_male_head_decimated.fbx`, `raw_male_torso_decimated.fbx`, `raw_male_arm_decimated.fbx`, `raw_male_leg_decimated.fbx`.

> **SUCCESS:** Phase 4 complete — character assembled with mirrored limbs and reduced polygon count.

---

# Phase 5 — Retopology and UV Mapping

> **Tools:** Hunyuan3D + Blender | **Time:** 3–5 hours

Retopology rebuilds the mesh surface with clean, evenly-spaced polygons. The AI mesh is messy — Hunyuan3D creates a clean version. Then you set up UV maps in Blender.

## What is Retopology?

Imagine wrapping crumpled tin foil around a ball — that's what the AI mesh looks like. Retopology replaces it with a smooth fabric that fits the same shape. The result animates much better.

## Retopology via Hunyuan3D

1. Go to `3d.hunyuan.tencent.com`.
2. Upload `raw_male_head_decimated.fbx`.
3. Choose face count:
   - a. Head and Torso: **High**
   - b. Arms and Legs: **Standard**
4. Enable **Intelligent UV Unfolding**.
5. Click **Generate** and wait.
6. Download and save as `retopo_male_head.fbx`.
7. Repeat for all 6 male chunks, all 6 female chunks, and all 6 cybernetic pieces.

> **TIP:** Hair meshes do NOT need Hunyuan3D retopology — you'll build hair cards manually in Phase 11.
>
> **SUCCESS:** Each retopologised mesh should look smoother with evenly-spaced polygons.

## Import Retopologised Meshes into Blender

8. Open Blender. Delete the default scene.
9. Import all 6 retopologised male chunks via `File > Import > FBX`.
10. Position them into a complete character shape (same as Phase 4).

## Check Total Polygon Count

11. Click a chunk to select it.
12. Look at the bottom of the Blender window for the triangle count (**Tris**).
13. Add up tri counts for all 6 chunks. Target: **5,000–10,000 tris**.

> **WARNING:** If over 10,000, add a Decimate modifier (ratio 0.8) to the largest chunks and recheck.

## Setting Up the Shared UV Atlas

All 6 body chunks must share one single texture image. Each chunk's UV map goes in a different area of the same texture space — like fitting six pictures into one frame without overlapping.

> **TIP:** Open the UV Editor via the top menu `+` icon next to layout tabs, and choose **UV Editing**.

14. Click the **UV Editing** tab at the top.
15. Select the Head chunk in the viewport.
16. Press `Tab` (Edit Mode), then `A` (select all vertices).
17. In the UV Editor, you should see the head's UV map.
18. Scale and move the head UV islands to the **top-left quarter**: `A` (select all), `S` (scale down), `G` (move).
19. Press `Tab` to exit Edit Mode.
20. Repeat for each chunk:

> **TIP:** Mirrored arms and legs already share UV space. Place them as one set of islands, not two.

| Chunk | UV Position | Notes |
|-------|------------|-------|
| Head | Top-left quarter | ~1/4 of total space |
| Torso | Top-right quarter | ~1/4 of total space |
| Arm (L+R mirrored) | Bottom-left half | Both sides share this region |
| Leg (L+R mirrored) | Bottom-right half | Both sides share this region |

21. Screenshot the UV Editor and save as `uv_layout_male.png` for reference.

> **STOP:** Check that NO UV islands from different chunks overlap. Overlapping = broken textures.

## Eliminating Seams — The Right Way

This is the most important technique in the entire pipeline: **join all chunks into one mesh, define clean cut lines, then split apart**. The split edges come from the same mesh, so they are perfectly matched by definition.

> **STOP:** Do NOT try to match seams by manually typing X/Y/Z coordinates. It doesn't scale and animation will expose mistakes.

### Step 1 — Join All Chunks Into One Mesh

22. Make sure all 6 retopologised chunks are positioned correctly.
23. Press `A` to select all 6 chunks.
24. Press `Ctrl+J` to join into a single mesh object.

> **SUCCESS:** Outliner shows one mesh object instead of six.

### Step 2 — Define Clean Cut Lines

25. Press `Tab` (Edit Mode).
26. Switch to **Edge Select**: press `2` on keyboard (not numpad).
27. `Alt+Click` on an edge at the shoulder to select the entire edge loop.

> **TIP:** If `Alt+Click` selects wrong edges, hold `Shift` and click to manually adjust.

28. Select edge loops at all 5 split points:
   - Neck (head from torso)
   - Left shoulder (left arm from torso)
   - Right shoulder (right arm from torso)
   - Left hip (left leg from torso)
   - Right hip (right leg from torso)

> **WARNING:** Make sure each edge loop goes all the way around with no gaps.

### Step 3 — Mark the Seams

29. With split edge loops selected: `Edge menu > Mark Seam`. Selected edges turn red.

### Step 4 — Separate Into Chunks

30. Switch to **Face Select**: press `3`.
31. Click a face on the head, press `Ctrl+L` (select all connected).
32. Press `P > Selection`. The head is now a separate object.
33. Rename it in the Outliner: `body_male_head`.
34. Repeat for each region:
   - Torso face → `Ctrl+L` → `P > Selection` → `body_male_torso`
   - Left arm → `body_male_arm_l`
   - Right arm → `body_male_arm_r`
   - Left leg → `body_male_leg_l`
   - Right leg → `body_male_leg_r`

> **SUCCESS:** 6 separate objects with perfectly matched boundary edges — zero seam gaps.
>
> **STOP:** Verify the Outliner shows exactly 6 objects with correct names before moving on.

### Step 5 — Apply This Approach to Blend Shapes Too

> **TIP:** Write this down: **join first, sculpt or split, then separate.** This one rule eliminates the two biggest risk areas in the entire pipeline.

> **SUCCESS:** Phase 5 complete — clean retopologised meshes with perfectly matched seams and a shared UV atlas.

---

# Phase 6 — Textures and Mask Maps

> **Tools:** Blender | **Time:** 3–5 hours

Two types of textures: the base colour (what the skin looks like) and mask maps (invisible guides for shader effects).

## The Most Important Rule About Textures

> **STOP:** Do NOT bake lighting, shadows, or ambient occlusion into your base colour texture. The texture should be flat and even — like a colouring book page with no shading. Shading is added at runtime by the engine.
>
> **Exception:** Normal maps record surface bumps and angles, not lighting. They are allowed.

## What Each Map Does

| Map Name | Colours Used | Purpose |
|----------|-------------|---------|
| Base skin texture | Flat skin colours | Basic colour. No shading, no highlights. |
| Skin region mask | White and black | White = skin. Black = not skin. |
| Attachment zone mask | Grey gradient | Where cybernetics attach. White at socket, fading to black. |
| Variation mask | Grey areas | Where scars and tattoos can appear. |
| Resonance crack mask | Dark fracture lines | Stress fracture patterns for characters with powers. |
| Normal map | Blue-purple | Surface bumps. Baked from high-poly mesh. |

## Setting Up for Texture Painting

1. Switch to the **Texture Paint** workspace tab.
2. Select the torso chunk.
3. Properties panel → material icon → **New** material.
4. Name it `mat_body_skin`.
5. Click the yellow dot next to **Base Color** → **Image Texture**.
6. Click **New**: Width/Height = 2048, Color = mid-tone skin colour.
7. Name the image `body_base_male`.
8. Assign this **same** material and **same** image to all 6 body chunks.

> **TIP:** To reuse the material: click another chunk → Material Properties → dropdown → select `mat_body_skin`.

## Painting the Base Skin Texture

9. In Texture Paint workspace: painting tools on the left, 3D view in the centre, UV editor on the right.
10. Paint flat skin colour. **No shading or highlights** — keep it even.
11. Slightly different flat tones for different zones (face, body, hands/feet).

> **TIP:** If using Modddif.com for a textured reference: export as OBJ, upload, generate — but use the result ONLY as a colour reference. It will have baked shading that must be removed.

12. Save: `Image > Save As` → `body_base_male.png`.

## Painting the Mask Maps

Each mask uses the same UV layout. Create a new image for each and paint in greyscale.

13. **Skin Region Mask** (2048x2048): All WHITE, then BLACK over non-skin areas (eye sockets, inside mouth). Save as `body_skin_mask.png`.
14. **Attachment Zone Mask** (2048x2048): All BLACK, then WHITE circles at each socket location (shoulders, hips, chest, neck) with soft brush gradient. Save as `body_attachment_mask.png`.
15. **Variation Mask** (2048x2048): Medium grey over scar-eligible areas (arms, torso, face sides). Darker on palms/soles. Save as `body_variation_mask.png`.
16. **Resonance Crack Mask** (2048x2048): All BLACK, then thin DARK GREY branching crack lines across torso and arms. Save as `body_resonance_mask.png`.

## Overlay Textures — Asymmetric Details

Mirrored UVs mean the base skin is identical on both sides. For asymmetric details (scars, tattoos), use **overlay textures** — separate small images composited by the shader at runtime.

> **TIP:** Think of overlays like stickers on top of the base skin. Mix different stickers per character for variety.

Overlays have their **own** UV unwrap, not the body atlas.

17. Select the arm mesh → `Tab` (Edit Mode).
18. Select only LEFT arm faces.
19. `UV > Unwrap` — creates a UV map for just those faces.
20. Create a 512x512 image, paint a scar pattern.
21. Save as `overlay_scar_arm_l_01.png`.
22. Create as many overlays as you want: scars, tattoos, birthmarks, burns.

> **WARNING:** Overlay textures are used by the runtime shader in Godot, not Blender. This step just produces the texture files.

## Normal Map Baking (Cybernetics)

Bake a normal map from the high-poly AI mesh to capture surface detail on the low-poly version.

23. Import both the high-poly mesh (`raw_cyber_arm_l.fbx`) AND the retopologised version (`retopo_cyber_arm_l.fbx`).
24. Position them exactly on top of each other.
25. Select the **LOW-POLY** mesh.
26. Create a material with an Image Texture node. New 2048x2048 image named `cyber_arm_l_normal`. Select the node (white border) but do **NOT** connect it.
27. Render Properties → change engine to **Cycles**.
28. Expand the **Bake** section.
29. Set Bake Type to **Normal**.
30. Enable **Selected to Active**.
31. Set Extrusion to **0.03**.
32. Click **Bake** (1–5 minutes).

> **SUCCESS:** Blue-purple image with slight colour variations at edges and panels.
>
> **STOP:** If the result looks like a photo (light and shadow), you baked Diffuse instead of Normal. Fix step 29.

33. Save as `cyber_arm_l_normal.png`.
34. Repeat for all 6 cybernetic pieces.

> **SUCCESS:** Phase 6 complete — all texture maps ready.

---

# Phase 7 — Rigging (Adding Bones)

> **Tools:** Blender + Auto-Rig Pro | **Time:** 4–6 hours

Rigging adds a skeleton inside the character so it can move and animate — like putting wire inside a puppet.

## Installing Auto-Rig Pro

1. Purchase from blendermarket.com/products/auto-rig-pro (download a `.zip`).
2. In Blender: `Edit > Preferences > Add-ons > Install`.
3. Select the `.zip` file.
4. Enable Auto-Rig Pro in the add-on list.
5. Close Preferences. The panel appears in the right sidebar (press `N` if hidden).

> **SUCCESS:** Auto-Rig Pro section visible in the N panel sidebar.

## Preparing the Character

6. All 6 body chunks positioned correctly in A-pose.
7. Select all: press `A`.
8. `Ctrl+A > All Transforms` to freeze transforms.

## Running Auto-Rig Pro Smart

9. In the Auto-Rig Pro panel, click **Smart**.
10. Click **Get Selected Objects**.
11. Click **Guess Markers** — coloured markers appear at detected joint positions.
12. Check each marker: head top, chin, shoulders, wrists, hips, ankles.
13. Drag any misplaced markers to the correct position.

> **WARNING:** Take your time. Wrong markers = wrong animation. Common mistakes: wrist markers too high, ankle markers too high, hip markers too far apart.

14. Click **Go**. Auto-Rig Pro builds the rig.

> **SUCCESS:** Armature (skeleton) visible as orange/yellow lines inside the character.

## Binding the Mesh to the Skeleton

15. In Auto-Rig Pro panel, click **Skin**.
16. Click **Voxelize** (wait for calculation).
17. Click **Bind**.

> **SUCCESS:** Nothing visible changes — the mesh is now bound to the skeleton.

## Testing the Rig

18. Click the armature.
19. Change to **Pose Mode** (dropdown at top-left of viewport).
20. Click an arm bone. Press `G` to move or `R` to rotate.
21. Watch the mesh follow the bone.
22. Check for problems:
   - a. Shoulder pinches or collapses? → Weight paint fix needed.
   - b. Torso moves when it shouldn't? → Weight paint fix needed.
   - c. Arm moves cleanly shoulder to wrist? → Good!
23. Press `Ctrl+Z` multiple times to undo test movements.

## Fixing Weight Paint Problems

Weight paint controls bone influence. Red = strong influence, blue = none.

24. Click the problem mesh chunk.
25. Switch to **Weight Paint** mode.
26. Select a bone via `Properties > Vertex Groups`.
27. Paint **red** (weight 1.0) on areas that should follow this bone completely.
28. Paint **blue** (weight 0.0) on areas that should NOT follow this bone.

> **TIP:** For arms: shoulder bone = weight 1.0 at upper arm, fading to 0.0 halfway down. Elbow bone takes over from there.

29. Return to Pose Mode and test again.

## Limiting Bone Influences

30. Select all mesh chunks (`A` in Object Mode).
31. `Object Data Properties > Vertex Groups`.
32. Find **Limit Total**.
33. Set to **4**.

> **TIP:** Max 4 bone influences per vertex is required for game engines.

## Adding Socket Bones

Socket bones are attachment points for cybernetics and equipment. They don't move the mesh.

34. Click the armature, press `Tab` (Edit Mode).
35. `Shift+Click` the shoulder bone, then press `E` to extrude a new bone.
36. Position it at the shoulder attachment point.
37. Rename to `upperarm_l_socket` in Bone Properties.
38. **Untick Deform** in Bone Properties.
39. Set tail position = head position (zero-length bone).
40. Add all 6 socket bones:

| Socket Bone Name | Parent (Extrude From) | Position |
|-----------------|----------------------|----------|
| `upperarm_l_socket` | Left upper arm bone | Left shoulder attachment |
| `upperarm_r_socket` | Right upper arm bone | Right shoulder attachment |
| `thigh_l_socket` | Left thigh bone | Left hip attachment |
| `thigh_r_socket` | Right thigh bone | Right hip attachment |
| `spine_03_socket` | Upper spine/chest bone | Centre chest attachment |
| `neck_01_socket` | Neck bone | Base of skull / head attachment |

41. Press `Tab` to exit Edit Mode.

## Exporting for Godot

42. Select all mesh chunks AND the armature (`A`).
43. `File > Export > glTF 2.0 (.glb/.gltf)`.
44. Export options:
   - a. `Include > Selected Objects` — ticked
   - b. `Transform > +Y Up` — ticked
   - c. `Geometry > Apply Modifiers` — ticked
   - d. `Animation > Shape Keys (Morph Targets)` — ticked
45. Save as `body_male_rigged.glb`.

> **SUCCESS:** Phase 7 complete — rigged character exported as `.glb` ready for Godot.

---

# Phase 8 — Blend Shapes (Body Variation)

> **Tools:** Blender | **Time:** 2–3 hours

Blend shapes (shape keys) morph the character between body types using sliders. You'll create **Fat** and **Tall** to generate different-looking characters.

## What is a Blend Shape?

A blend shape records a different position for every vertex. Slider at 0 = original shape. Slider at 1 = full morph. Slider at 0.5 = halfway between.

> **STOP:** Do NOT add blend shapes to each chunk separately — seams will drift and pop. Use the **join-then-split** approach from Phase 5.

## Step 1 — Join All Chunks

1. All 6 body chunks positioned correctly.
2. Press `A` to select all.
3. Press `Ctrl+J` to join into one mesh.

> **SUCCESS:** One unified mesh in the Outliner.

## Step 2 — Add the Basis Shape Key

4. Select the joined mesh.
5. Properties → green triangle icon (**Object Data Properties**).
6. Find **Shape Keys** → click `+`. A key named **Basis** appears (the default shape).

## Step 3 — Add the Fat Shape Key

7. Click `+` again. Rename to **Fat**.
8. Make sure Fat is selected/highlighted.
9. Press `Tab` (Edit Mode) — the shape key is now recording.
10. Press `A` (select all vertices).
11. Enable **Proportional Editing**: press `O`. Changes will fade out gradually.
12. Press `S` then `X` — scale outward on X axis (wider). Click to confirm.
13. Press `S` then `Y` — slight depth increase.
14. Widening should be most noticeable at waist, hips, upper arms, thighs.
15. Press `Tab` to exit Edit Mode.
16. Test: move the Fat slider from 0 to 1.

> **SUCCESS:** Character looks noticeably heavier at 1.0. Seams stay perfectly invisible.

17. Set Fat slider back to 0.

## Step 4 — Add the Tall Shape Key

18. Click `+`. Rename to **Tall**.
19. With Tall selected, press `Tab` (Edit Mode).
20. `A` (select all), then `S` then `Z` — scale upward on Z axis. Confirm.

> **TIP:** Scale the entire unified mesh — don't stretch only legs or torso. Keeps everything proportional.

21. Press `Tab` to exit. Test the Tall slider.
22. Set Tall slider back to 0.

## Step 5 — Split Back Into Chunks

23. Split using the same method as Phase 5, Steps 30–34:
   - a. `Tab` (Edit Mode), switch to Face Select (`3`).
   - b. Click a head face → `Ctrl+L` → `P > Selection`.
   - c. Repeat for torso, left arm, right arm, left leg, right leg.
   - d. Rename each chunk in the Outliner.

> **SUCCESS:** 6 separate chunks, each with identical Fat and Tall shape keys — perfectly consistent.

## Finding the Safe Slider Cap Values

24. Set both Fat and Tall to **1.0** on all chunks simultaneously.
25. Look for pinching, collapsing, or distortion.
26. If found: reduce sliders until distortion disappears. Add a small safety margin.
27. Example: distortion starts at 0.9 → cap value is **0.8**.
28. Write down: **Fat cap = ___**, **Tall cap = ___**.

## Re-Export with Shape Keys

29. Select all chunks and armature (`A`).
30. `File > Export > glTF 2.0`.
31. Confirm **Shape Keys (Morph Targets)** is ticked.
32. Save as `body_male_final.glb`.

> **SUCCESS:** Phase 8 complete — working blend shapes. Keep your cap values safe.

---

# Phase 9 — Import into Godot 4 and Validate

> **Tools:** Godot 4 | **Time:** 2–3 hours

Bring the character into the game engine and set up bone mapping for standard animation support.

## Setting Up Your Godot Project

1. Open Godot 4. Create a new project if needed.
2. Create folder structure in FileSystem panel:
   - a. `assets/characters`
   - b. `assets/animations`
   - c. `assets/cybernetics`
3. Copy `body_male_final.glb` into `assets/characters` on your hard drive.
4. Godot auto-detects the file.

## Configuring the Import Settings

5. Click `body_male_final.glb` in the FileSystem panel.
6. Open the **Import** panel.
7. Set `Animation > Import Rest As RESET` to **ON**.
8. Click **Reimport**.

> **SUCCESS:** No red error messages in the Output panel.

## Setting Up Bone Mapping

Map your rig's bones to Godot's standard humanoid bones. Do this once and reuse for all characters.

9. Double-click `body_male_final.glb` to open as a scene.
10. Find and click the **Skeleton3D** node.
11. Inspector → **Bone Map** → select **New BoneMap**.
12. Expand the BoneMap.
13. Set Profile to **SkeletonProfileHumanoid**.
14. Some slots auto-detect (green). Fix blank/orange slots:

| Godot Slot | Auto-Rig Pro Bone | Notes |
|-----------|-------------------|-------|
| Hips | `c_root_master.x` | Main root/hip bone |
| Spine | `spine_01.x` | Lower spine |
| Chest | `spine_02.x` | |
| UpperChest | `spine_03.x` | |
| Neck | `neck.x` | |
| Head | `head.x` | |
| LeftUpperArm | `arm_stretch.l` | |
| LeftLowerArm | `forearm_stretch.l` | |
| LeftHand | `hand.l` | |
| LeftUpperLeg | `thigh_stretch.l` | |
| LeftLowerLeg | `leg_stretch.l` | |
| LeftFoot | `foot.l` | |

> **TIP:** Right side = same names but `.r` instead of `.l`.

15. Save BoneMap as `assets/characters/bone_map_humanoid.tres`.

> **SUCCESS:** All bone slots show green.

## Setting Up the Test Scene

16. `Scene > New Scene` → add **Node3D** as root, name it `TestScene`.
17. Add a **Camera3D** child, position in front of the character.
18. Drag `body_male_final.glb` into the scene viewport.
19. Press `F5` to run.

> **SUCCESS:** Character standing in the game viewport, all 6 chunks visible.

## Testing Animations

20. Go to mixamo.com, upload `body_male_final.glb`.
21. Place markers for hips, wrists, elbows, knees, chin.
22. Search for **Idle** animation. Enable **In Place**.
23. Download: FBX, With Skin, 30 FPS. Save as `anim_idle.fbx`.
24. Copy to `assets/animations` in Godot.
25. Click `anim_idle.fbx` → Import panel → `Animation > Import As: Animation`.
26. Set Retarget BoneMap to `bone_map_humanoid.tres`.
27. Click **Reimport**.
28. Add an **AnimationPlayer** node as a child of the character.
29. Drag the animation into the AnimationPlayer.
30. Press play.

> **SUCCESS:** Idle animation plays correctly on all 6 chunks.
>
> **WARNING:** If bones twist unnaturally: go back to Blender → Auto-Rig Pro → **Apply Pose as Rest Pose** → re-export.

## Testing Blend Shapes

31. Click a MeshInstance3D node (a body chunk).
32. Inspector → **Blend Shapes** → Fat and Tall sliders.
33. Move Fat to your cap value. Mesh should get wider.
34. Move Tall to your cap value. Mesh should get taller.
35. Repeat for all 6 chunks.

> **SUCCESS:** All chunks blend correctly with no distortion within cap values.

## Testing Socket Bones

36. Click the Skeleton3D node.
37. Add child: **BoneAttachment3D** → set Bone Name to `upperarm_l_socket`.
38. Add a child **MeshInstance3D** with a simple **BoxMesh** (placeholder).
39. Run with idle animation playing.
40. The box should stay attached to the left shoulder throughout the animation.

> **SUCCESS:** Box follows the shoulder. Socket bone is working.

41. Test all 6 socket bones.
42. Remove test boxes when done.

## Stress Test — 10 Characters at Once

43. Duplicate the character 9 times (`Shift+D`).
44. Set different random Fat/Tall values on each (within cap range).
45. All 10 playing idle animation.
46. Zoom in close to one, then zoom out to see all 10. Check:
   - a. Visible seam lines?
   - b. Parts separating or floating?
   - c. Weird stretching at joints?
   - d. Performance acceptable?

> **SUCCESS:** All 10 animate smoothly, no visible seams, acceptable performance.
>
> **WARNING:** Seam problems on ANY character → go back to Phase 5 join-then-split. Do not move on.

> **SUCCESS:** Phase 9 complete — character fully working in Godot 4. The hardest part is done!

---

# Phase 10 — Cybernetic Pieces

> **Tools:** Blender + Godot 4 | **Time:** 4–6 hours

Process each of the 6 cybernetic pieces. Hard surface pieces are faster — no blend shapes or complex weight painting needed.

## Process for Each Cybernetic Piece

Repeat for: Left Arm, Right Arm, Left Leg, Right Leg, Chest, Head.

1. Open Blender. Delete default scene.
2. Import the raw cybernetic FBX (e.g., `raw_cyber_arm_l.fbx`).
3. Add Decimate modifier (ratio 0.3). Verify shape. Apply.
4. Upload to Hunyuan3D: **Hard Surface**, **Standard** quality, UV Unfolding enabled. Download result.
5. Target poly count: **500–1,500 triangles** per piece.
6. Create material + flat colour texture. Hard metal grey tones, no baked lighting.
7. Bake normal map from high-poly to retopo mesh (same as Phase 6, steps 23–34).
8. Position so the attachment end extends **1–1.5cm** into where the body chunk would be.
9. Import the armature from `body_male_final.glb`:
   - `File > Append` (not Import) → navigate to `.glb` → `Object` → select **Armature**
10. Select cybernetic mesh, `Shift+Click` armature → `Ctrl+P > With Automatic Weights`.
11. Weight Paint: paint **entire** mesh with weight 1.0 for the relevant bone. Zero for everything else.

> **TIP:** Cybernetics are hard surface — use hard 100% weights. One bone = one section. No smooth transitions.

12. Export as `cyber_arm_l_01.glb`.
13. In Godot: copy to `assets/cybernetics/`. Import.
14. Add **BoneAttachment3D** to Skeleton3D → set to `upperarm_l_socket`.
15. Add cybernetic scene as child.
16. Hide the corresponding body chunk (eye icon in scene tree).
17. Run idle animation and check:
   - a. Stays attached to socket?
   - b. No visible gap at attachment?
   - c. Moves naturally with animation?

> **SUCCESS:** No gap, moves with body, looks correct.

18. Repeat for all 6 pieces.

> **SUCCESS:** Phase 10 complete — all 6 cybernetic pieces working in Godot.

---

# Phase 11 — Hair Meshes

> **Tools:** Blender + Godot 4 | **Time:** 2–3 hours

Hair meshes are flat card shapes that create the illusion of volume. They attach to the head socket bone and can be swapped like equipment.

## What Are Hair Cards?

Instead of modelling every strand, use flat rectangles (cards) with hair textures. Many overlapping cards at different angles = realistic hairstyle. Like making a 3D bush from flat cardboard cutouts.

## Building Hair Cards in Blender

1. Open Blender. Delete default scene.
2. Open `concept_hair_m_01.png` for reference.
3. Create a plane: `Shift+A > Mesh > Plane`.
4. `S` to scale smaller. Position at the top of the head. `R` to rotate along hair flow.
5. `Shift+D` to duplicate, position to cover more of the hairstyle.
6. Add more cards (overlapping slightly) until the silhouette matches.

> **TIP:** 8–15 cards is enough for a simple hairstyle. More is not better.

7. Select all cards → `Ctrl+J` to join. Name: `equip_hair_m_01`.
8. UV unwrap: `Tab` (Edit Mode) → `A` → `UV > Smart UV Project`.

## Hair Textures

9. New 1024x1024 image: `hair_m_01_alpha`. Paint white where hair is visible, black where transparent. Irregular strand edges.
10. New 1024x1024 image: `hair_m_01_base`. Flat mid-brown or neutral colour (tinted at runtime).
11. New 1024x1024 image: `hair_m_01_roughness`. Light grey with slight variation (controls sheen).
12. Save all three.

## Rigging Hair to the Socket Bone

13. `File > Append` → `body_male_final.glb` → Object → Armature.
14. Select hair mesh, `Shift+Click` armature → `Ctrl+P > With Automatic Weights`.
15. Weight Paint: entire hair mesh = weight 1.0 for `neck_01` (or head) bone. Zero for everything else.
16. Export as `equip_hair_m_01.glb`.

## Testing Hair in Godot

17. Copy to `assets/characters/` in Godot.
18. Add **BoneAttachment3D** to Skeleton3D → Bone Name: `neck_01_socket`.
19. Add hair mesh as child.
20. Run with idle animation. Hair should sit on head and move with it.
21. Test bald: hide the hair node. Head should look clean.

> **SUCCESS:** Hair sits correctly. Bald look is clean.

22. Repeat for all 6 hairstyles (3 male + 3 female).

> **SUCCESS:** Phase 11 complete — all 6 hairstyles working in Godot.

---

# Phase 12 — Character Viewer (Testing Everything Together)

> **Tools:** Godot 4 | **Time:** 2–3 hours

Build an interactive test scene to preview the full character system: swap cybernetics, change blend shapes, toggle hair, preview overlays, run animations.

> **TIP:** Build this viewer before making any game systems. Fast way to spot problems and confirm fixes.

## 12.1 — Scene Structure

Create `CharacterViewer.tscn`:

| Node | Purpose |
|------|---------|
| `Node3D` (root) | Scene root |
| `Camera3D` | Orbiting camera |
| `DirectionalLight3D` | Basic lighting |
| `CharacterRoot` (Node3D) | Character + attachments |
| `body_male_final` (imported) | Base character mesh + skeleton |
| `AnimationPlayer` | Idle/walk/run animations |
| `CanvasLayer > Control` | UI toggle panel |

## 12.2 — Orbiting Camera

1. Add Camera3D at position `(0, 1.0, 3.0)` facing origin.
2. Create `viewer.gd` on root Node3D with orbit logic: track `orbit_angle` and `orbit_radius`, update camera position with sin/cos, call `camera.look_at(Vector3(0, 1.0, 0))`.
3. Run with `F5`. Arrow keys orbit around the character.

> **SUCCESS:** Camera rotates around the character from all angles.

## 12.3 — Animation Controls

4. Add **AnimationPlayer** as child of character.
5. Import idle, walk, run animations and add to the player.
6. Add spacebar toggle logic to `viewer.gd`.
7. Spacebar cycles through idle → walk → run.

## 12.4 — Blend Shape Sliders

8. In `CanvasLayer > Control`, add a **VBoxContainer**.
9. Add a **Label**: "Body Shape".
10. Add **HSlider** named `FatSlider`: Min=0, Max=your Fat cap, Step=0.01.
11. Add **HSlider** named `TallSlider`: Min=0, Max=your Tall cap, Step=0.01.
12. Connect sliders to update blend shapes on all chunks in `viewer.gd`.
13. Run. Sliders change body shape in real time.

> **SUCCESS:** Fat and Tall sliders update smoothly. No seam popping within cap range.

## 12.5 — Cybernetic Toggle Buttons

14. Add **Button** nodes to VBoxContainer: Left Arm, Right Arm, Left Leg, Right Leg, Chest, Head.
15. Cybernetic pieces already in scene as children of BoneAttachment3D nodes, invisible by default.
16. Add toggle logic: button press hides flesh chunk, shows cybernetic (and vice versa).
17. Test each toggle.

> **SUCCESS:** Flesh disappears, cybernetic appears cleanly. No gap. Repeat for all 6 slots.

## 12.6 — Hair Toggle

18. Add **OptionButton** (dropdown) to VBoxContainer: Bald, Style 1, Style 2, Style 3.
19. All hair meshes in scene attached to `neck_01_socket`, invisible by default.
20. Connect `item_selected` signal to switch visibility.
21. Test dropdown.

> **SUCCESS:** Hairstyles switch correctly. Bald shows a clean head.

## 12.7 — Overlay Preview

22. Create a **ShaderMaterial** for the skin material.
23. Add uniform texture slots for scar overlay and resonance mask.
24. Assign `body_base_male.png`, `overlay_scar_arm_l_01.png`, and `body_resonance_mask.png`.
25. Add two **HSliders**: Scar Strength and Resonance Strength (0.0–1.0).
26. Connect sliders to shader uniform parameters.
27. Test: Scar slider fades scars in. Resonance slider shows crack pattern.

> **SUCCESS:** Overlays blend correctly. No hard edges. Base skin unchanged at 0, full effect at 1.

## 12.8 — Final Viewer Test

Run through the complete checklist:

- [ ] Character loads in A-pose with idle animation playing
- [ ] Camera orbits with arrow keys
- [ ] Fat slider changes width on all chunks — no seam gaps
- [ ] Tall slider changes height on all chunks — no seam gaps
- [ ] Left Arm cybernetic toggles cleanly
- [ ] Right Arm cybernetic toggles cleanly
- [ ] Left Leg cybernetic toggles cleanly
- [ ] Right Leg cybernetic toggles cleanly
- [ ] Chest cybernetic toggles cleanly
- [ ] Head cybernetic toggles cleanly
- [ ] All cybernetics active simultaneously — no visual conflicts
- [ ] Hair dropdown cycles through all styles and bald
- [ ] Scar overlay fades in/out
- [ ] Resonance crack mask fades in/out
- [ ] Animation cycling works with all cybernetics and hair active
- [ ] 10-character stress test passes (random blend shapes, no seams, acceptable performance)

> **SUCCESS:** All checks pass. Character system is complete and ready for game integration.

---

# Final Checklist

## Base Meshes

- [ ] Male base mesh imports without errors
- [ ] Female base mesh imports without errors
- [ ] All 6 chunks visible and correctly positioned on each
- [ ] Idle, walk, run animations play correctly on both
- [ ] Fat blend shape works on all chunks (within cap)
- [ ] Tall blend shape works on all chunks (within cap)
- [ ] All 6 socket bones present and tracked
- [ ] No visible seams under normal lighting

## Cybernetic Pieces

- [ ] All 6 pieces import correctly
- [ ] Each attaches to correct socket without misalignment
- [ ] No visible gap when body chunk is hidden
- [ ] Each moves correctly with animations

## Hair Meshes

- [ ] All 6 hairstyles import correctly
- [ ] Each attaches to `neck_01_socket` and follows head
- [ ] Bald look is clean with no artifacts

## Character Viewer

- [ ] Camera orbits correctly
- [ ] Blend shape sliders work in real time
- [ ] All 6 cybernetic toggles work
- [ ] Hair dropdown cycles correctly
- [ ] Overlays blend correctly via shader
- [ ] 10-character stress test passes

## Blend Shape Cap Values

| Shape Key | Your Cap Value | Notes |
|-----------|---------------|-------|
| Fat | ___ | Maximum before distortion appears |
| Tall | ___ | Maximum before distortion appears |

---

**End of guide.**
