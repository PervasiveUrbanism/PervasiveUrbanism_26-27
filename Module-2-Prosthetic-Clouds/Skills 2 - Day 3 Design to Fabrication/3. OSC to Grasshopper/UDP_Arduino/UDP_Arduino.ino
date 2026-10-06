#include <WiFiS3.h>
#include <WiFiUdp.h>


#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
const char* ssid = SECRET_SSID;  // your network SSID (name)
const char* pass = SECRET_PASS;  // your network password (use for WPA, or use as key for WEP)


// UDP settings
const unsigned int localPort = 8000;         // Arduino listens here (not really needed, but OK)
const IPAddress remoteIp(192, 168, 1, 196);  // receiver
const unsigned int remotePort = 8050;        // receiver port

WiFiUDP udp;
float value = 0.0;  // smoothed random value

void setup() {
  Serial.begin(9600);
  while (!Serial) {}  // wait for Serial on native USB boards

  // Check WiFi module
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("No WiFi module found");
    while (true) {}
  }

  // Connect to WiFi
  Serial.print("Connecting to ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    Serial.println("Trying again...");
    delay(2000);
  }

  Serial.print("Connected. IP: ");
  Serial.println(WiFi.localIP());

  // Start UDP
  udp.begin(localPort);
}

void loop() {
  // Simple "noise": smoothed random value
  float r = random(-100, 101) / 100.0;  // -1.00 to +1.00
  value = 0.99 * value + 0.1 * r;       // smooth it a bit

  // Show in Serial Monitor
  Serial.println(value);

  // Send via UDP
  udp.beginPacket(remoteIp, remotePort);
  udp.print(value);  // send as text
  udp.endPacket();

  delay(50);  // send about 20 times per second
}
