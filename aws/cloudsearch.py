import boto3
import json
from functional import seq


def define_index(domain_name, fields):
    client = boto3.client('cloudsearch')

    # use for instead of lambda
    # use aioboto3 instead of boto3
    seq(fields).for_each(lambda f: __define_index_field(client, domain_name, f))

    print("Requesting document index")
    return client.index_documents(
        DomainName=domain_name
    )


def __define_index_field(client, domain_name, f):
    print("Adding %s field to domain %s" % (f['IndexFieldName'], domain_name))
    return client.define_index_field(
        DomainName=domain_name,
        IndexField=f
    )


def upload_plans(plans, cloudsearch_url):
    documents = seq(plans).map(lambda p: {
        'id': "%s-%d" % (p['state'], p['plan_id']),
        'type': 'add',
        'fields': p
    }).to_list()

    client = boto3.client(
        service_name='cloudsearchdomain',
        endpoint_url=cloudsearch_url
    )

    return client.upload_documents(
        documents=json.dumps(documents),
        contentType='application/json'
    )
