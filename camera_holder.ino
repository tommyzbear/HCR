  #if defined(ARDUINO) && ARDUINO >= 100
    #include "Arduino.h"
  #else
    #include <WProgram.h>
  #endif
  
  #include <Servo.h> 
  #include <ros.h>
  #include <std_msgs/UInt16.h>
  
  ros::NodeHandle  nh;
  
  Servo servo;
  int updown = 0;
  int angle;
  
  void cmd_cb( const std_msgs::UInt16& cmd_msg){
    

    digitalWrite(13, HIGH-digitalRead(13));  //toggle led
    
 
    if (cmd_msg.data>180){  
      updown = (cmd_msg.data-cmd_msg.data%180)/180;
      angle = cmd_msg.data%180;
    }  

      servo.write(angle); //set servo angle, should be from 0-180  
           
    if(updown == 0){
      analogWrite(7,0); 
      analogWrite(8,0);
    } 
    
    if(updown == 1){
      analogWrite(7,255); 
      analogWrite(8,0);
    } 
    
    if(updown == 2){
      analogWrite(7,0); 
      analogWrite(8,255);      
    } 
    
  }
  
  
  ros::Subscriber<std_msgs::UInt16> sub("servo", cmd_cb);

  void setup(){
    pinMode(13, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);  
    nh.initNode();
    nh.subscribe(sub);
    
    
    servo.attach(9); //attach it to pin 9
  }
  
  void loop(){
  nh.spinOnce();
  delay(1);
}
