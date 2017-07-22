#include <TimerOne.h>

#define LED1 8
#define LED2 9
#define LED3 10



void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);
  //Timer1.initialize(2000000);
  //Timer1.attachInterrupt(printStatus);
  Serial.setTimeout(2);
}

void loop() {
  long int input = -1;
  String 
  if(Serial.available() > 0) {
    input = Serial.parseInt();
    if(input >= 1 && input <=3) {
      toggleLED(input);
    } else {
      Serial.print("Invalid LED number. Enter a numbr between 1-3\n");
    }
  }
}

void toggleLED(int pin) {
  pin = pin+7;
  digitalWrite(pin, digitalRead(pin) ^ 1);
}
void printStatus() {
  
  Serial.print("     STATUS\n");
  Serial.print("LED1: ");
  pinState_print(LED1);
  Serial.print("LED2: ");
  pinState_print(LED2);
  Serial.print("LED3: ");
  pinState_print(LED3);
  Serial.print("\n");
}

void pinState_print(byte pin) {
  if(digitalRead(pin) == HIGH) {
      Serial.print("ON\n");  
  } else if (digitalRead(pin) == LOW) {
      Serial.print("OFF\n");
  } else {
      Serial.print("ERR\n");
  }
}

