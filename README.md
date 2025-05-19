# Phylogenetic Tree Pruner

This repository contains scripts for pruning parsimony-based phylogenetic trees encoded in Protocol Buffer format. It enables the removal of internal nodes with fewer than a specified number of descendant observations and exports the pruned trees in binary or text format.

## Features

* Prune internal nodes based on a minimum observation count (k).
* Support for Protocol Buffer binary and text formats.
* Auto-generated Protocol Buffer message definitions.

## Files

* **pruner.py**: Command-line script to prune a tree in binary Protobuf format.
* **ppruner.py**: Command-line script to prune a tree and export using Protobuf text format.
* **p2.py**: Experimental/alternate implementation of the pruning logic.
* **parsimony\_pb2.py**: Auto-generated Protobuf Python classes (`data`, `mut`, `mutation_list`) from `parsimony.proto`.

## Requirements

* Python 3.6 or above
* Packages:

  * `bte` (for `MATree` operations)
  * `protobuf` (for `parsimony_pb2.py`)
  * Standard libraries: `argparse`, `gzip`

Install dependencies:

```bash
pip install protobuf bte
```

## Usage

### pruner.py

Prune a binary Protocol Buffer tree:

```bash
python pruner.py <input_tree.pb> <k> <output_tree.pb>
```

* `<input_tree.pb>`: Path to the input tree in binary Protobuf format.
* `<k>`: Minimum number of descendant observations to retain internal nodes.
* `<output_tree.pb>`: Path to write the pruned tree.

### ppruner.py

Prune and export using Protobuf text format:

```bash
python ppruner.py <input_tree.pb> <k> <output_tree.pb>
```

Arguments are the same as for `pruner.py`.

### p2.py

Alternate pruning version:

```bash
python p2.py <input_tree.pb> <k> <output_tree.pb>
```

## Development

* If you modify the Protobuf schema (`parsimony.proto`), regenerate the Python classes:

  ```bash
  protoc --python_out=. parsimony.proto
  ```

* Integrate these scripts into your phylogenetic analysis pipelines as needed.
