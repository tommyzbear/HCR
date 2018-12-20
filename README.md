# Human-Centered Robotics

4th Year Imperial College EEE coursework

Video: https://youtu.be/wTMhObNkLsI

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

```
cd OpenNI-Bin-Dev-Linux-x64-v1.5.7.10
sudo ./install.sh
```

### Sensor

Download Sensor-Bin-Linux-x64-v5.1.2.1.tar.bz2

```
cd Sensor-Bin-Linux-x64-v5.1.2.1
sudo ./install.sh
```

### NITE

Download NITE-Bin-Dev-Linux-x64-v1.5.2.23.tar

```
cd NITE-Bin-Dev-Linux-x64-v1.5.2.23
sudo ./install.sh
```

### Or follow the instruction below

https://www.20papercups.net/programming/kinect-on-ubuntu-with-openni/comment-page-1/

### If the driver is unaccesscible, try the following

Make sure your user belongs to the ```video``` and ```audio``` groups

```
sudo adduser $USER video
sudo adduser $USER audio
```

Check if devices are listed in usb ports

```sudo lsusb -v | grep Microsoft```

If not present, run 

```echo -1 | sudo tee -a /sys/module/usbcore/parameters/autosuspend```

then reconnect the devices

Also check 

```sudo nano /etc/udev/rules.d/55-primesense-usb.rules```

Make sure your product is listed below, e.g.

```
# PrimeSense Devices
SUBSYSTEM=="usb", ATTR{idProduct}=="0200", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="0300", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="0400", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="0500", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="0600", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="0601", ATTR{idVendor}=="1d27", MODE:="0666", OWNER:="root", GROUP:="video"

#--avin mod--
# Kinect
SUBSYSTEM=="usb", ATTR{idProduct}=="02ae", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="02ad", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="audio"
SUBSYSTEM=="usb", ATTR{idProduct}=="02b0", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="02be", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="audio"
SUBSYSTEM=="usb", ATTR{idProduct}=="02bf", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="video"
SUBSYSTEM=="usb", ATTR{idProduct}=="02c3", ATTR{idVendor}=="045e", MODE:="0666", OWNER:="root", GROUP:="audio"
```

Add read/write accessibilities to usb port:

```sudo chmod a+rw /dev/bus/usb//```

Then restart

## Installing RosAria driver for P3AT

Open terminal in same directory as ```libaria_2.9.4+ubuntu16_amd64.deb```

```dpkg -i libaria_2.9.4+ubuntu16_amd64.deb```

Then go through ```P3ATs_QuickStartGuide.txt```

## Setting up Gazebo

```sudo apt install gazebo7```

OpenGL support can be disabled by setting the environment variable ```SVGA_VGPU10=0```.

```export SVGA_VGPU10=0```

Gazebo starts now and runs compared to the not 3D accelerated way pretty smooth on a T460p if the resolution of the VM guest system is not too high (<< 4K).

To make the change permanent:
```echo "export SVGA_VGPU10=0" >> ~/.bashrc```

# Running the files
Launch ```av_nav.launch``` with ```roslaunch``` will start running the nodes for RosAria, navigation, Openni for Kinect and skeleton_markers
Video filming components ```audio_control video_control video_combine```will need to be ran. 
Gesture recognition node is located in ```gesture```package
Voice command recognition node can be ran by ```rosrun voice_recognition main.py```
Kinect platform is powered by rosserial, please ensure to install rosserial package. Arduino script is the ```camera_holder.ino```.
