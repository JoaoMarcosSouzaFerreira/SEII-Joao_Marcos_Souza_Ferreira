#include "mytime.h"



timer tic() {
    timer tic_;
    gettimeofday(&tic_, NULL); // "marca" o tempo atual
    return tic_;
}


timer tac() {
    return tic();
}


float comptime(timer tic, timer tac) {
  float t = ((tac.tv_sec  - tic.tv_sec) * 1000.0) +
            ((tac.tv_usec - tic.tv_usec) * 0.001);
  
  return t;
}
