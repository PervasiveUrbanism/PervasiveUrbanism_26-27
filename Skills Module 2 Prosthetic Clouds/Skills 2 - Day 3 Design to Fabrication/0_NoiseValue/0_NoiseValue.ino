float value = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  value = noise();
  Serial.println(value);
}

float noise() {
  float r = random(-100, 100) / 100.0;  // random seed
  value = 0.99 * value + 0.1 * r;       // smoothing
  return value;
}