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
    
    #makes a dictionary of all the leaves and how many times they are found
    leaf_counts = {}
    for node in node_list:
        leaf_counts[node] = int(0)
        for child in tree.get_node(node.id).children:
            if tree.get_node(child.id).is_leaf() == True and tree.get_node(child.id).branch_length == 0:
                leaf_counts[node] = leaf_counts[node] + 1

    
    
    #removes all leaves not repeated more than k times
    remove_list = []
    for node in node_list:
        if leaf_counts[node] < k:
            for child in tree.get_node(node.id).children:
                if tree.get_node(child.id).is_leaf() == True:
                    remove_list.append(child)
        if leaf_counts[node] >= k:
            for child in tree.get_node(node.id).children:
                if tree.get_node(child.id).is_leaf() == True and tree.get_node(child.id).branch_length != 0:
                    remove_list.append(child)
    
    for node in remove_list:
        tree.remove_node(node.id)
        
    
    node_list = tree.breadth_first_expansion()
    
    '''
    # moves up child nodes to their parents positiosn if need be
    changed_nodes = {}
    remove_list = []
    for node in node_list:
        #if len(tree.get_node(node.id).children) == 1 and len(tree.get_node(node.id).mutations) == 0:
        if len(tree.get_node(node.id).children) == 1:
            remove_list.append(node)
            changed_nodes = update_child_positions(tree, node, changed_nodes)
        
    for key, value in changed_nodes:
        tree.move_node(key.id, value.id)
    for node in remove_list:
        tree.remove_node(node.id)        
      '''  
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