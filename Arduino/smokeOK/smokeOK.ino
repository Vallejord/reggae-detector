// Define the analog pin connected to the MQ2 sensor
const int smokeSensorPin = A0;
// Define the threshold for smoke detection
const int smokeThreshold = 250; // Adjust as needed

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the analog value from the smoke sensor
  int sensorValue = analogRead(smokeSensorPin);

  // Print the sensor value to the serial monitor
  Serial.print("Smoke Sensor Value: ");
  Serial.println(sensorValue);

  // Check if smoke is detected
  if (sensorValue > smokeThreshold) {
    Serial.println("Smoke detected!");
    // Send a signal to the PC to play the MP3 file
    Serial.println("PLAY_MP3");
  } else {
    Serial.println("No smoke detected.");
  }

  // Wait for a moment before taking another reading
  delay(1000);
}
