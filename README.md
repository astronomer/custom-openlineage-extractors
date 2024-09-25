Overview
========

This example Astro CLI project demonstrates how to use custom OpenLineage extractors to create cross-DAG dependencies.

In `include/operators.py`, we have two custom operators defined:

- PublishEventOperator: This operator publishes an event to an event stream.
- WaitForEventOperator: This operator waits for an event to be published to an event stream.

Each operator has OpenLineage extraction functions defined.
