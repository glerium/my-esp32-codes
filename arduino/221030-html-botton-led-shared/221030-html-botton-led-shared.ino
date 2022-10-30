/*********
  Rui Santos
  Complete instructions at https://RandomNerdTutorials.com/esp32-cam-projects-ebook/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files.
  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*********/
// https://randomnerdtutorials.com/esp32-esp8266-input-data-html-form/
// 

#include "WiFi.h"
#include "esp_timer.h"
#include "img_converters.h"
#include "Arduino.h"
#include "soc/soc.h"           // Disable brownour problems
#include "soc/rtc_cntl_reg.h"  // Disable brownour problems
#include "driver/rtc_io.h"
#include <ESPAsyncWebServer.h>
#include <StringArray.h>
#include <FS.h>

// LED pin
const int white_led_pin = 32;
const int yellow_led_pin = 33;

// Set your access point network credentials
const char* ssid = "esp32-AP";
const char* password = "Wenzelin2004";

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

const char* PARAM_INPUT_1 = "white_light";
const char* PARAM_INPUT_2 = "yellow_light";

void toggle_light(int color);

const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML><html>
<head>
  <title>Mini-Car Controller</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { text-align:center; }
    .vert { margin-bottom: 10%; }
    .hori{ margin-bottom: 0%; }
  </style>
</head>
<body>
  <div align="center">
    <button type="button" name="white_light" id="white_light">White Light</button>
    <button type="button" name="yellow_light" id="yellow_light">Yellow Light</button>
  </div>
  <script>
    var xhttp = new XMLHttpRequest();
    var white_light_botton = document.getElementById('white_light');
    var yellow_light_botton = document.getElementById('yellow_light');
    white_light_botton.onclick = function() {
      xhttp.open("POST", "/toggle_white_light");
      xhttp.send();
      console.log('toggle_white_light');
    }
    yellow_light_botton.onclick = function() {
      xhttp.open("POST", "/toggle_yellow_light");
      xhttp.send();
      console.log('toggle_yellow_light');
    }
  </script>
</body>
</html>)rawliteral";

void setup() {
  // Serial port for debugging purposes
  Serial.begin(115200);

  WiFi.mode(WIFI_AP);
  if(!WiFi.softAPConfig(IPAddress(192, 168, 4, 1), IPAddress(192, 168, 4, 1), IPAddress(255, 255, 0, 0))){
      Serial.println("AP Config Failed");
  }
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  // Turn-off the 'brownout detector'
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);

  // set led pinmode
  pinMode(white_led_pin, OUTPUT);
  pinMode(yellow_led_pin, OUTPUT);

  digitalWrite(white_led_pin, HIGH);
  digitalWrite(yellow_led_pin, HIGH);

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/html", index_html);
  });
  server.on("/toggle_white_light", HTTP_POST, [](AsyncWebServerRequest * request) {
    toggle_light(1);
  });
  server.on("/toggle_yellow_light", HTTP_POST, [](AsyncWebServerRequest * request) {
    toggle_light(2);
  });
  // Start server
  server.begin();
}

void loop() {
  delay(1);
}

void toggle_light(int color) {
  if (color == 1) {
    bool state = digitalRead(white_led_pin);
    digitalWrite(white_led_pin, !state);
  }
  else if (color == 2) {
    bool state = digitalRead(yellow_led_pin);
    digitalWrite(yellow_led_pin, !state);
  }
}
