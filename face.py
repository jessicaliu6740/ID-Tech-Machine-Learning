import jetson.inference
import jetson.utils

net = jetson.inference.detectNet(argv=['--model=models/face2/ssd-mobilenet.onnx', '--labels=models/face2/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'], threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img, overlay='none')

	for detection in detections:
		for y in range(int(detection.Top), int(detection.Bottom)):
			for x in range(int(detection.Left), int(detection.Right)):
				img[y,x] = (0,0,0)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
