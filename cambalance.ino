#include <Stepper.h>

const int stepsPerRevolution = 48;

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
int currentSteps = 0;

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  // initialize the serial port:
  Serial.begin(9600);
  Serial.println("start");
}

void loop() {
  int steps = Serial.parseInt();

  if (steps != 0)
  {
    int stepsToDo = steps - currentSteps;

    myStepper.step(stepsToDo);
    currentSteps = steps;
    Serial.println("done");
  }
}

