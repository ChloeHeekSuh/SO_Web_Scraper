import csv
import boto3
from keys import KEY_ID, SECRET_KEY




def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "apply_link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


def save_file_to_s3():
    s3 = boto3.client(
            's3',
            aws_access_key_id=KEY_ID,
            aws_secret_access_key=SECRET_KEY
    )
    s3.upload_file(r"YOUR/FILE/PATH", 'YOUR/BUCKET/NAME', 'FILE_NAME_YOU_WANT_TO_SAVE_IN_S3')
    print("successfully saved!")
