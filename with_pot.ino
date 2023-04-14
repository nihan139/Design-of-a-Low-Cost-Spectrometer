int pot;
int led;

float I = 0;
float V1 = 0;
float V2 = 0;
float R1=220;
float Vd = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A4, INPUT);
  pinMode(A0, INPUT);
}

void loop() {

  V1 = (float(analogRead(A0))/1023)*5;
  V2 = (float(analogRead(A4))/1023)*5;
  Vd = V1-V2;
  I=(V2/R1)*1000;
  Serial.println(Vd);
  //Serial.print("x");
  //Serial.print(" //// ");
  Serial.println(I);

  delay(500);
}
