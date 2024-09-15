#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define EONIX_IOT_SERVER "https://eonix-iot-server.com/api/v1"
#define EONIX_IOT_API_KEY "YOUR_API_KEY_HERE"
#define WIFI_SSID "YOUR_WIFI_SSID_HERE"
#define WIFI_PASSWORD "YOUR_WIFI_PASSWORD_HERE"

WiFiClient wifiClient;
HTTPClient http;

void setup() {
  Serial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println("Initializing Eonix IoT...");
  eonixIotInit();
}

void loop() {
  float temperature = 25.0; // Replace with actual temperature sensor data
  float humidity = 60.0; // Replace with actual humidity sensor data
  eonixIotSendData(temperature, humidity);
  delay(10000);
}

void eonixIotInit() {
  http.begin(EONIX_IOT_SERVER);
  http.addHeader("Authorization", "Bearer " EONIX_IOT_API_KEY);
}

void eonixIotSendData(float temperature, float humidity) {
  DynamicJsonDocument jsonDoc(2048);
  jsonDoc["temperature"] = temperature;
  jsonDoc["humidity"] = humidity;
  String jsonString;
  jsonDoc.printTo(jsonString);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(jsonString);
  if (httpResponseCode > 0) {
    Serial.println("Data sent successfully!");
  } else {
    Serial.println("Error sending data:");
    Serial.println(http.errorString(httpResponseCode));
  }
}
