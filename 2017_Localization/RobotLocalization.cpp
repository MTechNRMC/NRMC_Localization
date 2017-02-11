#include "RobotLocalization.h"
#include <math.h>

RobotLocalization::RobotLocalization(POSITION topPostPosition, POSITION bottomPostPosition) {
	this->topPostPosition = topPostPosition;
	this->bottomPostPosition = bottomPostPosition;
}

POSITION RobotLocalization::findPosition(POSITION bottomPosition, double topDistance, double bottomDistance, double separation) {
	POSITION foundPosition = {(double)0, (double)0};
	double verticalOffset = ((bottomDistance - topDistance)*(bottomDistance + topDistance) + pow(separation, 2)) / (2 * separation);
	foundPosition.y = bottomPosition.y + verticalOffset;
	foundPosition.x = sqrt(pow(bottomDistance, 2) - pow(verticalOffset, 2));
	return foundPosition;
}