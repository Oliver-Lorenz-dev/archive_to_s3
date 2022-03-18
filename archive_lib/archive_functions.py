import subprocess


def read_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
        data = list(map(str.strip, data))
        return data


def get_disk_usage(data_path):
    disk_usage = subprocess.check_output(['du', '-sh', data_path]).split()[0].decode('utf-8')
    return disk_usage


def get_job_queue(dir_size):
    if "T" in dir_size:
        job_queue = "basement"
    elif "G" in dir_size:
        job_queue = "long"
    elif "M" in dir_size:
        job_queue = "normal"
    elif "K" in dir_size and dir_size != "4.0K":
        job_queue = "small"
    else:
        job_queue = "empty"
    return job_queue


def generate_commands(job_queue, bucket, user, path):
    quote = '"'
    rclone_command = f"{quote}rclone sync --exclude '.**' {path} remote:{bucket}/{user}{quote}"
    bsub_command = f"bsub -J {user}_lustre_archive -o {user}.out -e {user}.err -R {quote}select[mem>5000] rusage[mem=5000]{quote} -M5000 -q {job_queue} "
    archive_command = f"{bsub_command}{rclone_command}"
    return archive_command


def generate_dry_run_command(bucket, user, path):
    rclone_command = f"rclone sync --dry-run --exclude '.**' {path} remote:{bucket}/{user}"
    return rclone_command


def get_user(path):
    user = path.split("/")[-1]
    return user