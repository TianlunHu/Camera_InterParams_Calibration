# Camera_InterParams_Calibration  

Camera Calibration for intrinsic Parameters.  

This code is used to obtain the intrinsic parameters of camera, such as:  

  1) Principle Distance  
  2) Principle Point  
  3) Aspect Ratio and Shearing Factor    
  4) Distortion Parameters  

  As Format Camera Matrix:    
  
  [ principle distance in X,       shearing Factor,     Coordinate of Principle Point in X ]  
  [           0            ,   principle distance in Y, Coordinate of Principle Point in Y ]  
  [           0            ,             0            ,                  1                 ]  
  
  
# Usage

(1) Prepare a Chess Marker with proper scale, then take a series of images of it from different angle and distance. (10 images at least)  
(2) The number of corners of chess marker in Cols and Rows should be adjusted manually in code, in line(10, 11)  
(3) The Result will be returned and stored in a txt file
