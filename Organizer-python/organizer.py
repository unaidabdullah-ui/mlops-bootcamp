import os
import shutil
import argparse
import logging
from datetime import datetime

# ------------------------------------------
# LOGGING SETUP
# ------------------------------------------
log_filename = f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# ------------------------------------------
# FILE TYPE MAPPING
# ------------------------------------------
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
}


def get_category(extension):
    """Return category folder based on extension."""
    for category, ext_list in FILE_TYPES.items():
        if extension.lower() in ext_list:
            return category
    return "Others"


def organize_folder(path, dry_run=False):
    """Organize files in the given folder."""
    if not os.path.exists(path):
        logging.error(f"Path does not exist: {path}")
        return

    files = os.listdir(path)
    logging.info(f"Found {len(files)} items in the folder.")

    for file in files:
        file_path = os.path.join(path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        category = get_category(ext)
        target_folder = os.path.join(path, category)

        # Create folder if not exists
        if not os.path.exists(target_folder):
            logging.debug(f"Creating folder: {target_folder}")
            if not dry_run:
                os.makedirs(target_folder)

        # Move file
        new_location = os.path.join(target_folder, file)
        logging.info(f"Moving: {file} → {category}/")

        if not dry_run:
            shutil.move(file_path, new_location)

    logging.info("Organization complete!")


# ------------------------------------------
# ARGPARSE SETUP
# ------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="CLI File Organizer — Sort files by type."
    )

    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Folder path to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what will happen without moving files"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    organize_folder(args.path, args.dry_run)


if __name__ == "__main__":
    main()
