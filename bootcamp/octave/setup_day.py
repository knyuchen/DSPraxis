#!/usr/bin/env python3
"""
Setup script for creating new day folders in the Octave DSP bootcamp.
Usage: python3 setup_day.py <week> <day> [topic]
"""

import os
import sys
import shutil
from datetime import datetime


def setup_day(week_num, day_num, topic=None):
    """Create a new day folder by copying the template."""
    
    # Validate inputs
    if not (1 <= week_num <= 6):
        print("Error: Week number must be between 1 and 6")
        return False
    
    if not (1 <= day_num <= 7):
        print("Error: Day number must be between 1 and 7")
        return False
    
    # Create paths
    template_path = "template_day"
    week_folder = f"week{week_num}"
    day_folder = f"day{day_num}"
    target_path = os.path.join(week_folder, day_folder)
    
    # Check if target already exists
    if os.path.exists(target_path):
        print(f"Warning: {target_path} already exists!")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return False
    
    # Create week folder if it doesn't exist
    if not os.path.exists(week_folder):
        os.makedirs(week_folder)
        print(f"Created week folder: {week_folder}")
    
    # Copy template to target
    try:
        shutil.copytree(template_path, target_path, dirs_exist_ok=True)
        print(f"Created day folder: {target_path}")
    except Exception as e:
        print(f"Error copying template: {e}")
        return False
    
    # Update main.m with day info
    main_m_path = os.path.join(target_path, "main.m")
    try:
        with open(main_m_path, 'r') as f:
            content = f.read()
        
        # Update the header
        today = datetime.now().strftime("%Y-%m-%d")
        topic_text = topic if topic else f"Week {week_num} Day {day_num} Practice"
        
        content = content.replace("Day X Practice - [Topic]", f"Day {day_num} Practice - {topic_text}")
        content = content.replace("[Date]", today)
        content = content.replace("[List of goals for this day]", f"Complete Week {week_num} Day {day_num} exercises")
        
        with open(main_m_path, 'w') as f:
            f.write(content)
        
        print(f"Updated main.m with day {day_num} information")
        
    except Exception as e:
        print(f"Error updating main.m: {e}")
    
    # Update README.md with day info
    readme_path = os.path.join(target_path, "README.md")
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
        
        today = datetime.now().strftime("%Y-%m-%d")
        topic_text = topic if topic else f"Week {week_num} Day {day_num} Practice"
        
        content = content.replace("Day X - [Topic]", f"Day {day_num} - {topic_text}")
        content = content.replace("[Date]", today)
        content = content.replace("[Week Number]", str(week_num))
        content = content.replace("[Main topic for this day]", topic_text)
        
        with open(readme_path, 'w') as f:
            f.write(content)
        
        print(f"Updated README.md with day {day_num} information")
        
    except Exception as e:
        print(f"Error updating README.md: {e}")
    
    print(f"\n✅ Successfully created {target_path}")
    print(f"📁 Navigate to: cd {target_path}")
    print(f"🔬 Run with Octave: octave main.m")
    
    return True


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python3 setup_day.py <week> <day> [topic]")
        print("Example: python3 setup_day.py 1 2 'Signal Analysis'")
        print("Example: python3 setup_day.py 2 1")
        return
    
    try:
        week_num = int(sys.argv[1])
        day_num = int(sys.argv[2])
        topic = sys.argv[3] if len(sys.argv) > 3 else None
        
        setup_day(week_num, day_num, topic)
        
    except ValueError:
        print("Error: Week and day must be numbers")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
