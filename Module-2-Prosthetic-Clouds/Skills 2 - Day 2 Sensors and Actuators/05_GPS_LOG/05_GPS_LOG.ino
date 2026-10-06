#include <TinyGPS++.h>
#include <SPI.h>
#include <SD.h>

TinyGPSPlus gps;

// this is for the card
const int chipSelect = 4;

// this is for the gsr sensor
const int GSRPIN = A0;
int gsr_sensorValue = 0;
int gsr_average = 0;

// files and strings
File dataFile;
String filename = "Data.csv";
String Data = "";
String Header = "index \t lat \t long \t speed \t date \t time \t gsr";

// counter
int index = 0;

void setup() {

  Serial1.begin(9600);  //This opens up communications to the GPS

  Serial.begin(9600);      //This opens up communications to the Serial monitor in the Arduino IDE and sets the speed. This is basically the connection to the computer
  Serial.println(Header);  //and these are the values

  SD.begin(chipSelect);
  SD.remove(filename);
  File dataFile = SD.open(filename, FILE_WRITE);
  if (dataFile) {
    dataFile.println(Header);
    dataFile.close();
  }
}



void loop() {
  while (Serial1.available())  //While there is data coming from the GPS, do follwing...
  {
    gps.encode(Serial1.read());  //...read the signal, transform into an object called "gps"
  }

  if (gps.location.isUpdated())  //if this object has been updated, do the following
  {
    Data = "";
    // each reading has an index
    Data.concat(index);
    // This writes a line with the data coming from the gps
    Data.concat("\t");
    Data.concat(String(gps.location.lat(), 6));
    Data.concat("\t");
    Data.concat(String(gps.location.lng(), 6));
    Data.concat("\t");
    Data.concat(gps.speed.mph());
    Data.concat("\t");
    Data.concat(gps.date.value());
    Data.concat("\t");
    Data.concat(gps.time.value());

    // This reads the gsr sensor
    long gsr_sum = 0;
    for (int i = 0; i < 10; i++)  //Average the 10 measurements to remove the glitch
    {
      gsr_sensorValue = analogRead(GSRPIN);
      gsr_sum += gsr_sensorValue;
      delay(5);
    }
    gsr_average = gsr_sum / 10;
    Data.concat("\t");
    Data.concat(gsr_average);

    // and at the end of each reading cycle, it write the datapoint to the card
    dataFile = SD.open(filename, FILE_WRITE);
    if (dataFile) {
      dataFile.println(Data);
      dataFile.close();
      Serial.println(Data);
    }
    index = index + 1;
  }
}
