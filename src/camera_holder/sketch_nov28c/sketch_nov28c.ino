   #include <ros.h>
   #include <std_msgs/Empty.h>
   #include <std_msgs/UInt16.h>
   
   ros::NodeHandle nh;
   
  void camera_cb( const std_msgs::UInt16& cmd_msg){
    
    analogWrite(7,0); 
    analogWrite(8,0);
    digitalWrite(13, HIGH-digitalRead(13));  //toggle led   
    
    if(cmd_msg.data == 181){
      analogWrite(7,255); 
      analogWrite(8,0);
         digitalWrite(13, HIGH-digitalRead(13));  //toggle led   
    } if(cmd_msg.data == 182){
        analogWrite(7,0); 
        analogWrite(8,255);  
        digitalWrite(13, HIGH-digitalRead(13));  //toggle led  tt    
      } 
  }
   
  ros::Subscriber<std_msgs::UInt16> sub("dc", camera_cb);
   
   void setup()
   {
     pinMode(13, OUTPUT);
     nh.initNode();
     nh.subscribe(sub);
   }
   
   void loop()
   {
     nh.spinOnce();
     delay(1);
   }
