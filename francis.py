# Francis - Deadline Assistant
# Python version for PC

import csv
import os
from datetime import datetime
import time
import subprocess

# Configuration
EVENTS_FILE = "francis_events.csv"

# English texts
TEXTS = {
    "title": "Francis - Deadline Assistant",
    "menu": "Select an option:\n1. View events\n2. Add event\n3. Delete event\n4. Sync with GitHub\n5. Exit",
    "add_event": "Add new event",
    "event_type": "Event type (1.University, 2.Music, 3.Work, 4.Rest): ",
    "event_name": "Event name: ",
    "event_date": "Event date (YYYY-MM-DD): ",
    "days_left": "days left",
    "university": "University",
    "music": "Music",
    "work": "Work",
    "rest": "Rest",
    "today_events": "Today's events",
    "upcoming_events": "Upcoming events",
    "no_events": "No scheduled events",
    "select_event": "Select event to delete: ",
    "goodbye": "Goodbye!",
    "sync_success": "Synchronization successful!",
    "sync_fail": "Synchronization failed!"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_days_left(event_date):
    today = datetime.today().date()
    event_date = datetime.strptime(event_date, "%Y-%m-%d").date()
    return (event_date - today).days

def load_events():
    events = []
    if os.path.exists(EVENTS_FILE):
        try:
            with open(EVENTS_FILE, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    events.append(row)
        except:
            pass
    return events

def save_events(events):
    try:
        with open(EVENTS_FILE, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Type', 'Name', 'Date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for event in events:
                writer.writerow(event)
        return True
    except:
        return False

def show_events():
    events = load_events()
    today = datetime.today().strftime("%Y-%m-%d")
    
    print(f"\n{TEXTS['title']}")
    print("=" * 40)
    
    # Today's events
    today_events = [event for event in events if event['Date'] == today]
    if today_events:
        print(f"\n{TEXTS['today_events']}:")
        for event in today_events:
            print(f" - {event['Type']}: {event['Name']} (TODAY)")
    
    # Upcoming events
    upcoming_events = [event for event in events if event['Date'] > today]
    upcoming_events.sort(key=lambda x: x['Date'])
    
    if upcoming_events:
        print(f"\n{TEXTS['upcoming_events']}:")
        for i, event in enumerate(upcoming_events, 1):
            days_left = get_days_left(event['Date'])
            event_type_display = TEXTS.get(event['Type'].lower(), event['Type'])
            print(f" {i}. {event_type_display}: {event['Name']} - {event['Date']} ({days_left} {TEXTS['days_left']})")
    
    if not today_events and not upcoming_events:
        print(f"\n{TEXTS['no_events']}")
    
    print("\n")

def sync_with_github():
    """Sincroniza automáticamente con GitHub"""
    try:
        # Detectar la rama actual
        branch_result = subprocess.run(["git", "branch", "--show-current"], 
                                     capture_output=True, text=True)
        current_branch = branch_result.stdout.strip()
        
        if not current_branch:
            print("✗ Could not determine current branch")
            return False
        
        # Agregar todos los cambios
        subprocess.run(["git", "add", "."], check=True)
        
        # Hacer commit
        commit_message = f"Auto-sync from PC: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Hacer push
        subprocess.run(["git", "push", "origin", current_branch], check=True)
        
        print("✓ Changes synchronized with GitHub")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Synchronization failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Synchronization error: {str(e)}")
        return False

def add_event():
    print(f"\n{TEXTS['add_event']}")
    
    # Event type
    type_input = input(TEXTS['event_type'])
    event_type = ""
    if type_input == "1":
        event_type = "University"
    elif type_input == "2":
        event_type = "Music"
    elif type_input == "3":
        event_type = "Work"
    elif type_input == "4":
        event_type = "Rest"
    else:
        event_type = type_input
    
    # Event name
    name = input(TEXTS['event_name'])
    if not name.strip():
        print("Event name cannot be empty.")
        return
    
    # Event date
    date = input(TEXTS['event_date'])
    
    # Validate date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    
    # Add event
    events = load_events()
    new_event = {'Type': event_type, 'Name': name, 'Date': date}
    events.append(new_event)
    
    if save_events(events):
        print("Event added successfully!")
        sync_with_github()
    else:
        print("Failed to add event.")

def delete_event():
    events = load_events()
    today = datetime.today().strftime("%Y-%m-%d")
    upcoming_events = [event for event in events if event['Date'] >= today]
    upcoming_events.sort(key=lambda x: x['Date'])
    
    if not upcoming_events:
        print(TEXTS['no_events'])
        return
    
    print(f"\n{TEXTS['select_event']}")
    for i, event in enumerate(upcoming_events, 1):
        days_left = get_days_left(event['Date'])
        event_type_display = TEXTS.get(event['Type'].lower(), event['Type'])
        print(f" {i}. {event_type_display}: {event['Name']} - {event['Date']} ({days_left} {TEXTS['days_left']})")
    
    selection = input("\nEnter the event number to delete (0 to cancel): ")
    try:
        index = int(selection) - 1
    except ValueError:
        print("Invalid selection.")
        return
    
    if selection == "0":
        return
    
    if 0 <= index < len(upcoming_events):
        event_to_delete = upcoming_events[index]
        events = [event for event in events if not (
            event['Type'] == event_to_delete['Type'] and
            event['Name'] == event_to_delete['Name'] and
            event['Date'] == event_to_delete['Date']
        )]
        
        if save_events(events):
            print("Event deleted successfully!")
            sync_with_github()
        else:
            print("Failed to delete event.")
    else:
        print("Invalid selection.")

def main():
    # Create events file if it doesn't exist
    if not os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Name', 'Date'])
    
    while True:
        clear_screen()
        show_events()
        
        choice = input(TEXTS['menu'] + "\n")
        
        if choice == "1":
            show_events()
            input("Press Enter to continue...")
        elif choice == "2":
            add_event()
            input("Press Enter to continue...")
        elif choice == "3":
            delete_event()
            input("Press Enter to continue...")
        elif choice == "4":
            sync_with_github()
            input("Press Enter to continue...")
        elif choice == "5":
            print(TEXTS['goodbye'])
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main()
