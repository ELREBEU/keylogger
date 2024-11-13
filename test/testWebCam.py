import cv2


camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
while True:
    ret, frame = camera.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('Camera',frame)

    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
out.release()
cv2.destroyAllWindows()