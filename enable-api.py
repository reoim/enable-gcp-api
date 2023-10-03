import subprocess
import json

def get_project_ids(organization):
    """Extracts list of project IDs from the output of the gcloud command.

    Args:
        output: Output of the gcloud command.

    Returns:
        List of project IDs.
    """
    if folder == '':
        command = ['gcloud', 'asset', 'search-all-resources', 
                    '--asset-types='+'cloudresourcemanager.googleapis.com/Project', 
                    '--scope=organizations/'+organization, '--format=json']
    else:
        command = ['gcloud', 'asset', 'search-all-resources', 
                    '--asset-types='+'cloudresourcemanager.googleapis.com/Project', 
                    '--scope=folders/'+folder, '--format=json']

    output = subprocess.check_output(command)
    projects = json.loads(output)

    project_ids = []
    for project in projects:
        project_ids.append(project['additionalAttributes']['projectId'])
    return project_ids

def enable_api(service, project_id):
    """Runs a command for a given project ID.

    Args:
        project_id: Project ID.
        command: Command to run.
    """
    print(f'Enable API: {service} for project "{project_id}"')
    subprocess.run(['gcloud', 'services', 'enable', service, '--project='+project_id])

          

# Get the organization parameter.
organization = input('Enter the organization id: ')
if organization =='':
    print('Please enter the organization id')
    exit()

# Get the folder parameter.
print('\nBy default, this script will enalbe the API for all projects under the organization')
folder = input('Enter the folder id if you want to enable the API only at the folder level: ')

# Get the service parameter.
print('\nService name example: policyanalyzer.googleapis.com')
service = input('Enter the service name of the API that you want to enable: ')


# Extract the list of project IDs from the output.
project_ids = get_project_ids(organization)

# Run the command for each project ID.
for project_id in project_ids:
  enable_api(service, project_id)
