This script takes 2 input ASCII files with the following format:

2026-04-03 00:00:01	2026-04-03 00:03:56	3618683	1	DragPointing 18683	281.991	62.369	45.984	Auto	0x000a	0	175
2026-04-03 00:04:01	2026-04-03 00:08:00	3618684	1	DragPointing 18684	286.993	60.289	34.998	Auto	0x000a	0	180
2026-04-03 00:08:01	2026-04-03 00:13:55	3618685	1	DragPointing 18685	235.989	-9.253	24.019	Auto	0x000a	0	210
2026-04-03 00:14:00	2026-04-03 00:20:00	3618686	1	DragPointing 18686	296.008	-54.255	35.999	Auto	0x000a	0	215

containing the information about the PPST and AFST pointings for a specific day. It compares the start and stop times and show in red mismatches of more than 30 s in the start and end times.
