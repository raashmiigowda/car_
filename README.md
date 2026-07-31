# car_

# Automotive HDRI Rendering Pipeline

A Blender Python pipeline that places a fixed 3D car model into an HDR environment and generates a realistic render with environment-based lighting, reflections, and shadows.

## Overview

The pipeline:

* Imports a fixed `.glb` car model
* Loads an HDRI environment
* Uses Blender Cycles for realistic rendering
* Generates reflections and shadows based on the HDR lighting
* Saves the final rendered image

## Project Structure

```text
AutomotiveAI/

├── render.py
│
├── assets/
│   └── car.glb
│
├── environments/
│   └── environment.hdr
│
└── outputs/
    └── final_render.png
```

## Requirements

* Blender 4.x
* A `.glb` 3D car model
* A `.hdr` environment map

## Running the Pipeline

### Blender Scripting

1. Open Blender
2. Go to **Scripting**
3. Open `render.py`
4. Click **Run Script**

### Command Line

Run:

```bash
blender -b -P render.py
```

## Pipeline Flow

```text
car.glb
   |
   v
Blender Scene
   |
   +---- HDR Environment
   |
   +---- Cycles Lighting
   |
   +---- Shadow Catcher
   |
   v
final_render.png
```

## Features

* Fixed vehicle consistency
* HDRI-based lighting
* Automatic reflections
* Physically accurate shadows
* Automated Blender rendering
