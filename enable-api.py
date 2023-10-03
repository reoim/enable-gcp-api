import subprocess
import json
import argparse

def get_arguments():
    """
    Parsing the arugments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--organization', '-o', help='Example) --organization 302793038411', dest='org', required=True)
    parser.add_argument('--folder', '-f', help='Example) --folder 112793038411', dest='folder')
    parser.add_argument('--services', '-s', nargs='+', 
                        help='Example) --services "policyanalyzer.googleapis.com" "bigquery.googleapis.com"', 
                        default=[], dest='service', required=True)

    org_id = parser.parse_args().org
    folder_id = parser.parse_args().folder
    services_list = parser.parse_args().service

    return org_id, folder_id, services_list


def get_project_ids(org_id, folder_id):
    """Extracts list of project IDs from the output of the gcloud command.

    Args:
        org_id: Orgnazation ID
        folder_id: Folder ID

    Returns:
        List of project IDs.
    """
    if folder_id =='' or folder_id is None:
        command = ['gcloud', 'asset', 'search-all-resources', 
                        '--asset-types='+'cloudresourcemanager.googleapis.com/Project', 
                        '--scope=organizations/'+org_id, '--format=json']
    else:
        command = ['gcloud', 'asset', 'search-all-resources', 
                    '--asset-types='+'cloudresourcemanager.googleapis.com/Project', 
                    '--scope=folders/'+folder_id, '--format=json']

    output = subprocess.check_output(command)
    projects = json.loads(output)

    project_ids = []
    for project in projects:
        project_ids.append(project['additionalAttributes']['projectId'])
    return project_ids


def enable_api(services_list, project_id):
    """Enable services given project ID.

    Args:
        project_id: Project ID.
        services_list: Service Names of API to be enabled on the project
    """
    for service in services_list:
        print(f'Enable API: {service} for project "{project_id}"')
        subprocess.run(['gcloud', 'services', 'enable', service, '--project='+project_id])

org_id, folder_id, services_list = get_arguments()

# Extract the list of project IDs from the output.
project_ids = get_project_ids(org_id, folder_id)

for project_id in project_ids:
  enable_api(services_list, project_id)
