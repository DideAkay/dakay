// Visual Micro is in vMicro>General>Tutorial Mode
// 
/*
    Name:       otoSulama.ino
    Created:	31.12.2019 15:53:51
    Author:     DideAkay\Dide Akay
*/

// Define User Types below here or use a .h file
//


// Define Function Prototypes that use User Types below here or use a .h file
//

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


int flowLed = 8; //motorStatus = high ise yanar
int stopLed = 7; //motorStatus = low ise yanar

int higroPin = A0;

int motorPin =10;

int esikDeger = 400;
int anlikDeger = 0;



long olcumSayaci;
long previousMillis = 0;
long currentMillis = 0;





// The setup() function runs once each time the micro-controller starts
void setup()
{
	pinMode(flowLed, OUTPUT);
	pinMode(stopLed, OUTPUT);
	pinMode(higroPin, INPUT);



	lcd.begin(16, 2);

	Serial.begin(9600);
}

// Add the main program code into the continuous loop() function
void loop()
{
	anlikDeger = analogRead(higroPin);
	Serial.println("anlikDeger");
	Serial.println(anlikDeger);
	
	olcumSayaci = currentMillis - previousMillis;
	Serial.println("olcumSayaci");
	Serial.println(olcumSayaci);

	

	if (anlikDeger > esikDeger){
		
		


		if (olcumSayaci == 0) {
			previousMillis = millis();
			digitalWrite(flowLed, HIGH);
			digitalWrite(stopLed, LOW);
			digitalWrite(motorPin, HIGH);
			currentMillis = millis();
			lcd.clear();
			lcd.print("Giving");
			lcd.setCursor(0, 1);
			lcd.print("water...");
		}
		
	
		
		

		else if (olcumSayaci <= 1000) {
			currentMillis = millis();
			// bir saniye boyunca motoru çalýþtýr
			digitalWrite(stopLed, LOW);
			digitalWrite(motorPin, HIGH);
			digitalWrite(flowLed, HIGH);
			lcd.clear();
			lcd.print("Giving");
			lcd.setCursor(0, 1);
			lcd.print("water...");

		}

		else if (olcumSayaci < 5000) {
			//ilk ölçümden beþ saniye sonra hala kuru ise
			//sayaçlarý bir sonraki ölçüm için sýfýrla
			//sayaçlar sýfýrlanýnca baþtaki if(olcumSayacý = 0) döngüsüne girip su verir
			currentMillis = millis();
			digitalWrite(stopLed, HIGH);
			digitalWrite(motorPin, LOW);
			digitalWrite(flowLed, LOW);
			lcd.clear();
			lcd.print("Measuring...");
			
		}
		
		else if (olcumSayaci > 5000) {
			olcumSayaci = 0;
			previousMillis = 0;
			currentMillis = 0;

		}
		
		
		

	}

	else {
	 
			digitalWrite(flowLed, LOW);
			digitalWrite(stopLed, HIGH);
			digitalWrite(motorPin, LOW);
			previousMillis = 0;
			currentMillis = 0;
			lcd.clear();
			lcd.print("Moisture:");
			lcd.setCursor(0, 1);
			lcd.print("sufficient :)");
		}


	
	}
