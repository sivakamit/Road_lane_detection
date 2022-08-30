import cv2
import numpy as np


def cannyEdges(image):
    edged = cv2.Canny(image, 50, 150)
    return edged


def getROI(image):
    height = image.shape[0]
    width = image.shape[1]
    # Defining Triangular ROI: The values will change as per camera mounts
    triangle= np.array([[(200, height), (1100, height), (550, 250)]])
    # creating black image same as that of input image
    black_image = np.zeros_like(image)
    # Put the Triangular shape on top of our Black image to create a mask
    mask = cv2.fillPoly(black_image, triangle, 255)
    # applying mask on original image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def getLines(image):
    lines = cv2.HoughLinesP(image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    return lines


# display lines over a image
def displayLines(image, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)  # converting to 1d array []
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return image


def getCoordsFromParameters(image, line_parameters):
    slope = line_parameters[0]
    intercept = line_parameters[1]
    y1 = image.shape[0]  # since line will always start from bottom of image
    y2 = int(y1 * (3.4 / 5))  # some random point at 3/5
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


# Average all the left and right lines found for a lane and retuns single left and right line for the the lane
def getSmoothLines(image, lines):
    left_fit = []  # will hold m,c parameters for left side lines
    right_fit = []  # will hold m,c parameters for right side lines

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]

        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)

    left_line = getCoordsFromParameters(image, left_fit_average)
    right_line = getCoordsFromParameters(image, right_fit_average)
    return np.array([left_line, right_line])


# work with test_video, test_video1, test_video2
videoFeed = cv2.VideoCapture("test_video1.mp4")

try:
    # print("video feed present")
    while videoFeed.isOpened():
        # print("video feed opened")
        (status, image) = videoFeed.read()
        # print(status)
        edged_image = cannyEdges(image)
        roi_image = getROI(edged_image)
        lines = getLines(roi_image)
        # print(lines)
        # image_with_lines = displayLines(image, lines)
        smooth_lines = getSmoothLines(image, lines)
        image_with_smooth_lines = displayLines(image, smooth_lines)


        cv2.imshow("Output", image_with_smooth_lines)
        k = cv2.waitKey(1)
        if k == 27:
            break
except:
    print("Error")
    pass