import argparse
import os
from archive_lib.archive_functions import read_file, get_user
from archive_lib.delete_from_remote import generate_delete_command, generate_delete_command_dry_run

parser = argparse.ArgumentParser()
parser.add_argument("--print", "-p", help="Print Rclone commands", required=False, action="store_true")
parser.add_argument("--dryrun", "-dr", help="Dry run the rclone command", required=False, action="store_true")
parser.add_argument("--delete", "-d", help="Run the delete commands", required=False, action="store_true")
parser.add_argument("--input", "-i", help="Path to file containing remote paths - see remote_paths.txt", required=True)
args = parser.parse_args()


def delete(args):
    data = read_file(args.input)
    if not args.print and not args.dryrun and not args.delete:
        print("Please provide 1 of the following arguments: --print , --dryrun, --delete")
    for path in data:
        user = get_user(path)
        bucket = path.split("/")[0]
        command = generate_delete_command(bucket, user)
        if args.print:
            print(command)
        elif args.dryrun:
            dry_run_command = generate_delete_command_dry_run(bucket, user)
            os.system(dry_run_command)
        elif args.delete:
            os.system(command)


if __name__ == '__main__':
    delete(args)