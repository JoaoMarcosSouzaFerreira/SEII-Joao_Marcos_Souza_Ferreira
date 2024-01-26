#ifndef MY_TIME_H
#define MY_TIME_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

typedef struct timeval timer; 
timer tic();
timer tac();
float comptime(timer tic, timer tac);

#endif
