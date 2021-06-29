# ReadMe
这里有用矩阵束方法实现Prony方法的matlab和python代码，可用来分析时域信号。matlab代码来自参考文献，py代码的过程和功能和matlab代码一致。

代码中的函数需要三个输入参数，分别是信号数组x\[n\]，分析阶数p（p阶意味着信号由p项指数项的线性组合表示）和采样时间。

函数输出的是一个p×4矩阵，矩阵的列向量分别是振幅，初相位，衰减因子和频率。

-----------------------------------------------------------------------------------------------------------------------------------------
This repository includes matlab code and py code which implement Prony's method via Matrix Pencil Method.

A data sequence x\[n\] can be represented by the sum of p complex parameters (order p).The function requires three input parameters (x,p,Ts), which are data sequence x\[n\], p, and sampling period of signal x\[n\].

The output parameter of the function is a (p × 4) matrix whose column vectors are amplitude, initial phase, attenuation factor, and frequency.

Reference :
Fernández Rodríguez, A., de Santiago Rodrigo, L., López Guillén, E. et al. Coding Prony’s method in MATLAB and applying it to biomedical signal filtering. BMC Bioinformatics 19, 451 (2018). https://doi.org/10.1186/s12859-018-2473-y
