import matplotlib.pylab as plt
import data_viz
import sys
import gzip
import argparse
import matplotlib
matplotlib.use('Agg')
# Import modules.


def linear_search(key, L):
    """
    This function performs a linear search on an array.
    """
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i

    return -1
    # Scan the array and match the current value to the desired key.


def binary_search(key, L):
    """
    This function performs a binary search on an array.
    """
    lo = -1
    hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1
    # Scan the array and match the current value to the desired key.


def main():
    """
    Purpose
    -------

    Inputs
    ------

    Outputs
    -------
    Out_File: .png
    Screenshot of the generated box plot.
    """

    data_file_name = args.gene_read
    sample_info_file_name = args.gene_file
    group_col_name = args.group_type
    gene_name = args.gene
    outfile = args.out_file
    # Read in arguments.

    sample_id_col_name = 'SAMPID'

    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))
    # Read the gene file and put each line in an array, except for the header.

    group_col_index = linear_search(group_col_name, sample_info_header)
    sample_id_col_index = linear_search(sample_id_col_name, sample_info_header)
    # Find indices of gene group & sample.

    groups = []
    members = []
    names = []
    for row_index in range(len(samples)):
        sample = samples[row_index]
        sample_name = sample[sample_id_col_index]
        # Take sample & sample name from indices above.

        curr_group = sample[group_col_index]
        names = names + [curr_group]
        # Current group and gene name from indices above.

        curr_group_index = linear_search(curr_group, groups)
        if curr_group_index == -1:
            curr_group_index = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_index].append(sample_name)

    nameset = list(dict.fromkeys(names).keys())
    # Take only the unique gene names.

    version = None
    dim = None
    data_header = None

    gene_name_col = 1
    group_counts = [[] for i in range(len(groups))]

    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_index in range(len(groups)):
                for member in members[group_index]:
                    member_index = binary_search(member, data_header)
                    if member_index != -1:
                        group_counts[group_index].append(int(A[member_index]))
        # Run the binary search method on the gene name & type.
        # This code is taken from the lecture notes.

    g = data_viz.boxplot(group_counts, nameset, group_col_name, gene_name,
                         outfile)
    # Pass the gene information to data_viz.py to make a plot.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gene plotting tool')
    parser.add_argument('--gene_read', type=str, help='File of gene reads',
                        required=True)
    parser.add_argument('--gene_file', type=str, help='File of genes',
                        required=True)
    parser.add_argument('--gene', type=str, help='Gene type', required=True)
    parser.add_argument('--group_type', type=str,
                        help='Group type (SMTS or SMTSD)', required=True)
    parser.add_argument('--out_file', type=str, help='Name of output file',
                        required=True)
    args = parser.parse_args()
    # Arguments for command line calling.

    main()
