import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import pickle
# %matplotlib inline
# %matplotlib qt

# Number of Corner in Chess
CN_in_Row = 6
CN_in_Col = 4
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CN_in_Col*CN_in_Row, 3), np.float32)
objp[:, :2] = np.mgrid[0:CN_in_Row, 0:CN_in_Col].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# Make a list of calibration images
libname = 'Nexus3'
filename = 'chess*'

images = glob.glob(libname+'/'+filename+'.jpg')
# Step through the list and search for chessboard corners
for idx, fname in enumerate(images):
    img = cv2.imread(fname)
    img = cv2.resize(img, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (CN_in_Row, CN_in_Col), None)

    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (CN_in_Row, CN_in_Col), corners, ret)
        #write_name = 'corners_found'+str(idx)+'.jpg'
        #cv2.imwrite(write_name, img)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Test undistortion on an image
img = cv2.imread(libname+'/chess1.jpg')
img = cv2.resize(img, (640, 480))
img_size = (img.shape[1], img.shape[0])

# Do camera calibration given object points and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)


dst = cv2.undistort(img, mtx, dist, None, mtx)
cv2.imwrite(libname+'/output.jpg',dst)

# Save the camera calibration result for later use
# Visualize undistortion
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=30)
ax2.imshow(dst)
ax2.set_title('Undistorted Image', fontsize=30)

print("retval:", ret)
print("cameraMatrix:\n",mtx)
print("distortionParams:\n",dist)
f = open(libname+'/result.txt','w')
f.write('retval:'+str(ret)+'\n\n')
f.write('cameraMatrix:\n'+str(mtx)+'\n\n')
f.write('distortionParams:\n'+str(dist))
f.close()