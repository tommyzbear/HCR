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

