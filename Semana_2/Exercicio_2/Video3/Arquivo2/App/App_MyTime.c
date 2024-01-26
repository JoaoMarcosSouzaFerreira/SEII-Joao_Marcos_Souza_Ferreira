#include "float_vector.h"
#include "mytime.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
	FloatVector *vec = FloatVector_create(3);
	FloatVector_print(vec);

	timer t1 = tic();
	
	FloatVector_append(vec, 1);
	FloatVector_append(vec, 2);
	FloatVector_append(vec, 3);
	FloatVector_print(vec);

	fprintf(stdout, "Removed value [%f]", FloatVector_remove(vec, 1));
	FloatVector_print(vec);
	
	timer t2 = tac();
	fprintf(stdout, "Tempo de processamento: %f\n", comptime(t1, t2));

	return EXIT_SUCCESS;
}
