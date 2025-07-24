from pydantic import BaseModel
from typing import Union, List, Literal


class CustomerMessage(BaseModel):
    customer_id: str
    message: str
    product: str


# Bug report response data
class BugTicket(BaseModel):
    id: str
    title: str
    severity: str
    affected_component: str
    reproduction_steps: List[str]
    priority: str
    assigned_team: str


class BugReportResponseData(BaseModel):
    ticket: BugTicket


# Feature request response data
class ProductRequirement(BaseModel):
    id: str
    title: str
    description: str
    user_story: str
    business_value: str
    complexity_estimate: str
    affected_components: List[str]
    status: str


class FeatureRequestResponseData(BaseModel):
    product_requirement: ProductRequirement


# General inquiry response data
class SuggestedResource(BaseModel):
    title: str
    url: str


class GeneralInquiryResponseData(BaseModel):
    inquiry_category: Literal[
        "Account Management", "Billing", "Usage Question", "Other"
    ]
    requires_human_review: bool
    suggested_resources: List[SuggestedResource]


class CustomerResponse(BaseModel):
    message_type: Literal["bug_report", "feature_request", "general_inquiry"]
    confidence_score: float
    response_data: Union[
        BugReportResponseData, FeatureRequestResponseData, GeneralInquiryResponseData
    ]
    customer_response: str
