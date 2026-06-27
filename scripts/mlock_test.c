#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>

int main() {
    size_t size = 300 * 1024 * 1024; // 300 MB

    printf("Allocating memory...\n");

    char *buffer = malloc(size);

    if (buffer == NULL) {
        perror("malloc failed");
        return 1;
    }

    memset(buffer, 1, size);

    printf("Memory allocated. Press Enter to apply mlock...\n");
    getchar();

    if (mlock(buffer, size) == 0) {
        printf("mlock applied successfully. Memory locked in RAM.\n");
    } else {
        perror("mlock failed");
    }

    printf("Press Enter to exit...\n");
    getchar();

    munlock(buffer, size);
    free(buffer);

    return 0;
}
