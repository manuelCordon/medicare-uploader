from functional import seq


def __get_generic(plans, key):
    return seq(plans.values()) \
        .filter(lambda i: key in i) \
        .flat_map(lambda i: i[key]) \
        .map(lambda c: (c['val'], c['name'])) \
        .to_dict()


def __yes_no(param):
    return param.lower().startswith('y')


def __pharmacy_preference(param):
    pharmacy_preferences = {
        -1: 'NA',
        0: 'out',
        1: 'in',
        2: 'pref retail',
        3: 'pref mail',
        4: 'pref both'
    }
    return pharmacy_preferences.get(param)


def __format_plan(plan, premium_ranges, appointments, policy_types, ncs):
    output = {
        'state': plan['stateAbbr'],
        'plan_id': plan['id'],
        'name': plan['name'],
        'carrier': plan['carrierName'],
        'premium': plan['premium'],
        'deductible': plan['deductible'],
        'type': plan['type'],
        'has_preferred_pharmacies': __pharmacy_preference(plan['hasPreferredPharmacies']),
        'low_performer': plan['lowPerformer'],
        'pharmacy_network_status': plan['pharmacyNetworkStatus'],
        'brand': plan['brand'],
        'medical_deductible': plan['medicalDeductible'],
        'out_of_network_deductible': plan['oonDeductible'],
        'out_of_network_max_out_of_pocket': plan['oonMoop'],
        'combined_deductible': plan['combDeductible'],
        'combined_max_out_of_pocket': plan['combMoop'],
        'max_out_of_pocket': plan['moop'],
        'part_b_reimbursement': plan['partBReimbursement'],
        'accepts_mail_order': __yes_no(plan['acceptsMailOrder']),
        'has_dental': __yes_no(plan['hasDental']),
        'has_vision': __yes_no(plan['hasVision']),
        'has_hearing': __yes_no(plan['hasHearing']),
        'coverage_type': plan['coverageType'],
        'annual_cost': plan['annualCost'],
        'drug_cost': plan['drugCost'],
        'health_cost': plan['healthCost'],
        'premium_range': premium_ranges[plan['premiumRange']],
        'savings': plan['savings']
    }

    # Add optional fields.
    if plan['fmtRating'].isdecimal():
        output['star_rating'] = plan['fmtRating']

    if plan['sobUrl'] != '#':
        output['summary_of_benefits'] = plan['sobUrl']

    if plan.get('policyTypeId') in policy_types:
        output['policy_type'] = policy_types[plan['policyTypeId']]

    if plan.get('appointedId') in appointments:
        output['appointed'] = appointments[plan['appointedId']]

    if plan.get('ncId') in ncs:
        output['nc'] = ncs[plan['ncId']]

    return output


def build_plans(plans):
    premium_ranges = __get_generic(plans, 'premium')
    appointments = __get_generic(plans, 'appointed')
    policy_types = __get_generic(plans, 'policyType')
    ncs = __get_generic(plans, 'nc')

    return seq(plans['plans']) \
        .map(lambda p: __format_plan(p, premium_ranges, appointments, policy_types, ncs)) \
        .to_list()
