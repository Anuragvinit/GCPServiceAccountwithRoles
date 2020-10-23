def GenerateConfig(context):
    project_id = context.env['project']
    service_account = context.properties['service-account']
    resources = [
        {
            'name': cloudopty-serviceaccountTest,
            'type': 'iam.v1.serviceAccount',
            'properties': {
                'accountId': cloudopty-serviceaccountTest,
                'displayName': cloudopty-serviceaccountTest,
                'projectId': project_id
            }
        },
        {
            'name': 'bind-iam-policy',
            'type': 'gcp-types/cloudresourcemanager-v1:virtual.projects.iamMemberBinding',
            'properties': {
                'resource': project_id,
                'role': 'projects/'+project_id+'/roles/CloudOptyserviceRole',
                'member': 'serviceAccount:$(ref.' + service_account + '.email)'
            },
            'metadata': {
                'dependsOn': [service_account]
            }
        }
    ]

    return {'resources': resources}
