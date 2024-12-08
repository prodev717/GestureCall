import os
import cv2
import mediapipe as mp
import numpy as np

import pickle

mph = mp.solutions.hands
hands = mph.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mpd = mp.solutions.drawing_utils


def calc_angle(a, b, c):
    ba = np.array(a) - np.array(b)
    bc = np.array(c) - np.array(b)
    cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    return np.degrees(angle)
def get_angles(lmks):
    angs = []
    pairs = [
        (0, 1, 2), (1, 2, 3), (2, 3, 4),
        (0, 5, 6), (5, 6, 7), (6, 7, 8),
        (0, 9, 10), (9, 10, 11), (10, 11, 12),
        (0, 13, 14), (13, 14, 15), (14, 15, 16),
        (0, 17, 18), (17, 18, 19), (18, 19, 20)
    ]
    for (i, j, k) in pairs:
        angs.append(calc_angle(lmks[i], lmks[j], lmks[k]))
    return angs

def comp_angles(a1, a2, marg=9.5, th=0.8):
    match = [abs(x1 - x2) <= marg for x1, x2 in zip(a1, a2)]
    ratio = sum(match) / len(match)
    return ratio >= th
# database_path = "database"
# img_text = {}

# for folder_name in os.listdir(database_path):
#     folder_path = os.path.join(database_path, folder_name)
#     if os.path.isdir(folder_path):
#         for file_name in os.listdir(folder_path):
#             file_ext = file_name.split('.')[-1].lower()
#             if file_ext in ['jpg', 'jpeg', 'png', 'webp']:
#                 img_path = os.path.join(folder_path, file_name)
#                 img_text[img_path] = folder_name.capitalize() 

# buffer_sent = []
# ref_data = {}
# for path, text in img_text.items():
#     img = cv2.imread(path)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     res = hands.process(img_rgb)
    
#     if res.multi_hand_landmarks:
#         lmks = [(lm.x, lm.y, lm.z) for lm in res.multi_hand_landmarks[0].landmark]
#         angs = get_angles(lmks)
#         ref_data[path] = angs
#         print(f"angles for {text} - {angs}")
#     else:
#         print(f"Cannot detect angles in this image: {path}")

ref_data = {}
with open("data.pkl","rb") as f:
    ref_data = pickle.load(f)

def convert(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(img_rgb)
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    if res.multi_hand_landmarks and res.multi_handedness:
        for idx, hand_lmks in enumerate(res.multi_hand_landmarks):
            hand_type = res.multi_handedness[idx].classification[0].label
            mpd.draw_landmarks(img_bgr, hand_lmks, mph.HAND_CONNECTIONS)
            lmks = [(lm.x, lm.y, lm.z) for lm in hand_lmks.landmark]
            angs = get_angles(lmks)
            
            matched = False
            for path, ref_angs in ref_data.items():
                if comp_angles(angs, ref_angs):
                    disp_text = path.split("\\")[1] #img_text[path]
                    if hand_type == "Left":
                        cv2.putText(img_bgr, disp_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    elif hand_type == "Right":
                        cv2.putText(img_bgr, disp_text, (img_bgr.shape[1] - 250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    matched = True
                    break
            if not matched:
                if hand_type == "Left":
                    cv2.putText(img_bgr, "No match seen", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                elif hand_type == "Right":
                    cv2.putText(img_bgr, "No match seen", (img_bgr.shape[1] - 250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    return img_bgr
    

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, img = cap.read()
#     if not success:
#         break
#     img_bgr = convert(img)
#     cv2.imshow('ISL Detection', img_bgr)
#     if cv2.waitKey(5) & 0xFF == ord('m'):
#         break

# cap.release()
# cv2.destroyAllWindows()