---
title: "DepthImage"
---
<!-- DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/docs/website.rs -->

A depth image, i.e. as captured by a depth camera.

Each pixel corresponds to a depth value in units specified by [`components.DepthMeter`](https://rerun.io/docs/reference/types/components/depth_meter).

## Fields
### Required
* `buffer`: [`ImageBuffer`](../components/image_buffer.md)
* `format`: [`ImageFormat`](../components/image_format.md)

### Optional
* `meter`: [`DepthMeter`](../components/depth_meter.md)
* `colormap`: [`Colormap`](../components/colormap.md)
* `depth_range`: [`ValueRange`](../components/value_range.md)
* `point_fill_ratio`: [`FillRatio`](../components/fill_ratio.md)
* `draw_order`: [`DrawOrder`](../components/draw_order.md)


## Can be shown in
* [Spatial2DView](../views/spatial2d_view.md)
* [Spatial3DView](../views/spatial3d_view.md) (if logged under a projection)
* [DataframeView](../views/dataframe_view.md)

## API reference links
 * 🌊 [C++ API docs for `DepthImage`](https://ref.rerun.io/docs/cpp/stable/structrerun_1_1archetypes_1_1DepthImage.html)
 * 🐍 [Python API docs for `DepthImage`](https://ref.rerun.io/docs/python/stable/common/archetypes#rerun.archetypes.DepthImage)
 * 🦀 [Rust API docs for `DepthImage`](https://docs.rs/rerun/latest/rerun/archetypes/struct.DepthImage.html)

## Examples

### Simple example

snippet: archetypes/depth_image_simple

<picture data-inline-viewer="snippets/depth_image_simple">
  <source media="(max-width: 480px)" srcset="https://static.rerun.io/depth_image_simple/77a6fa4f938a742bdc7c5350f668c4f31eed4d01/480w.png">
  <source media="(max-width: 768px)" srcset="https://static.rerun.io/depth_image_simple/77a6fa4f938a742bdc7c5350f668c4f31eed4d01/768w.png">
  <source media="(max-width: 1024px)" srcset="https://static.rerun.io/depth_image_simple/77a6fa4f938a742bdc7c5350f668c4f31eed4d01/1024w.png">
  <source media="(max-width: 1200px)" srcset="https://static.rerun.io/depth_image_simple/77a6fa4f938a742bdc7c5350f668c4f31eed4d01/1200w.png">
  <img src="https://static.rerun.io/depth_image_simple/77a6fa4f938a742bdc7c5350f668c4f31eed4d01/full.png">
</picture>

### Depth to 3D example

snippet: archetypes/depth_image_3d

<picture data-inline-viewer="snippets/depth_image_3d">
  <source media="(max-width: 480px)" srcset="https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/480w.png">
  <source media="(max-width: 768px)" srcset="https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/768w.png">
  <source media="(max-width: 1024px)" srcset="https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/1024w.png">
  <source media="(max-width: 1200px)" srcset="https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/1200w.png">
  <img src="https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/full.png">
</picture>

