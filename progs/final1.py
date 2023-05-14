import face_recognition
import numpy as np
import json

#load the json file 
with open('loaddate/file.json') as f:
    data= json.load(f)

# Define an empty list to store face encodings and names
encodings = []
names = []

# Load images and their corresponding names and generate encodings
image_files = list(data.keys())
names_list = list(data.values())

for idx, file in enumerate(image_files):
    # Load image
    image = face_recognition.load_image_file(file)

    # Generate face encodings
    encoding = face_recognition.face_encodings(image)[0]

    # Append encoding and name to their respective lists
    encodings.append(encoding)
    names.append(names_list[idx])

# Convert lists to numpy arrays
encodings = np.array(encodings)
names = np.array(names)

# Save the dataset
np.save("savedata/known_faces.npy", encodings)
np.save("savedata/known_names.npy", names)
print("Sucessfully Trained")
