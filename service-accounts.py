def GenerateConfig(context):
    project_id = context.env['project']
    service_account = context.properties['service-account']
    resources = [
        {
            'name': service_account,
            'type': 'iam.v1.serviceAccount',
            'properties': {
                'accountId': service_account,
                'displayName': service_account,
                'projectId': project_id
            }
        },
        {
            'name': 'bind-iam-policy',
            'type': 'gcp-types/cloudresourcemanager-v1:virtual.projects.iamMemberBinding',
            'properties': {
                'resource': project_id,
                'role': 'projects/zillionx-master/roles/CloudOptyserviceRole',
                'member': 'serviceAccount:$(ref.' + service_account + '.email)'
            },
            'metadata': {
                'dependsOn': [service_account]
            }
        }
    ]

    return {'resources': resources}