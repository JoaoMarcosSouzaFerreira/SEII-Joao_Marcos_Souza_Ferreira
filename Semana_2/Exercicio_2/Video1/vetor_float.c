#include "float_vector.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/***********************************************INTERFACE PRIVADA***************************************/

struct float_vector {
	int capacity;
	int size;
	float *data;
};

bool _FloatVector_isFull(const FloatVector *vec){
	return vec->size == vec->capacity;
}

/****************************************IMPLEMENTAÇÃO DA INTERFACE PÚBLICA*****************************/

/**
 * @brief Cria(aloca), um vetor de floats com uma dada capacidade
 *
 * @param capacity capacidade do vetor
 * @return FloatVector* Um vetor de floats alocado/criado.
 */

FloatVector *FloatVector_create(int capacity){
	FloatVector *vec = (FloatVector*) calloc(1, sizeof(FloatVector));
	vec->size = 0;
	vec->capacity = capacity;
	vec->data = (float*) calloc(capacity, sizeof(float));
	return vec;
}

void FloatVector_destroy(FloatVector** vec_ref){
	FloatVector *vec = *vec_ref;
	
	free(vec->data);
	free(vec);
	*vec_ref = NULL;
}

void FloatVector_append(FloatVector *vec, float val){
	if(_FloatVector_isFull(vec)){
		fprintf(stderr, "ERROR in 'append'\n");
		fprintf(stderr, "Vector is full\n");
		exit(EXIT_FAILURE);
	}

	vec->data[vec->size] = val;
	vec->size++;
}

float FloatVector_remove(FloatVector *vec, int index){
	if(index < 0 || index >= vec->size){
		fprintf(stderr, "ERROR in 'remove'\n");
		fprintf(stderr, "Index [%d] is out of bounds: [0, %d]\n", index, vec->size);
		exit(EXIT_FAILURE);
	}

	float removedValue = vec->data[index];
	for(int i = index; i < vec->size; i++){
		vec->data[i] = vec->data[i+1];
	}
	vec->size--;
	return removedValue;
}

void FloatVector_print(const FloatVector *vec){
	puts("------------------------");
	printf("Size: %d\n", vec->size);
	printf("Capacity: %d\n", vec->capacity);
	puts("---");

	for(int i = 0; i < vec->size; i++){
		printf("[%d] = %f\n", i, vec->data[i]);
	}
	puts("------------------------");
}

float FloatVector_at(const FloatVector *vec, int index){
	if(index < 0 || index >= vec->size){
		fprintf(stderr, "ERROR in 'at'\n");
		fprintf(stderr, "Index [%d] is out of bounds: [0, %d]\n", index, vec->size);
		exit(EXIT_FAILURE);
	}

	return vec->data[index];
}

float FloatVector_get(const FloatVector *vec, int index){
	return vec->data[index];
}

void FloatVector_set(FloatVector *vec, int index, float val){
	if(index < 0 || index >= vec->size){
		fprintf(stderr, "ERROR in 'set'\n");
		fprintf(stderr, "Index [%d] is out of bounds: [0, %d]\n", index, vec->size);
		exit(EXIT_FAILURE);
	}

	vec->data[index] = val;
}
