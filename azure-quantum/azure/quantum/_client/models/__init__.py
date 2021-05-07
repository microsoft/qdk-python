# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .error_data_py3 import ErrorData
    from .job_details_py3 import JobDetails
    from .blob_details_py3 import BlobDetails
    from .sas_uri_response_py3 import SasUriResponse
    from .target_status_py3 import TargetStatus
    from .provider_status_py3 import ProviderStatus
    from .quota_py3 import Quota
    from .rest_error_py3 import RestError, RestErrorException
except (SyntaxError, ImportError):
    from .error_data import ErrorData
    from .job_details import JobDetails
    from .blob_details import BlobDetails
    from .sas_uri_response import SasUriResponse
    from .target_status import TargetStatus
    from .provider_status import ProviderStatus
    from .quota import Quota
    from .rest_error import RestError, RestErrorException
from .job_details_paged import JobDetailsPaged
from .provider_status_paged import ProviderStatusPaged
from .quota_paged import QuotaPaged
from .quantum_client_enums import (
    JobStatus,
    ProviderAvailability,
    TargetAvailability,
    DimensionScope,
    MeterPeriod,
)

__all__ = [
    "ErrorData",
    "JobDetails",
    "BlobDetails",
    "SasUriResponse",
    "TargetStatus",
    "ProviderStatus",
    "Quota",
    "RestError",
    "RestErrorException",
    "JobDetailsPaged",
    "ProviderStatusPaged",
    "QuotaPaged",
    "JobStatus",
    "ProviderAvailability",
    "TargetAvailability",
    "DimensionScope",
    "MeterPeriod",
]
