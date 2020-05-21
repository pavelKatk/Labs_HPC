import numpy as np
import pycuda.autoinit
from  pycuda import  driver
from pycuda.compiler import SourceModule
import time

mod = SourceModule("""
                __global__ void Calc(double *x, double *y, double *count) {
        int idx = blockIdx.x * blockDim.x + threadIdx.x; 
        int threadCount = gridDim.x * blockDim.x;
        int N = 65536*16;
        int count_gpu = 0;
        for (int i = idx; i < N; i += threadCount) {
                if (x[i] * x[i] + y[i] * y[i] < 1) {
                        count_gpu++;
                }
        }
        atomicAdd(count , count_gpu);
}
""")

def calc_cpu(N):
    count_cpu = 0
    for i in range(N):
        if x[i] ** 2 + y[i] ** 2 < 1:
            count_cpu += 1
    return count_cpu*4/N

N = 65536*16
x,y = np.random.random(N), np.random.random(N)

block_size = (256, 1, 1)
grid_size = (int(N / (128 * block_size[0])), 1)

count = np.zeros(1)
calc = mod.get_function("Calc")

start = time.time()
calc(driver.In(x), driver.In(y),driver.Out(count), block = block_size, grid = grid_size)
driver.Context.synchronize()
end = time.time()

start_cpu = time.time()
pi_cpu = calc_cpu(N)
end_cpu = time.time()

print('Время GPU {}'.format(end - start))
print('Время  CPU {}'.format(end_cpu - start_cpu))
print('Ускорение {}'.format((end_cpu - start_cpu)/ (end - start)))
print('Значение CPU ', pi_cpu)
print('Значение GPU ', count*4/N)
