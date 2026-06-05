import os, shutil, datetime, schedule, time

source_dir = "/Users/hunterhalvorson/Downloads/python_automation"
destination_dir = "/Users/hunterhalvorson/Downloads/Backups"


def copy_folder_to_director(source, dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest, str(today))

  try:
    shutil.copytree(source, dest_dir)
    print(f"Folder copied to: {dest_dir}")
  except FileExistsError:
    print(f"Folder already exists in: {dest}")

schedule.every().day.at("13:04").do(lambda: copy_folder_to_director(source_dir, destination_dir))

while True:
  schedule.run_pending()
  time.sleep(60)