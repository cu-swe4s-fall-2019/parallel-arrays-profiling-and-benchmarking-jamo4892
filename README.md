Homework 4
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
These files must be downloaded to the user's local repository before running the code.

Code
data_viz.py
Makes a box plot of the frequency of the selected gene in different tissue types. Called by plot_gtex.py

plot_gtex.py
Searches the files downloaded above to find the selected gene type and gene group type, using linear_search and binary_search (functions within plot_gtex.py). Calls data_viz.py.

Profiling & Benchmarking
I was unable to complete this part of the assignment. The plot_gtex.linear_search.txt file contains the output of the following command:
$ python -m cProfile -s tottime plot_gtex.py
I do not know if I ran this correctly, as there is no indication of either linear_search or binary_search in
the profiling results.

Testing
I was unable to complete unit or functional tests for the assignment. The only tests I added to the 
.travis.yml file are to test plot_gtex.py and data_viz.py with pycodestyle.

Example
$ python plot_gtex.py --gene_readGTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --gene_file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --out_file gene_plot.png