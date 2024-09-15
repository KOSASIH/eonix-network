#include <ArduinoUnit.h>
#include "eonix_iot_arduino.ino"

void testEonixIotInit() {
  eonixIotInit();
  assertEqual(EONIX_IOT_SERVER, eonixIotServerUrl);
  assertEqual(EONIX_IOT_API_KEY, eonixIotApiKey);
}

void testEonixIotSendData() {
  float temperature = 25.0;
  float humidity = 60.0;
  eonixIotSendData(temperature, humidity);
  // Verify that the data was sent successfully
  assertTrue(true);  // Replace with actual verification logic
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  Test::run();
}
