#include <SPI.h>
#include <SD.h>

const int chipSelect = 4;            // Seeed SD shield V4.0 uses D4 as CS
File dataFile;
const char* filename = "DATA.CSV";   // use const char* for SD library

String Data = "Entry Number: ";
int loopCount = 1;

void setup() {
  Serial.begin(9600);
  while (!Serial) { }  // optional, but nice when using Serial Monitor

  Serial.println("Initializing SD card...");

  pinMode(10, OUTPUT);              // hardware SS must be output

  if (!SD.begin(chipSelect)) {
    Serial.println("SD init failed.");
    while (1) { delay(10); }
  }
  Serial.println("SD init done.");

  SD.remove(filename);              // start with a clean file (optional)

  dataFile = SD.open(filename, FILE_WRITE);
  if (dataFile) {
    dataFile.println("first entry during setup.");
    dataFile.close();
    Serial.println("Wrote header line.");
  } else {
    Serial.println("Could not open file in setup.");
  }
}

void loop() {
  Data = "Entry Number: ";
  Data.concat(loopCount);

  dataFile = SD.open(filename, FILE_WRITE);
  if (dataFile) {
    dataFile.println(Data);
    dataFile.close();
    Serial.println("New line successfully written: " + Data);
  } else {
    Serial.println("Error opening file.");
  }

  loopCount++;
  delay(1000);
}
