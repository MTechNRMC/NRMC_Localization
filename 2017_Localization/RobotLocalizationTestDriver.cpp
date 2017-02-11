// Driver to test the localization functions

#include "RobotLocalization.h"
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char** argv)
{
	POSITION topPostPosition = {stod(argv[1]), stod(argv[2])};
	POSITION bottomPostPosition = {stod (argv[3]), stod(argv[4])};
	double separation = topPostPosition.y - bottomPostPosition.y;
	POSITION realPosition = {stod(argv[5]), stod(argv[6])};
	RobotLocalization localizer(topPostPosition, bottomPostPosition);
	double topDistance = sqrt(pow(topPostPosition.x - realPosition.x, 2) + pow(topPostPosition.y - realPosition.y, 2));
	double bottomDistance = sqrt(pow(bottomPostPosition.x - realPosition.x, 2) + pow(bottomPostPosition.y - realPosition.y, 2));
	POSITION foundPosition = localizer.findPosition(bottomPostPosition, topDistance, bottomDistance, separation);

	printf("Found position as %f, %f; real position is %f, %f\n", foundPosition.x, foundPosition.y, realPosition.x, realPosition.y);
}

