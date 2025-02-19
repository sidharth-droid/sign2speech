import os
import pickle
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = "./data"

if not os.path.exists(DATA_DIR):
    print(f"Error: Directory '{DATA_DIR}' does not exist.")
    exit()

data = []
labels = []
FEATURES = 84  # 42 for each hand (x, y coordinates)

for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):
        continue

    for img_path in os.listdir(dir_path):
        data_aux = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(dir_path, img_path))
        print(img_path)
        if img is None:
            print(f"Error: Failed to load image {img_path}")
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        if results.multi_hand_landmarks is None:
            print(f"Warning: No hands detected in {img_path}")
            continue

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        # Ensure 84 features (42 per hand)
        while len(data_aux) < FEATURES:
            data_aux.append(0.0)

        data.append(data_aux)
        labels.append(dir_)

with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
print("Data successfully saved to 'data.pickle'.")














# import os, pickle, cv2
# import mediapipe as mp


# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=True,min_detection_confidence=0.3)

# DATA_DIR = "./data"

# if not os.path.exists(DATA_DIR):
#     print(f"Error: Directory '{DATA_DIR}' does not exist.")
#     exit()

# data = []
# labels = []

# for dir_ in os.listdir(DATA_DIR):
#     dir_path = os.path.join(DATA_DIR, dir_)
#     if not os.path.isdir(dir_path):
#         print(f"Skipping non-directory file: {dir_}")
#         continue

#     for img_path in os.listdir(dir_path):
#         data_aux = []
#         x_ = []
#         y_ = []

#         img = cv2.imread(os.path.join(dir_path, img_path))
#         if img is None:
#             print(f"Error: Failed to load image {img_path}")
#             continue
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = hands.process(img_rgb)
#         if results.multi_hand_landmarks is None:
#             print(f"Warning: No hands detected in {img_path}")
#             continue

#         for hand_landmarks in results.multi_hand_landmarks:
#             for i in range(len(hand_landmarks.landmark)):
#                 x = hand_landmarks.landmark[i].x
#                 y = hand_landmarks.landmark[i].y
#                 x_.append(x)
#                 y_.append(y)
#             for i in range(len(hand_landmarks.landmark)):
#                 x = hand_landmarks.landmark[i].x
#                 y = hand_landmarks.landmark[i].y
#                 data_aux.append(x - min(x_))
#                 data_aux.append(y - min(y_))
#         data.append(data_aux)
#         labels.append(dir_)

# with open('data.pickle', 'wb') as f:
#     pickle.dump({'data': data, 'labels': labels}, f)
# print("Data successfully saved to 'data.pickle'.")




