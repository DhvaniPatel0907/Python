
# Skill Track Pro
# Manage certifications, skills, and learning records
# Using Object-Oriented Programming (OOP) in Python


class SkillRecord:
    """Class to represent a single skill/certification record."""

    def __init__(self, skill_name, platform, completion_date, certificate_link=None):
        self.skill_name = skill_name
        self.platform = platform
        self.completion_date = completion_date
        self.certificate_link = certificate_link

    def __str__(self):
        """Readable format for displaying a record."""
        return f"Skill: {self.skill_name}, Platform: {self.platform}, Date: {self.completion_date}, Certificate: {self.certificate_link}"


class SkillTrackPro:
    """Main application class for managing skill records."""

    def __init__(self):
        self.records = []  # store all SkillRecord objects

    # ---------- CRUD Operations ----------
    def create_record(self, skill_name, platform, completion_date, certificate_link=None):
        """Create a new skill record and add it to the list."""
        record = SkillRecord(skill_name, platform, completion_date, certificate_link)
        self.records.append(record)
        print(" Record added successfully!")

    def read_records(self):
        """Display all stored records."""
        if not self.records:
            print("No records found.")
        else:
            print("\nYour Skill Records:")
            for idx, record in enumerate(self.records, start=1):
                print(f"{idx}. {record}")

    def update_record(self, index, skill_name=None, platform=None, completion_date=None, certificate_link=None):
        """Update specific details of a record."""
        if 0 <= index < len(self.records):
            record = self.records[index]
            if skill_name:
                record.skill_name = skill_name
            if platform:
                record.platform = platform
            if completion_date:
                record.completion_date = completion_date
            if certificate_link:
                record.certificate_link = certificate_link
            print(" Record updated successfully!")
        else:
            print(" Invalid record index!")

    def delete_record(self, index):
        """Delete a record by its index."""
        if 0 <= index < len(self.records):
            removed = self.records.pop(index)
            print(f" Record '{removed.skill_name}' deleted successfully!")
        else:
            print(" Invalid record index!")

    #  Helper 
    def menu(self):
        """Interactive menu for the user to perform actions."""
        while True:
            print("\n===== Skill Track Pro Menu =====")
            print("1. Add New Skill Record")
            print("2. View All Records")
            print("3. Update a Record")
            print("4. Delete a Record")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                skill = input("Enter skill/certification name: ")
                platform = input("Enter platform (Coursera, Udemy, etc.): ")
                date = input("Enter completion date (YYYY-MM-DD): ")
                cert = input("Enter certificate link (optional): ")
                self.create_record(skill, platform, date, cert if cert else None)

            elif choice == "2":
                self.read_records()

            elif choice == "3":
                self.read_records()
                idx = int(input("Enter record number to update: ")) - 1
                skill = input("New skill name (press Enter to skip): ")
                platform = input("New platform (press Enter to skip): ")
                date = input("New completion date (press Enter to skip): ")
                cert = input("New certificate link (press Enter to skip): ")
                self.update_record(idx,
                                   skill_name=skill if skill else None,
                                   platform=platform if platform else None,
                                   completion_date=date if date else None,
                                   certificate_link=cert if cert else None)

            elif choice == "4":
                self.read_records()
                idx = int(input("Enter record number to delete: ")) - 1
                self.delete_record(idx)

            elif choice == "5":
                print(" Exiting Skill Track Pro. Goodbye!")
                break

            else:
                print(" Invalid choice. Please try again.")


# ----------- Run Application -----------
if __name__ == "__main__":
    app = SkillTrackPro()
    app.menu()
