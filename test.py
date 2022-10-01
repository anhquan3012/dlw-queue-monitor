import cv2
import pygame
import numpy as np

from queue_monitor import set_up_regions
from check_region import in_region

height=700
width=1000
frame_shape = [width, height]
score_thr = 0.5

RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)

pygame.init()
pygame.display.set_caption("Vision-based Queue Monitoring System")
surface = pygame.display.set_mode(frame_shape)
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print("fps:", fps)
cap.set(cv2.CAP_PROP_FPS, 5)

# from mmdet.apis import init_detector, inference_detector, show_result_pyplot
# import mmcv

config_file = 'yolov3_mobilenetv2_320_300e_coco.py'
checkpoint_file = 'yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth'

# model = init_detector(config_file, checkpoint_file, device='cuda:0')

################################### stage 1 ##################################
regions = set_up_regions()


################################### stage 2 ##################################
while True:
    surface.fill([0,0,0])

    success, frame = cap.read()
    if not success:
        break

    person_bbox = inference_detector(model, frame)[0]

    # frame = model.show_result(frame,
    #             np.array([person_bbox]),
    #             score_thr=score_thr,
    #             bbox_color=(72, 101, 241),
    #             text_color=(72, 101, 241),
    #             mask_color=None,
    #             thickness=2,
    #             font_size=13,
    #             win_name='',
    #             show=False,
    #             wait_time=0,
    #             out_file=None)

    # #for some reasons the frames appeared inverted
    frame = np.fliplr(frame)
    frame = np.rot90(frame)

    # bbox = list(inference_detector(model, frame)[0])

    # # The video uses BGR colors and PyGame needs RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    surf = pygame.surfarray.make_surface(frame)
    

    # uncomment these lines to get image coordinates 
    # be careful with pygame coordinates system
    points = []
    count = {k: 0 for k, v in regions.items()}
    count[0] = 0
    for bbox in list(person_bbox):
        if bbox[4] > score_thr:
            #topleft = (bbox[0], bbox[1])
            #topright = (bbox[2], bbox[1])
            #bottomleft = (bbox[0], bbox[3])
            #bottomright = (bbox[2], bbox[3])
            point = ((bbox[0] + bbox[2])/2), (bbox[1] + bbox[3])/2
            points.append(point)
            count[in_region(point, regions)] += 1
    del count[0]
            
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            background_color = RED
            surface.fill(background_color)
            pygame.display.update
            end_time = self.time()
            print(count)

    # Show the PyGame surface!
    surface.blit(surf, (0,0))
    pygame.display.flip()
