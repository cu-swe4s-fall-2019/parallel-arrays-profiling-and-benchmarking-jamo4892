import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
# Import modules.


def boxplot(L, nameset, group_col_name, gene_name, out_file_name):
    """
    Purpose
    -------
    This function makes a box plot of an input array of gene types
    and saves the plot to a file.

    Inputs
    ------
    L: Integer array
    Array with the count of each gene type

    nameset: String array
    Array with the name of each gene type

    group_col_name: String
    Gene type name

    gene_name: String
    Gene name

    out_file_name: string
    File name for saving the plot

    Outputs
    -------
    out_file: .png
    File of the box plot
    """

    plot_figure = plt.figure(figsize=(6, 2), dpi=300)
    boxplt = plot_figure.add_subplot(1, 1, 1)
    # Create a series of box plots- add each new plot to the existing figure.

    boxplt.boxplot(L)
    boxplt.set_xlabel(group_col_name)
    boxplt.set_ylabel('Gene Counts')
    boxplt.set_title(gene_name)
    boxplt.set_xticklabels(nameset, rotation=90)
    # Make the plot and add labels.

    plt.savefig(out_file_name, bbox_inches='tight')
    return out_file_name
    # Save plot to file name.
