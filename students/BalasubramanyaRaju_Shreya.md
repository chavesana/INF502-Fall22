## Assignment-1: Part 2 
### Report on the last paper I've read is as follows;

1. Title of the paper:  Fuzz Testing the Compiled Code in R Packages
2. Authors: Akhila Chowdary Kolla, Dr. Toby Dylan Hocking, Dr. Alex groce
3. Venue (Conference Name): The R conference
4. Number of pages in the conference: 9
5. Outcomes of the paper: 
   - RcppDeepState detects memory leaks and memory safety concerns. In addition, a comparison was made to evaluate if there was any discernible difference in performance between the different fuzzers. 
   - With only the tool's default settings and the included RcppExports. R files, RcppDeepState was used to fuzz a large number of CRAN packages using Rcpp.
   - The fuzzing is completed quickly and at a low cost. The most well-known fuzzers are Afl and libFuzzer, the function-based fuzzer included with the newest versions of LLVM/clang. The built-in brute-force fuzzer in DeepState was known for its lightning-fast test generation rate. Each fuzzer found flaws in a variety of packages and functionalities. 
   - When a function finds invalid input, it raises a gentle exception to alert the user. There are 2,077 Rcpp packages in CRAN. One thousand and eighty-five of these were evaluated. There were 6,860 procedures that were fuzzed. At least one Valgrind alert was triggered by 965 of them.
6. Link to the paper: [click here](https://agroce.github.io/issre21.pdf)
