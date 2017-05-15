#define EN_PIN    11 //enable (CFG6)
#define DIR_PIN   13 //direction
#define STEP_PIN  12 //step

const int stepsPerRevolution = 200;
int currentSteps = 0;

void setup()
{
  //set pin modes
  pinMode(EN_PIN, OUTPUT);
  digitalWrite(EN_PIN, HIGH); //deactivate driver (LOW active)
  pinMode(DIR_PIN, OUTPUT);
  digitalWrite(DIR_PIN, LOW); //LOW or HIGH
  pinMode(STEP_PIN, OUTPUT);
  digitalWrite(STEP_PIN, LOW);

  digitalWrite(EN_PIN, LOW); //activate driver

  Serial.begin(9600);
  Serial.println("start");
}

void loop()
{
  //make steps
  digitalWrite(STEP_PIN, HIGH);
  delay(2);
  digitalWrite(STEP_PIN, LOW);
  delay(2);

  int degs = Serial.parseInt();

  if (degs != 0)
  {
     int totalSteps = degs / 1.8;
     int stepsToDo = totalSteps - currentSteps;
     doSteps(stepsToDo);
     currentSteps = totalSteps;
     Serial.println(currentSteps);
  }
}

void doSteps(int steps)
{
  while (steps != 0)
  {
    if (steps > 0)
    {
      digitalWrite(DIR_PIN, HIGH);
      steps--;
    }
    else if (steps < 0)
    {
      digitalWrite(DIR_PIN, LOW);
      steps++;
    }

    digitalWrite(STEP_PIN, HIGH);
    delay(2);
    digitalWrite(STEP_PIN, LOW);
    delay(2);
  }
}

