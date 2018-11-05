# Human-Centered Robotics

4th Year Imperial College EEE coursework

## Installing Drivers and Framework for Kinect

### OpenKinect

Install all necessary dependencies for OpenKinect

```
sudo apt-get install git cmake build-essential libusb-1.0-0-dev freeglut3-dev libxmu-dev libxi-dev g++ python openjdk-8-jdk doxygen graphviz mono-complete
```

Clone ```libfreenect```repository from OpenKinect

```
mkdir Kinect
cd Kinect
git clone https://github.com/OpenKinect/libfreenect.git
cd libfreenect
mkdir build
cd build
cmake -L ..
make
sudo make install
```

Add Kinect for Windows udev rules so you'll no longer need to run your apps as root

```
sudo cp ~Kinect/libfreenect/platform/linux/udev/51-kinect.rules /etc/udev/rules.d/
```

### OpenNI

Download OpenNi-Bin-Dev-Linux-x64-v1.5.7.10.tar

```cd OpenNI-Bin-Dev-Linux-x64-v1.5.7.10```
```sudo ./install.sh```

### Sensor

Download Sensor-Bin-Linux-x64-v5.1.2.1.tar.bz2

```cd Sensor-Bin-Linux-x64-v5.1.2.1```
```sudo ./install.sh```

### NITE

Download NITE-Bin-Dev-Linux-x64-v1.5.2.23.tar

```cd NITE-Bin-Dev-Linux-x64-v1.5.2.23```
```sudo ./install.sh```


https://www.20papercups.net/programming/kinect-on-ubuntu-with-openni/comment-page-1/
