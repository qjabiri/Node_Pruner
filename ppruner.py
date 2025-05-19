import argparse
from google.protobuf import text_format
from parsimony_pb2 import data, mut, mutation_list
import gzip

'''
def encode_tree(tree_data):
    # Create a new instance of the 'data' class
    tree_pb = data()

    # Populate the 'newick' field with tree data
    tree_pb.newick = tree_data["newick"]

    # Populate the 'node_mutations' field with mutation data
    for node_mutations_data in tree_data["node_mutations"]:
        node_mutations_pb = mutation_list()
        for mutation_data in node_mutations_data:
            mutation_pb = mut(position=mutation_data["position"],
                               ref_nuc=mutation_data["ref_nuc"],
                               par_nuc=mutation_data["par_nuc"],
                               mut_nuc=mutation_data["mut_nuc"])
            node_mutations_pb.mutation.append(mutation_pb)
        tree_pb.node_mutations.append(node_mutations_pb)

    # Serialize the 'data' object to a binary string
    serialized_pb = tree_pb.SerializeToString()

    return serialized_pb

'''

def write_pb_to_file(tree_data, output_path):
    # Write the serialized binary data to a file
    serialized_pb = tree_data.SerializeToString()
    with gzip.open(output_path, 'wb') as f:
        f.write(serialized_pb)


def process_parsed_data(parsed_data, k, new_tree):
    ''' I TRIED TO FIND NODES IN NODES BUT THAT DID NOT WORK
    def process_parsed_data(parsed_data, k, new_node):
    
    for node_mutation in parsed_data.condensed_nodes:
        
        mutations = []
        for mutation in node_mutation.condensed_leaves:
            mutation_tracker = 0
            for mutation_count in node_mutation.condensed_leaves:
                if mutation_count == mutation:
                        mutation_tracker+=1
                
            if mutation_tracker >= k:
                mutations.append(mutation)
        if len(mutations) > 0:
            new_node2 = data.condensed_nodes
            for mutation in mutations:
                new_node2.add(mutation)
            new_node.extend(new_node2)
        
        
       # try:
        new_node = process_parsed_data(node_mutation, k, new_node)
        print('a')
       # except:
        #    return new_node'''                
    ''' THIS ONE WORKS BUT I WANTED TO EXTEND IT TO MORE THIGNS
    for node_mutation in parsed_data.node_mutations:
        mutations = []
        for mutation in node_mutation.mutation:
            mutation_tracker = 0
            for mutation_count in node_mutation.mutation:
                if mutation_count == mutation:
                        mutation_tracker+=1
                
            if mutation_tracker >= k:
                mutations.append(mutation)
        if len(mutations) > 0:
            new_node = data.node.mutations
            for mutation in mutations:
                new_node.add(mutation)
                print(mutation.mutation)
            parsed_data.extend(new_node)
    return parsed_data
     '''   
     
    mutations = []
    names = []
    cleaves = []
    metas = []
    for node_mutation in parsed_data.node_mutations:
        tmutations = []
        for mutation in node_mutation.mutation:
            mutation_tracker = 0
            for mutation_count in node_mutation.mutation:
                if mutation_count == mutation:
                        mutation_tracker+=1
                
            if mutation_tracker >= k:
                tmutations.append(mutation)
        mutations.append(tmutations)
                
                
                
    for condesned_node in parsed_data.condensed_nodes:
        tnames = []
        for cnode in condesned_node.node_name:
            mutation_tracker = 0
            for mutation_count in condesned_node.node_name:
                if mutation_count == cnode:
                        mutation_tracker+=1
                
            if mutation_tracker >= k:
                tnames.append(cnode)
        names.append(tnames)
        
                
                
    for condesned_node in parsed_data.condensed_nodes:
        tcleaves = []
        for cleaf in condesned_node.condensed_leaves:
            mutation_tracker = 0
            for mutation_count in condesned_node.condensed_leaves:
                if mutation_count == cnode:
                        mutation_tracker+=1
                
            if mutation_tracker >= k:
                tcleaves.append(cleaf)
        cleaves.append(tcleaves)
                
                
                
                
    #for metadata in parsed_data.metadata:
     #   tmetas = []
      #  for meta in metadata.clade_annotations:
       #     mutation_tracker = 0
        #    for mutation_count in metadata.clade_annotations:
         #       if mutation_count == meta:
          #              mutation_tracker+=1
                
           # if mutation_tracker >= k:
            #    tmetas.append(meta)
      #  metas.append(tmetas)
                
                
                
                
                
    if len(mutations) > 0:
        new_node = data.node_mutations
        new_cleaf = data.condensed_nodes
        new_metadata = data.metadata
        for i in range(len(mutations)):
            for j in range(len(mutations[i])):
                
                new_node.extend(mutation[j])
                new_cleaf.extend(names[j], cleaves[j])
                new_metadata.add(metas[j])
        new_tree.extend(new_node)   #add new_metadata
        new_tree.extend(new_cleaf)
    return new_tree
    
    
        
            
'''
def process_parsed_data(parsed_data, k, new_tree):
    # Example: Print the 'newick' field of the parsed data
    #print("Newick: ", parsed_data.newick)

     #Example: Iterate through 'node_mutations' and print each mutation
    
    for nodes in parsed_data.node_mutations:
        for node_mutation in nodes.node_mutations:
            for mutation in node_mutation.mutation:
                mutation_tracker = 0
                for mutation_count in node_mutation.mutation:
                    if mutation_count == mutation:
                        mutation_tracker+=1
                
                if mutation_tracker >= k:
                    new_tree.add(mutation)     # maybe .extend

    for node in parsed_data.node_mutations:
        if isinstance(data().node_mutations) in node.node_mutations:
            new_tree = is_node(node, k, new_tree)
            
            
    return new_tree


for node_mutation in parsed_data.node_mutations:
        for mutation in node_mutation.mutation:
            print("Mutation: ", mutation)
'''
# Example usage:
#parsed_data = decode_pb_file('path/to/your.pb')
#process_parsed_data(parsed_data)



def decode_pb_file(input_path):
    # Open the .pb file, read its contents, and parse it into an instance of the 'data' class
    with gzip.open(input_path, 'rb') as f:
        parsed_data = data()
        parsed_data.ParseFromString(f.read())
    return parsed_data



def prune_and_export_tree(input_path, k, output_path):
   parsed_data = decode_pb_file(input_path)
   new_tree = data()
   new_tree = process_parsed_data(parsed_data, k, new_tree)
   #new_tree = encode_tree(new_tree)
   write_pb_to_file(new_tree, output_path)


def main():
    parser = argparse.ArgumentParser(description="Prune and export a Protocol Buffer tree file.")
    parser.add_argument('tree_path', help="Path to the input Protocol Buffer tree file in pb format.")
    parser.add_argument('k_value', type=int, help="Minimum observation count for pruning.")
    parser.add_argument('output_path', help="Path to the output pruned Protocol Buffer tree file in pb format.")
    
    args = parser.parse_args()
    
    prune_and_export_tree(args.tree_path, args.k_value, args.output_path)

if __name__ == "__main__":
    main()
