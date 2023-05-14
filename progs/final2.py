import cv2
import face_recognition
import numpy as np

# Load the dataset
encodings = np.load("savedata/known_faces.npy")
names = np.load("savedata/known_names.npy")

# Access the default camera
cap = cv2.VideoCapture(0)

# Initialize an empty set to keep track of people who have entered the frame
people_seen = set()

# Loop over frames from the video stream
while True:
    # Capture the frame from the camera
    ret, frame = cap.read()

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in the current frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for any of the known persons
        matches = face_recognition.compare_faces(encodings, face_encoding)
        name = "Unknown"

        # If there's a match, set the person's name
        if True in matches:
            match_index = np.argmax(matches)
            name = names[match_index]
            
            # If the person is not already in the set of people seen, add them and print their name
            if name not in people_seen:
                people_seen.add(name)
                print(name)

        # Draw a box around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame on the screen
    cv2.imshow('Camera Feed', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save the list of people seen to a numpy array
people_seen_array = np.array(list(people_seen))
np.save("savedata/people_seen.npy", people_seen_array)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
