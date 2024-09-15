#include <stdio.h>
#include <string.h>
#include <esp_wifi.h>
#include <esp_http_client.h>
#include <eonix_iot.h>

#define EONIX_IOT_SERVER "https://eonix-iot-server.com/api/v1"
#define EONIX_IOT_API_KEY "YOUR_API_KEY_HERE"

eonix_iot_t eonix_iot;

void eonix_iot_init(void) {
    eonix_iot.server_url = EONIX_IOT_SERVER;
    eonix_iot.api_key = EONIX_IOT_API_KEY;
    eonix_iot_init_wifi();
}

void eonix_iot_init_wifi(void) {
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_start());
}

void eonix_iot_send_data(float temperature, float humidity) {
    char json_data[256];
    sprintf(json_data, "{\"temperature\": %f, \"humidity\": %f}", temperature, humidity);
    esp_http_client_config_t config = {
        .url = EONIX_IOT_SERVER,
        .method = HTTP_METHOD_POST,
        .event_handler = eonix_iot_event_handler,
    };
    esp_http_client_handle_t client = esp_http_client_init(&config);
    esp_http_client_set_header(client, "Authorization", "Bearer " EONIX_IOT_API_KEY);
    esp_http_client_set_post_field(client, json_data, strlen(json_data));
    esp_http_client_perform(client);
}

void eonix_iot_event_handler(esp_http_client_event_t *evt) {
    switch (evt->event_id) {
        case HTTP_EVENT_ON_DATA:
            printf("Received data: %.*s\n", evt->data_len, evt->data);
            break;
        case HTTP_EVENT_ON_FINISH:
            printf("Request finished\n");
            break;
        default:
            break;
    }
}

int main() {
    eonix_iot_init();
    while (1) {
        float temperature = 25.0; // Replace with actual temperature sensor data
        float humidity = 60.0; // Replace with actual humidity sensor data
        eonix_iot_send_data(temperature, humidity);
        vTaskDelay(10000 / portTICK_PERIOD_MS);
    }
    return 0;
}
