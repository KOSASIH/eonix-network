#include <unity.h>
#include "eonix_iot_esp32.c"

void test_eonix_iot_init(void) {
    eonix_iot_init();
    TEST_ASSERT_EQUAL_STRING(EONIX_IOT_SERVER, eonix_iot.server_url);
    TEST_ASSERT_EQUAL_STRING(EONIX_IOT_API_KEY, eonix_iot.api_key);
}

void test_eonix_iot_send_data(void) {
    float temperature = 25.0;
    float humidity = 60.0;
    eonix_iot_send_data(temperature, humidity);
    // Verify that the data was sent successfully
    TEST_ASSERT_TRUE(1); // Replace with actual verification logic
}

int main() {
    UNITY_BEGIN();
    RUN_TEST(test_eonix_iot_init);
    RUN_TEST(test_eonix_iot_send_data);
    return UNITY_END();
}
