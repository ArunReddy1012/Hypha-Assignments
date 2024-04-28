#!/bin/bash

DB_USER="root"
read -p "Enter the Password" DB_PASS
DB_NAME="test"

# Backup directory
BACKUP_DIR="/home/db"

# Function to backup MySQL database
backup_mysql() {
    # Create backup directory if it doesn't exist
    mkdir -p "$BACKUP_DIR"
    echo "++++++++++++++++++creating the directory: $BACKUP_DIR"

    # Backup filename
    BACKUP_FILE="$BACKUP_DIR/backup_$(date +'%Y%m%d_%H%M%S').sql"
    echo "++++++++++++++creating the backup file: $BACKUP_FILE"

    # Dump MySQL database
    mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_FILE"
    echo "##################  Dump ####################### "

    # Compress backup file
    gzip "$BACKUP_FILE"
    echo "++++++++++++++++++++compressed to: $BACKUP_FILE"
}

# Function to restore MySQL database
restore_mysql() {
    # List available backup files
    ls -ltrh "$BACKUP_DIR"

    # Prompt user to enter backup file name
    read -p "Enter the backup file name to restore: " BACKUP_FILE_NAME

    # Decompress backup file
    gunzip -c "$BACKUP_DIR/$BACKUP_FILE_NAME" > "$BACKUP_DIR/restore.sql"

    # Restore MySQL database
    mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" < "$BACKUP_DIR/restore.sql"
    echo "################## restoration completed  ##################### "

    # Clean up
    rm "$BACKUP_DIR/restore.sql"
}

# Main menu
while true; do
    echo "1. Backup MySQL database"
    echo "2. Restore MySQL database"
    echo "3. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1) backup_mysql ;;
        2) restore_mysql ;;
        3) exit ;;
        *) echo "Invalid choice. Please enter 1, 2, or 3." ;;
    esac
done
