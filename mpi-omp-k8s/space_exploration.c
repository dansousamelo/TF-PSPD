#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>
#include <omp.h>

#define NUM_PLANETS 5
#define MAX_CAMERAS 4

const char *planets[NUM_PLANETS] = {
    "Marte", "Vênus", "Júpiter", "Saturno", "Netuno"
};

double random_value(double min, double max) {
    return min + (rand() / (double) RAND_MAX) * (max - min);
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size, world_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    srand(time(NULL) + world_rank);


    int planet_index = rand() % NUM_PLANETS;
    printf("🚀 Sonda %d está explorando o planeta %s! 🌍\n", world_rank, planets[planet_index]);


    #pragma omp parallel num_threads(MAX_CAMERAS)
    {
        int thread_id = omp_get_thread_num();
        double temperature = random_value(-100, 100);
        double radiation = random_value(0, 10);
        double mineral = random_value(0, 100);

        printf("📡 [Sonda %d - Câmera %d] Planeta: %s | Temp: %.2f°C | Radiação: %.2f | Minerais: %.2f%%\n",
               world_rank, thread_id, planets[planet_index], temperature, radiation, mineral);
    }

    MPI_Finalize();
    return 0;
}
