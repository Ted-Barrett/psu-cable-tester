#include <Wire.h>
#include <Adafruit_SH110X.h>
#include <Adafruit_GFX.h>

#define SCREEN_WIDTH 64   // OLED display width, in pixels
#define SCREEN_HEIGHT 128 // OLED display height, in pixels
#define OLED_RESET -1     // can set an oled reset pin if desired
#define IIC_ADDRESS 0x3C  // IIC Address of display
Adafruit_SH1107 display = Adafruit_SH1107(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define NUM_OPTIONS 5
String menu_options[] = {"Corsair", "Coolermaster", "EVGA", "MSI", "Back"};

void setup()   {

  Serial.begin(9600);

  delay(250); // wait for the OLED to power up

  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.

  display.begin(IIC_ADDRESS, true); // Address 0x3D default
  display.setRotation(3);

  display.setTextSize(1);
  display.setTextColor(1);
 
  display.clearDisplay();
  display.display();
}

void loop() {
  for (int i = 0; i < NUM_OPTIONS; i++) {
    display.setCursor(0,0);
    display.clearDisplay();
    display.println("PSU Brand:");
    for (int j = 0; j < NUM_OPTIONS; j++) {
      if (j == i) {
        display.print(">");
      } else {
        display.print(" ");
      }
      display.println(menu_options[j]);
    }
    display.display();
    delay(500);
  }
}
