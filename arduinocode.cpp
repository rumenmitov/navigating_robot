// C++ code
#define GET_DIST(t) (t/2) * 340L / 10000L
static int trig = 7;
static int echo = 6;
int duration = 0;
int distance = 0;
static int rotation_motor = 2;
static int engine_motor = 3;

void setup()
{
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  digitalWrite(trig, LOW);
  pinMode(rotation_motor, OUTPUT);
  pinMode(engine_motor, OUTPUT);
}

void loop()
{
  digitalWrite(trig, HIGH);
  delay(15); 
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = GET_DIST(duration);
  Serial.print(distance);
  Serial.print("\n");
  //Motor movement
  digitalWrite(engine_motor, LOW);
  if(distance <= 50L){
  	digitalWrite(rotation_motor, HIGH);
    delay(1500);
    digitalWrite(rotation_motor, LOW);
    serial.write(1);//Writing 1 to python to plot rotation
  }
  else{
    serial.write(0);
  }
    digitalWrite(engine_motor, HIGH);
  	delay(500);
}

