# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
Example of authenticating with SPN + Secret
Can be expanded to retrieve values from Key Vault or other sources
"""
# Kevin Chant extended this...
# START-EXAMPLE
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items, append_feature_flag
import argparse

parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('--WorkspaceId', type=str)
parser.add_argument('--Environment', type=str)
parser.add_argument('--RepositoryDirectory', type=str)
parser.add_argument('--FeatureFlags', type=str)
args = parser.parse_args()

# Convert fabric_cicd_feature_flags into a list
featflags = args.FeatureFlags
featflags = featflags.replace(" ", "")
fabric_cicd_feature_flags = featflags.split(",")

for flag in fabric_cicd_feature_flags:
    print("Append feature flag: ", flag)
    append_feature_flag(flag)

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id= args.WorkspaceId,
    environment=args.Environment,
    repository_directory=args.RepositoryDirectory, 
    # item_type_in_scope=item_type_in_scope,  
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)
