from pathlib import Path
from random import randrange

from peekingduck.pipeline.nodes.dabble import fps, bbox_to_btm_midpoint, zone_count
from peekingduck.pipeline.nodes.draw import bbox, legend, zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner
from src.custom_nodes.dabble import posebox

def generate_zones():
    top = 0
    bottom = 0.5
    left = 0
    right = 0.67
    randrange(0, 1, 0.1)
    return []

def main():
    posebox_node = posebox.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")

    visual_node = visual.Node(source=0)
    yolo_node = yolo.Node(detect=["person"])
    bbox_node = bbox.Node(show_labels=True)
    midpoint_node = bbox_to_btm_midpoint.Node()
    draw_zones_node = zones.Node()

    fps_node = fps.Node()
    zone_count_node = zone_count.Node(resolution = [1280, 720], zones=[[[0.2, 0], [0.5, 0], [0.5, 0.67], [0.2, 0.67]],
    [[0, 0], [0.5, 0], [0.5, 0.67], [0, 0.67]]])
    legend_node = legend.Node(show=["zone_count"])
    screen_node = screen.Node()

    media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "results"))

    runner = Runner(
        nodes=[
            visual_node,
            yolo_node,
            posebox_node,
            bbox_node,
            fps_node,
            midpoint_node,
            zone_count_node,
            draw_zones_node,
            legend_node,
            screen_node,
            media_writer_node,
        ]
    )
    runner.run()


if __name__ == "__main__":
    main()