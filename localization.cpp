// localization.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "ultra_simple.h"
#include <string>


//matrix of data, angle, distance, quality;
static struct TARGET
{
	float distance;
	float angle;
}T1, T2;


class ProcessTargets{
public:
	int points;
	float data[decimation*angles][3];

	ProcessTargets() :points(decimation * angles)
	{
		
	}

	void search()
	{
		//TODO: algo goes here;
		//use the data table;

		T1.angle = 100;
		T1.distance = 200;
		T2.angle = T1.angle;
		T2.distance = T2.distance;
	}

	void find_directions()
	{
		// TODO: Ross' code here
	}

};


int main(int argc, const char * argv[])
{
	ProcessTargets Targets;
	RPlidarDriver * retdrv;
	u_result op_result;
	int retval = ultra_simple(argc, argv, &retdrv);
	if (retval != 1)
		printf("Something wrong. Error code: %d", retval);

	while (1){
		
		rplidar_response_measurement_node_t nodes[angles * decimation];
		size_t   node_count = _countof(nodes);
		op_result = retdrv->grabScanData(nodes, node_count);

		if (IS_OK(op_result))
		{
			retdrv->ascendScanData(nodes, node_count);

			// first build the table
			for (int pos = 0; pos < (int)node_count; ++pos) {
				//string quality = (nodes[pos].sync_quality & RPLIDAR_RESP_MEASUREMENT_SYNCBIT) ? "S " : "  "; 1.angle 2. distance 3. quality;
				Targets.data[pos][0] = (nodes[pos].angle_q6_checkbit >> RPLIDAR_RESP_MEASUREMENT_ANGLE_SHIFT) / 64.0f;
				Targets.data[pos][1] = nodes[pos].distance_q2 / 4.0f;
				Targets.data[pos][2] = nodes[pos].sync_quality >> RPLIDAR_RESP_MEASUREMENT_QUALITY_SHIFT;

				printf("%s theta: %03.2f Dist: %08.2f Q: %d \n",
					(nodes[pos].sync_quality & RPLIDAR_RESP_MEASUREMENT_SYNCBIT) ? "S " : "  ",
					(nodes[pos].angle_q6_checkbit >> RPLIDAR_RESP_MEASUREMENT_ANGLE_SHIFT) / 64.0f,
					nodes[pos].distance_q2 / 4.0f,
					nodes[pos].sync_quality >> RPLIDAR_RESP_MEASUREMENT_QUALITY_SHIFT);
			}

			//next process the data from the table
			Targets.search(); //setup T1,T2;
			Targets.find_directions();
		}

	}

	on_finished(&retdrv);
	return 0;

}

