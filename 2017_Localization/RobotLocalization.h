#pragma once
struct POSITION {
	double x;
	double y;
};

class RobotLocalization {
private:
	POSITION topPostPosition;
	POSITION bottomPostPosition;
public:
	RobotLocalization(POSITION, POSITION);
	// TODO: Get the actual distances from the Leddar and the Pixie and account for the offset from the center of the robot
	POSITION getPosition();
	POSITION findPosition(POSITION, double, double, double);

	// TODO: Implement once we know what to expect from the Leddar and the Pixie
	double getAngle();
};