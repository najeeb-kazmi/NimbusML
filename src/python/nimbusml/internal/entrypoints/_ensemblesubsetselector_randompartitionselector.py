# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
RandomPartitionSelector
"""


from ..utils.entrypoints import Component
from ..utils.utils import try_set


def random_partition_selector(
        feature_selector=None,
        **params):
    """
    **Description**
        None

    :param feature_selector: The Feature selector (settings).
    """

    entrypoint_name = 'RandomPartitionSelector'
    settings = {}

    if feature_selector is not None:
        settings['FeatureSelector'] = try_set(
            obj=feature_selector, none_acceptable=True, is_of_type=dict)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleSubsetSelector')
    return component