from airflow.models import BaseOperator
from airflow.providers.openlineage.extractors import OperatorLineage
from airflow.providers.common.compat.openlineage.facet import Dataset


class PublishEventOperator(BaseOperator):
    def __init__(self, event_name: str, **kwargs):
        super().__init__(**kwargs)
        self.event_name = event_name

    def execute(self, context):
        print(f"Publishing event {self.event_name}")

    def get_openlineage_facets_on_start(self) -> OperatorLineage:
        return OperatorLineage(
            outputs=[Dataset(namespace="custom-eventbus", name=self.event_name)]
        )


class WaitForEventOperator(BaseOperator):
    def __init__(self, event_name: str, **kwargs):
        super().__init__(**kwargs)
        self.event_name = event_name

    def execute(self, context):
        print(f"Waiting for event {self.event_name}")

    def get_openlineage_facets_on_start(self) -> OperatorLineage:
        return OperatorLineage(
            inputs=[Dataset(namespace="custom-eventbus", name=self.event_name)]
        )
