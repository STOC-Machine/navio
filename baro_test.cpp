#include "Navio/MS5611.h"
#include "Navio/Util.h"
#include <unistd.h>
#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <signal.h>

using namespace std;

int main()
{
  MS5611* barometer = new MS5611;
  assert(barometer != NULL) {
    cerr << "ERROR: Could not allocate memory MS5611 device." << endl;
    return -1;
  }

  if (check_apm()) {
        return 1;
    }

  barometer->initialize(); // init the actual device for usage

  barometer->refreshPressure();
  usleep(10000); // Waiting for pressure data ready
  barometer->readPressure();

  barometer->refreshTemperature();
  usleep(10000); // Waiting for temperature data ready
  barometer->readTemperature();

  barometer->calculatePressureAndTemperature();

  printf("Temperature(C): %f Pressure(millibar): %f\n",
          barometer->getTemperature(), barometer->getPressure());

  if ((barometer -> getTemperature()) <= 21.f && (barometer -> getTemperature()) >= 15.f) {
    printf("You're in a fairly warm enviornment.\n");
  }

  delete barometer;

  return 0;

}
