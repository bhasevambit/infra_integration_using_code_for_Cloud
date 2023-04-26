import aws_cdk as cdk
import aws_cdk.aws_s3 as s3


class AwsCdkTrainingForPythonStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, "first-s3-bucket-by-cdk-python",
            bucket_name="first-s3-bucket-by-cdk-python-353981446712",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=True,
                block_public_policy=True,
                ignore_public_acls=True,
                restrict_public_buckets=True
            )
        )
