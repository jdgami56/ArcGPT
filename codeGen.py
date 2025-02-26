from diagrams import Diagram
from diagrams.aws.network import ALB
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.database import ElastiCache
from diagrams.aws.management import Cloudwatch
from diagrams.aws.analytics import Quicksight
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.analytics import Glue
from diagrams.onprem.queue import Kafka  # Using Kafka as an alternative for MSK
from diagrams.generic.storage import Storage  # Generic component for session storage

def create_diagram(filename):
    with Diagram("Cloud Architecture", show=False, filename='cloud_architecture_1740535252'):
        # Define AWS ALB for ingress traffic
        alb = ALB("ingress")

        # Define ECS Fargate services
        service1 = ECS("service1")
        service2 = ECS("service2")
        service3 = ECS("service3")

        # Define ElastiCache Redis for session storage
        redis = ElastiCache("session")

        # Define Amazon RDS PostgreSQL for user data
        rds = RDS("users")

        # Define Amazon CloudWatch for metrics
        cloudwatch = Cloudwatch("metric")

        # Define Amazon QuickSight for monitoring
        quicksight = Quicksight("monitoring")

        # Define Amazon Kinesis Data Firehose for logging
        firehose = KinesisDataFirehose("logging")

        # Define Kafka as an alternative for Amazon MSK
        msk = Kafka("stream")

        # Define AWS Glue for analytics
        glue = Glue("analytics")

        # Define connections
        alb >> [service1, service2, service3]
        service1 >> redis
        service2 >> redis
        service3 >> redis
        redis - Storage("session replica")  # Representing session replica
        rds - Storage("RDS replica")  # Representing RDS replica
        [service1, service2, service3] >> cloudwatch >> quicksight
        [service1, service2, service3] >> firehose >> msk >> glue

create_diagram("cloud_architecture")