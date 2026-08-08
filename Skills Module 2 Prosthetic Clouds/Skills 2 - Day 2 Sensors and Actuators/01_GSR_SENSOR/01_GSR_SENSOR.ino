const int GSRPIN = A0;
int gsr_sensorValue = 0;
int gsr_average = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {

  long gsr_sum = 0;
  for (int i = 0; i < 50; i++)    //Average the 10 measurements to remove the glitch
  { gsr_sensorValue = analogRead(GSRPIN);
    gsr_sum += gsr_sensorValue;
    delay(5);
  }
  gsr_average = gsr_sum / 50;

  Serial.println(gsr_average);
}
