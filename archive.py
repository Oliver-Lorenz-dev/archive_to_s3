import argparse
import os
from archive_lib.archive_functions import read_file, get_disk_usage, get_job_queue, generate_commands, \
    get_user, generate_dry_run_command

parser = argparse.ArgumentParser()
parser.add_argument("--print", "-p", help="Print Rclone commands", required=False, action="store_true")
parser.add_argument("--dryrun", "-d", help="Dry run the rclone command", required=False, action="store_true")
parser.add_argument("--archive", "-a", help="Run the archive commands", required=False, action="store_true")
parser.add_argument("--no-du", "-nd", help="Don't run du - assume 1TB for all", required=False, action="store_true")
parser.add_argument("--bucket", "-b", help="Bucket name e.g. 'test_bucket'", required=True)
parser.add_argument("--input", "-i", help="Path to file containing lustre paths - see lustre_paths.txt", required=True)
args = parser.parse_args()


def archive(args):
    data = read_file(args.input)
    if not args.print and not args.dryrun and not args.archive:
        print("Please provide 1 of the following arguments: --print , --dryrun, --archive")
    for path in data:
        user = get_user(path)
        if not args.no_du:
            dir_size = get_disk_usage(path)
        elif args.no_du:
            dir_size = "TB"
        job_queue = get_job_queue(dir_size)
        if job_queue == "empty":
            continue
        command = generate_commands(job_queue, args.bucket, user, path)
        if args.print:
            print(command)
        elif args.dryrun:
            dry_run_command = generate_dry_run_command(args.bucket, user, path)
            os.system(dry_run_command)
        elif args.archive:
            os.system(command)


if __name__ == '__main__':
    archive(args)
