import cv2
import pygame
import numpy as np

from queue_monitor import display_text, set_up_regions, draw_regions
from check_region import in_region

paths = ['video_for_demo.mp4', 'IMG_0441edited (online-video-cutter.com).mp4']
vidcap = cv2.VideoCapture(paths[0])
success,frame = vidcap.read()


camera_height = np.shape(frame)[0]
height=np.shape(frame)[0] + 80
width=np.shape(frame)[1]
frame_shape = [width, height]
score_thr = 0.3


RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Vision-based Queue Monitoring System")

surface = pygame.display.set_mode(frame_shape)

from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv

config_file = 'yolov3_d53_fp16_mstrain-608_273e_coco.py'
checkpoint_file = 'yolov3_d53_fp16_mstrain-608_273e_coco_20210517_213542-4bc34944.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')

################################### stage 1 ##################################
# regions = set_up_regions(surface)
set_region_done = False

################################### stage 2 ##################################
current = 0
while True:
    pygame.display.update() 
    surface.fill(BLACK)
    display_text(surface, "Queue Monitoring System", (20, height-70))

    # frame = cv2.resize(frame, frame_shape, interpolation = cv2.INTER_AREA)
    
    if set_region_done:
        person_bbox = inference_detector(model, frame)[0]

        frame = model.show_result(frame,
                    np.array([person_bbox]),
                    score_thr=score_thr,
                    bbox_color=(72, 101, 241),
                    text_color=(72, 101, 241),
                    mask_color=None,
                    thickness=2,
                    font_size=13,
                    win_name='',
                    show=False,
                    wait_time=0,
                    out_file=None)

    # #for some reasons the frames appeared inverted
    frame = np.fliplr(frame)
    frame = np.rot90(frame)

    # # The video uses BGR colors and PyGame needs RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    surf = pygame.surfarray.make_surface(frame)
    
    if set_region_done:
    # uncomment these lines to get image coordinates 
    # be careful with pygame coordinates system
        
        points = []
        count = {k: 0 for k, v in regions.items()}
        count[0] = 0
        for bbox in list(person_bbox):
            if bbox[4] > score_thr:
                point = ((bbox[0] + bbox[2])/2), (bbox[1] + 0.5*bbox[3])/1.5
                points.append(point)
                count[in_region(point, regions)] += 1
        del count[0]
        draw_regions(regions, surf, count)
    
    surface.blit(surf, (0,0))
    pygame.display.flip()

    if not set_region_done:
        regions = set_up_regions(surface, camera_height)
        set_region_done = True

    success,frame = vidcap.read()