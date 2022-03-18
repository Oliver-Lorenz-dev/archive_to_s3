def generate_delete_command(bucket, user):
    quote = '"'
    bsub_command = f"bsub -J {user}_delete_archive -o {user}.out -e {user}.err -R {quote}select[mem>5000] rusage[mem=5000]{quote} -M5000 "
    rclone_command = f"{quote}rclone delete remote:{bucket}/{user}{quote}"
    delete_command = f"{bsub_command}{rclone_command}"
    return delete_command


def generate_delete_command_dry_run(bucket, user):
    quote = '"'
    rclone_command = f"{quote}rclone delete --dry-run remote:{bucket}/{user}{quote}"
    return rclone_command
