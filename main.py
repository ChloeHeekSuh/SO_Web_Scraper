from so import get_jobs as get_so_jobs
from save import save_to_file, save_file_to_s3

jobs = get_so_jobs()

save_to_file(jobs)

save_file_to_s3()
