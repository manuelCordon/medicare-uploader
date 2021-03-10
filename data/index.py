# make it a constsant
def fields_definition():
    return [
        {
            'IndexFieldName': 'state',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': False,
                'SortEnabled': False
            }
        },
        {
            'IndexFieldName': 'plan_id',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': False,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': False
            }
        },
        {
            'IndexFieldName': 'name',
            'IndexFieldType': 'text',
            'TextOptions': {
                'ReturnEnabled': True,
                'SortEnabled': True,
                'HighlightEnabled': True
            }
        },
        {
            'IndexFieldName': 'carrier',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'premium',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'deductible',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'type',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'has_preferred_pharmacies',
            'IndexFieldType': 'literal',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'low_performer',
            'IndexFieldType': 'int',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'pharmacy_network_status',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'brand',
            'IndexFieldType': 'text',
            'TextOptions': {
                'ReturnEnabled': True,
                'SortEnabled': True,
                'HighlightEnabled': True
            }
        },
        {
            'IndexFieldName': 'medical_deductible',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'out_of_network_deductible',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'out_of_network_max_out_of_pocket',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'combined_deductible',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'combined_max_out_of_pocket',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'max_out_of_pocket',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'part_b_reimbursement',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'accepts_mail_order',
            'IndexFieldType': 'int',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'has_dental',
            'IndexFieldType': 'int',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'has_vision',
            'IndexFieldType': 'int',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'has_hearing',
            'IndexFieldType': 'int',
            'IntOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'coverage_type',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'annual_cost',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'drug_cost',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'health_cost',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'premium_range',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'savings',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'star_rating',
            'IndexFieldType': 'double',
            'DoubleOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'summary_of_benefits',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': False,
                'SearchEnabled': False,
                'ReturnEnabled': True,
                'SortEnabled': False
            }
        },
        {
            'IndexFieldName': 'policy_type',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'appointed',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        },
        {
            'IndexFieldName': 'nc',
            'IndexFieldType': 'literal',
            'LiteralOptions': {
                'FacetEnabled': True,
                'SearchEnabled': True,
                'ReturnEnabled': True,
                'SortEnabled': True
            }
        }
    ]
