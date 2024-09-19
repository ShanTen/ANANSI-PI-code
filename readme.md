# ANANSI Pi Code

## What is ANANSI

ANANSI is a hexapod designed for search and rescue operations powered by the ST-Discovery-L475E-IOT01A designed and presented for [AICTE Inventor's Challenge](https://community.arm.com/the-inventors-challenge-2024).

## What is this code?

This is the code that that resides on a headless raspberry pi zero (w). Which is used to transmit to the [electron client](https://github.com/shanten/ANANSI-Electron-Client`).

## Data Transmitted 

1. Camera Stream (from pi camera) - HTTP Server  
2. LiDAR (ydlidar X2) Information ([angle, direction] from LiDAR) - UDP Stream  

The YDlidarX2 driver is from [here](https://github.com/smlaage/YDLidarX2).