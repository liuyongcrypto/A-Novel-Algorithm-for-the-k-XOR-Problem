# A Novel Algorithm for the k-XOR Problem

## Introduction

This Python script is designed to compute the state vector of the k-XOR algorithm with the optimal Time-Memory Trade-Off (TMTO) formula. It also provides the decomposition of k when applicable and allows users to specify custom decompositions to compute their corresponding state vectors.

## Features

- Computes the state vector of the k-XOR algorithm with the optimal TMTO formula.
- Determines the decomposition of k that achieves the optimal TMTO formula.
- Allows users to input their own decomposition of k to obtain the corresponding state vector.

## Requirements

This script runs on Python 3 and requires no additional dependencies.

## Usage

Run the script using Python:

```
python A Novel Algorithm for the k-XOR Problem.py
```

### User Inputs

Upon execution, the user will be prompted to select a model:

1. Compute the state vector of the k-XOR algorithm with the optimal TMTO formula.
2. Compute the state vector of the k-XOR algorithm with the optimal TMTO formula and find the corresponding decomposition of k.
3. Compute the state vector of the k-XOR algorithm with the optimal TMTO formula and its decomposition, and additionally allow user-defined decompositions.

The user is then prompted to enter the value of `k` (default is `7` if left blank). The script then computes and displays the results based on the selected model.

### Example Execution

#### Selecting Model 1

```
Please select a model:
Enter 1 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula.
Enter 2 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k.
Enter 3 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k. Additionally, the state vector of the k-XOR algorithm can be derived for any given decomposition of k.
Enter your choice (1 - 3): 1

You selected Model 1: Design the k-XOR algorithm with an optimal TMTO formula.

Please enter the parameter k (k >= 3) of the k-XOR algorithm to be designed:
If you choose Model 1, you can obtain results in just a few minutes for k not exceeding 30.
If you choose Model 2, you can obtain results in just a few minutes for k not exceeding 29.
If you choose Model 3, you can obtain results in just a few minutes for k not exceeding 27.
Pressing Enter directly will use the default parameter 'k = 7': 5

The state of the 5-XOR algorithm with the optimal TMTO formula is:
[[2, 0, 1], [2, 1, 1], [2, 2, 1]]
```

#### Selecting Model 2

```
Please select a model:
Enter 1 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula.
Enter 2 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k.
Enter 3 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k. Additionally, the state vector of the k-XOR algorithm can be derived for any given decomposition of k.
Enter your choice (1 - 3): 2

You selected Model 2: Design the k-XOR algorithm with an optimal TMTO formula and obtain the decomposition of k.

Please enter the parameter k (k >= 3) of the k-XOR algorithm to be designed:
If you choose Model 1, you can obtain results in just a few minutes for k not exceeding 30.
If you choose Model 2, you can obtain results in just a few minutes for k not exceeding 29.
If you choose Model 3, you can obtain results in just a few minutes for k not exceeding 27.
Pressing Enter directly will use the default parameter 'k = 7': 5

The state of the 5-XOR algorithm with the optimal TMTO formula is:
[[2, 0, 1], [2, 1, 1], [2, 2, 1]]

The decomposition of k corresponding to the k-XOR algorithm with the optimal TMTO formula is as follows.
If multiple decompositions are available, any one of them can be selected.
When M^1 <= T <= M^3, the decomposition of 5 can be: 5 =  2 + 3

Please derive the TMTO formula for the 5-XOR algorithm based on the definition of the state of the K-XOR algorithm presented in the manuscript.
```

#### Selecting Model 3

```
Please select a model:
Enter 1 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula.
Enter 2 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k.
Enter 3 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k. Additionally, the state vector of the k-XOR algorithm can be derived for any given decomposition of k.
Enter your choice (1 - 3): 3

You selected Model 3: Design the k-XOR algorithm with an optimal TMTO formula and obtain the decomposition of k. You can also obtain the state vector of the k-XOR algorithm corresponding to any decomposition of k.

Please enter the parameter k (k >= 3) of the k-XOR algorithm to be designed:
If you choose Model 1, you can obtain results in just a few minutes for k not exceeding 30.
If you choose Model 2, you can obtain results in just a few minutes for k not exceeding 29.
If you choose Model 3, you can obtain results in just a few minutes for k not exceeding 27.
Pressing Enter directly will use the default parameter 'k = 7': 6

The state of the 6-XOR algorithm with the optimal TMTO formula is:
[[2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 3, 1]]

The decomposition of k corresponding to the k-XOR algorithm with the optimal TMTO formula is as follows.
If multiple decompositions are available, any one of them can be selected.
When M^1 <= T <= M^4, the decomposition of 7 can be: 7 =  3 + 4

Please derive the TMTO formula for the 7-XOR algorithm based on the definition of the state of the K-XOR algorithm presented in the manuscript.

If you want to print the state corresponding to any decomposition of 7.

Please enter multiple numbers separated by spaces (press Enter to exit).
Please enter numbers k_i from smallest to largest (e.g., 4 4 6 9).
2 5
The state vector corresponding to decomposition 7 =  2 + 5 is:

[[2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
```

## Notes

- The script supports computations for `k` up to 30 for Model 1, up to 29 for Model 2, and up to 27 for Model 3.
- The computation time increases with higher values of `k`.

## License

This project is released under the MIT License.