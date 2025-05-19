import bte
import argparse

def update_child_positions(tree, node, changed_nodes):
    for child in tree.get_node(node.id).children:
        changed_nodes[tree.get_node(child.id)] = tree.get_node(node.id)
        if len(tree.get_node(child.id).children) != 0:
            update_child_positions(tree, child, changed_nodes)


def prune_and_export_tree(input_path, k, output_path):
    # Load the tree from the input Protocol Buffer tree file
    tree = bte.MATree(input_path)
    
    #Make a list of all nodes in the tree with their mutations
    node_list = tree.breadth_first_expansion()
    
    #makes a dictionary of all the mutations and how many times they are found
    mutation_counts = {}
    for node in node_list:
        for mutation in tree.get_node(node.id).mutations:
            if mutation in mutation_counts:
                mutation_counts[mutation] = mutation_counts[mutation] + 1
            else:
                mutation_counts[mutation] = 0

 
    
    #removes all mutations not repeated more than k times
    remove_list = []
    for node in node_list:
        mutation_list = []
        for mutation in tree.get_node(node.id).mutations:
            if mutation_counts[mutation] >= k:
                mutation_list.append(mutation)
        node.update_mutations(mutation_list)        
    
    node_list = tree.breadth_first_expansion()
    
    
    
    #removes all leaves with no mutations
    remove_node = []
    for node in node_list:
        #for child in tree.get_node(node.id).children:
        if len(tree.get_node(node.id).mutations) == 0 and len(tree.get_node(node.id).children) == 0:
            remove_node.append(node)
                
                
    for node in remove_node:
        tree.remove_node(node.id)
        
    return tree.save_pb(output_path)
    
    

def main():
    parser = argparse.ArgumentParser(description="Prune and export a Protocol Buffer tree file.")
    parser.add_argument('tree_path', help="Path to the input Protocol Buffer tree file in pb format.")
    parser.add_argument('k_value', type=int, help="Minimum observation count for pruning.")
    parser.add_argument('output_path', help="Path to the output pruned Protocol Buffer tree file in pb format.")
    
    args = parser.parse_args()
    
    prune_and_export_tree(args.tree_path, args.k_value, args.output_path)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
  #  every node in the tree, and for each internal node ask how many decendents with branh length zero 
  
  
  
  
  
  def foo(list)