#include <TinyGPS++.h>

TinyGPSPlus gps;

String Data = "";

void setup() {

  Serial1.begin(9600);//This opens up communications to the GPS

  Serial.begin(9600);//This opens up communications to the Serial monitor in the Arduino IDE and sets the speed. This is basically the connection to the computer
  Serial.println("GPS Start\n**************************");//Just show to the monitor that the sketch has started
  Serial.println("lat \t long \t speed \t date \t time");//and these are the values

}

void loop()
{
  while (Serial1.available()) //While there is data coming from the GPS, do follwing...
  {
    gps.encode(Serial1.read());//...read the signal, transform into an object called "gps"
  }

  if (gps.location.isUpdated()) //if this object has been updated, do the following
  {Data = "";
    Data.concat(String(gps.location.lat(), 6));
    Data.concat(",");
    Data.concat(String(gps.location.lng(), 6));
    Data.concat(",");
    Data.concat(gps.speed.mph());
    Data.concat(",");
    Data.concat(gps.date.value());
    Data.concat(",");
    Data.concat(gps.time.value());
    Serial.println(Data);
  }
}
