# -*- coding: utf-8 -*-
"""
Spikesorting with SpikeInterface
=========================================

One of the most common processing steps for neuronal data is the identification
of spiking activity of individual neurons. [SpikeInterface](https://github.com/Spikeinterface/Spikeinterface)
is a python packages that provides a common interface to multiple different software tools designed
for this task. Here we demonstrate how to preprocess a BIDS-ephys compatible dataset using SpikeInterface
and visualize the result. This script is accessible at :download:`source Python script <plot_spikesorting.py>`."""

# %%
# First we import SpikeInterface and locate the dataset

import matplotlib.pyplot as plt
import spikeinterface.full as si

session_folder = '../ephys_nix/sub-i/ses-140703/ephys'

# %%
# SpikeInterface provides a convenience function for loading a BIDS-ephys compatible dataset.
# This dataset contains multiple streams (data recorded at different sampling rates).
# SpikeInterface represents each of those streams in a separate `recording` object.

recordings = si.read_bids(session_folder)

# %%
# We select the most `raw` data stream by selecting the one with the highest temporal resolution, i.e. sampling frequency.
recording_raw = recordings[0]
for rec in recordings[1:]:
    if rec.get_sampling_frequency() > recording_raw.get_sampling_frequency():
        recording_raw = rec

# %%
# By default the software packages to be used for spike sorting needs to be installed locally to
# perform the sorting. However, the installation of these specialized software tools can be
# complicated and inconvenient due to specific system requirement. To simplify the usage of
# different spike sorting packages SpikeInterface provides a set of containers with preinstalled
# sorting packages. The list of available containers and their versions is available on
# [DockerHub](<TODO: Add link here>).
#
# Here we run the sorting package `ironclust` using the containerized version. To run the c
# ontainer we are using `singularity`, alternativly SpikeInterface also supports running contains
# in `docker`.

sorting = si.run_sorter_container(sorter_name='ironclust', recording=recording_raw,
                                       mode='singularity',
                                       container_image='spikeinterface/ironclust-compiled-base',
                                       output_folder='ironclust_output',
                                       with_output=True, fGpu=False)
print(sorting)

# %%
# Automatic spike sorting always requires manual inspection the results to confirm the sorting
# algorithm and the applied parameters were suited for the dataset. Here we visualize the extracted
# spike times for each unit (neuron) in a raster plot.

si.plot_rasters(sorting)

for ext in ['png', 'svg']:
    plt.savefig(f'raster_plot.{ext}')

# %%
# We can extract the waveforms on which the sorting is based. To align the waveforms we remove the
# low frequency components before extracting the waveform snippets from the raw signal.

recording_filtered = si.highpass_filter(recording_raw, freq_min=300.)  # frequencies are provided in Hz
recording_filtered.annotate(is_filtered=True)

waveforms = si.extract_waveforms(recording_filtered, sorting, './ironclust_waveform_output',
                                 load_if_exists=True, ms_before=1, ms_after=2.)

si.plot_unit_waveforms(waveforms)

plt.show()

# %%
# Block splitters allow you alternate between code and text blocks **and**
# separate sequential blocks of code (above) and text (below).

##############################################################################
# A line of ``#``'s also works for separating blocks. The above line of ``#``'s
# separates the text block above from this text block. Notice however, that
# separated text blocks only shows as a new lines between text, in the rendered
# output.

def dummy():
    """This should not be part of a 'text' block'"""

    # %%
    # This comment inside a code block will remain in the code block
    pass


# this line should not be part of a 'text' block

# %%
#
# ####################################################################
#
# The above syntax makes a line cut in Sphinx. Note the space between the first
# ``#`` and the line of ``#``'s.

# %%
# .. warning::
#     The next kind of comments are not supported (notice the line of ``#``'s
#     and the ``# %%`` start at the margin instead of being indented like
#     above) and become too hard to escape so just don't use code like this::
#
#         def dummy2():
#             """Function docstring"""
#         ####################################
#         # This comment
#         # %%
#         # and this comment inside python indentation
#         # breaks the block structure and is not
#         # supported
#             dummy2
#

"""Free strings are not supported. They will be rendered as a code block"""

# %%
# New lines can be included in your text block and the parser
# is capable of retaining this important whitespace to work with Sphinx.
# Everything after a block splitter and starting with ``#`` then one space,
# is interpreted by Sphinx-Gallery to be a rST text block. Keep your text
# block together using ``#`` and a space at the beginning of each line.
#
# rST header within text block
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print('one')

# %%
#

# another way to separate code blocks shown above
B = 1

# %%
# Last text block.
#
# That's all folks !
#
# .. literalinclude:: plot_parse.py
#
#
